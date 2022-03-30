


import json
import os
from queue import Queue
import time
import networkx
import random
import tweepy



class UserExtractor:

    # set the waiting time
    Time=0
    fullStructure = None


    @staticmethod
    def crawlUser(extractor,context,graph,fullSchema):
        UserExtractor.fullStructure = fullSchema

        # print(extractor)
        # print(fullSchema)
        # print(userQueue)
        # print(coordinatesQueue)
        freshUser = context.get("Twitter_User_ID",False)
        UserExtractor.insertUser(extractor,freshUser,graph)

        while True:
            # print("again")
            # print(freshUser.screen_name)


            try:
                print("Collecting data for ",freshUser)  
                
                UserExtractor.scrapFollowers(freshUser,context,extractor,graph)
                
                UserExtractor.scrapFriends(freshUser,context,extractor,graph)

                # getting the timeline..
                # usertweets = extractor.user_timeline(screen_name=freshUser.screen_name, 
                #            # 200 is the maximum allowed count
                #            count=200,

                #            include_rts = False,
                #            # Necessary to keep full_text 
                #            # otherwise only the first 140 words are extracted
                #            tweet_mode = 'extended'
                #            )

                # if(UserExtractor.fullStructure["tweet"]):
                #     for tweet in usertweets:
                #         print("adding a tweet")
                #         # graph.add_edge(freshUser.id,tweet.id,other= "published")#done inside tweetExtractor
                #         tweetQueue.put(tweet)

            except tweepy.TweepyException as ex: 
                print("An exception has occured :")
                print(ex)
                break





    # count = 0

    @staticmethod
    def insertUser(extractor,user_id,graph): # verifies existence inside
        
        attributes = {}
        # user= json.dumps(user)
        # user = tweepy.API(extractor.getAuth()).get_user(user_id=user_id)
        # print(user.id)
        print(graph)
        # print(UserExtractor.fullStructure)
        if(user_id in graph): #nothing to do here
            return 
        attributes["id"] = user_id
        # for attribute in UserExtractor.fullStructure["user"]:
            # attributes[str(attribute)+""] = str(getattr(user,attribute))
        

        # print(attributes)
        
        # print(attributes.items())
        # if(len(attributes.items()) > 2) :
        #     graph.add_nodes_from([(user.id,[k for k in attributes.items()])],color="green")
        
        graph.add_nodes_from([(user_id,[k for k in attributes.items()])],color="green")
        

    @staticmethod
    def scrapFriends(freshUser,context,extractor,graph):
        # if freshUser.friends_count<UserExtractor.Limited_number_of_friends:
        # collect the list of the user v friends
        Friends = []
        for user in tweepy.Cursor(tweepy.API(extractor.getAuth()).get_friend_ids, user_id=freshUser,count=context.get("Follower_Friend_Limit")).items():
        #     try:
        #         Friends.extend(page)
        #     except tweepy.TweepError as e:
        #         print("Going to sleep:", e)
        #         time.sleep(60)
        # for user in Friends:
            # print(user.screen_name)
            Time=0
            # graph.nodes[user.id]['checked']=1
            UserExtractor.insertUser(extractor,user,graph)
            context.set("Twitter_User_ID",user)
            graph.add_edge(freshUser.id,user.id,other= "friend")
        print ("\t\tNumber Of nodes collected so far followers: ", graph.number_of_nodes())
        print ("\t\tNumber Of edge collected so far followers: ", graph.number_of_edges())
        # nx.write_gexf(G, "Graph.gexf") 
        # json_graph.nodes_link_data(G)
        print ("\tNumber Of nodes collected so far ", graph.number_of_nodes())
        print ("\tNumber Of edges collected so far", graph.number_of_edges())

    @staticmethod
    def scrapFollowers(freshUser,context,extractor,graph):
        # if freshUser.followers_count<UserExtractor.Limited_number_of_followers:
            # get the followers of the user
        print("followers?")
        followers = []
        for user in tweepy.Cursor(tweepy.API(extractor.getAuth()).get_follower_ids, user_id=freshUser,count=context.get("Follower_Count_Limit")).items():
            # try:
            #     followers.extend(page)
            #     print(followers)
            # except tweepy.TweepError as e:
            #     print("Going to sleep:", e)
            #     time.sleep(60)
        # for user in followers:
            UserExtractor.insertUser(extractor,str(user),graph)
            context.set("Twitter_User_ID",str(user))
            print("GRAPHING?")
            graph.add_edge(str(user),freshUser,other= "follows")
            print ("\t\tNumber Of nodes collected so far followers:", graph.number_of_nodes())
            print ("\t\tNumber Of edges collected so far followers:", graph.number_of_edges())


