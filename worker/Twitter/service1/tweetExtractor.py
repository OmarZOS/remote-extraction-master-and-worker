



import networkx
from networkx.classes import graph
import tweepy


class TweetExtractor:
    fullStructure = None

    @staticmethod
    def crawlTweet(api,graph,fullSchema,userQueue,coordinatesQueue,placeQueue,urlQueue,mediaQueue,tweetQueue):
        
        TweetExtractor.fullStructure = fullSchema
        
        while True:
            
            try:

                freshTweet = tweetQueue.get()
                # print("another tweet",freshTweet.id)
                # print(freshTweet)
                TweetExtractor.insertTweet(freshTweet,graph)
                
                # entities = freshTweet["entities"]
                
                # TODO : 
                # hashtags_list = []
                # for hashtag in entities["hashtags"] :
                #     placeQueue.put(hashtag["text"])
                
                # TODO : 
                # urls_list = []
                # for url in entities["urls"]:
                #     urlQueue.put(url)
                
                # TODO : 
                # media_list = {}
                # if 'media' in entities :
                #     for media in entities["media"]:
                #         mediaQueue.put(media)
                
                # TODO :             
                # user_mentions_list = []
                # for user_mention in entities["user_mentions"]:
                #     user_mentions_list.append(user_mention["screen_name"])
                # self.user_mentions = user_mentions_list

                # TODO :             
                # coordinates_list = []
                # for coordinate in entities["coordinates"]:
                #     coordinatesQueue.put(coordinate)
                

            except tweepy.TweepyException as ex:
                print("\033[93m An exception has occured in the tweet thread \030[90m")
                print(ex.with_traceback)
                while not tweetQueue.empty():
                    tweetQueue.task_done()
                    print("resident tweet inserted..")
                    # TweetExtractor.insertTweet(tweetQueue.get())
                    tweetQueue.get()


            tweetQueue.task_done()




    @staticmethod
    def insertTweet(tweet:tweepy.User,graph: networkx.DiGraph): # verifies existence inside
        attributes = {}
        if(tweet.id in graph): #nothing to do here
            return 
        # print(TweetExtractor.fullStructure["tweet"])
        # print("\033[93m inserting tweet")
        for attribute in TweetExtractor.fullStructure["tweet"]:
            attributes[attribute+""] = str(getattr(tweet,attribute))
        # print("inserted",attributes)
        if(len(attributes.items()) > 2) :
            graph.add_nodes_from([(tweet.id,[k for k in attributes.items()])],color="green")

        
        
