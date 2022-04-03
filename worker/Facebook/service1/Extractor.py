
# COPYRIGHT 2022 LAMRI Ali, ZAIDI Omar

from asyncio.windows_events import NULL
from API_ExtractionService.Network_Extractor import Network_Extractor, NetworkExtractor
import json
from facebook_scraper import get_posts,get_friends,get_profile
from facebook_scraper import get_group_info
import pandas as pd
from context  import Context
import time
import os
import networkx as nx
from Add_data import Add_friends,Add_posts 
from get_data import get_driver,get_friends_user,get_id,get_user_name_password
from networkx.readwrite import json_graph

class Extractor(NetworkExtractor):
    
    context=None
    Schema=[]
    graphe=NULL
    def __init__(self,zos_context,Schema,publisher,roadmap):
        # print("Extractors")
        zos_context.get("FB_USERS")
        Schema={'user':['id','Name','Friend_count','Follower_count','About'],'post':['post_id','post_text','comments','user_id','reaction_count','page_id','fetched_time']}
        account='100012000482675'
        cookie=['s.txt']
        creds={'email':email,'password':password}
        post=True
        limit_post=1
        limit_friends=3
        max=1
        # file_graphe="fb_graphe"
        
        cxt=Context(account,creds,limit_post,limit_friends,max,post,False,True)

        context=cxt

        # this was painful to adapt..
        self.super().__init__("Facebook",context,Schema,publisher,roadmap)
        self.Schema=Schema
        try:
            cookies=list(context.get("Fb_cookies")   )
        except Exception as ex:
            print(ex)

    
    def save_json(self,filename,graph):
        g = graph
        g_json = json_graph.node_link_data(g)
        json.dump(g_json,open(filename,'w'),indent=2)

    def get_graph(self):
        return self.graphe

    def set_graph(self,g):
        self.graphe=g

    
    @NetworkExtractor.data_publisher
    def create_Graphe_friends(self,context,Schema,cookies):
        
        count_parsed=0
        email= context.keys["email"]
        password=context.keys["password"]
        
        account=context.account
        print(password)

        Graphe=nx.DiGraph()
    
        key=0
         
        Graphe.add_nodes_from([(account, {'id':"",
                                            
                                        'checked' :0 ,
                                            
      
                                            } )])
        try:
            profile=get_profile(account)
        except Exception as ex:
            print(str(ex))
            profile=get_profile(account,cookies=cookies)

        

        key=(key+1)%len(cookies)
         
        for attr in Schema['user']:
            if attr in profile.keys():             
              nx.set_node_attributes(Graphe, name=attr, values=str(profile[attr]))

        if context.user:

            print("user scraping")
            try:
                nx.set_node_attributes(Graphe, name='type', values='user')
                         
                Nodeslist = [v for v in Graphe.nodes()]

                i = 0
                while (i < len(Nodeslist)):
                   
                   v = Nodeslist[i]
                   i += 1
                   
                   if  Graphe.nodes[v]['checked']==0 :
                         
                        Graphe.nodes[v]['checked']=1
                                
                                #récupérer friends 
                                  
                        limit_friend=context.limit_friends
                        list_friends=get_friends_user(email,password,v,limit_friend) 
                        
                        #Add friends
                        try:
                            
                             Add_friends(Graphe,list_friends,limit_friend,Schema['user'],v,cookies)
                        except Exception as ex:
                            print(ex)
                         

                        # Add Post
                        if context.post==True:
                             

                            limit_posts=context.limit_posts
                            try:
                                Add_posts(email,password,account,Schema,Graphe,limit_posts, cookies)
                                time.sleep(2)
                            except Exception as ex:
                                print(ex)

                   count_parsed=count_parsed+1
                   
                   if count_parsed==context.max_pars:
                        print("Extraction complete...........*")
                        
                        self.set_graph(Graphe)
                        final_graph=self.get_graph()
                        #self.save_json(file_graphe+".json",final_graph)
                        json=json_graph.node_link_data(self.graphe)
                         
                       # print(json)
                        payload = json
                        payload["road_map"] = []
                        break
        
                      # delivering payload
                      # locator.getPublisher().publish("Twitter",json.dumps(payload))
                    
                
                   time.sleep(3)
                self.set_graph(Graphe)
                final_graph=self.get_graph()
                self.graph = self.graphe
                # json=json_graph.node_link_data(self.graph)
                         
                # print(json)
                # payload = json
                # payload["road_map"] = []
                
                                     

            except Exception as ex:
                print("ops")
                print(ex)     

    @NetworkExtractor.data_publisher
    def create_Graphe_group(self,context,Schema,cookies):
        count_parsed=0
        email=context. keys['email']
        password=context. keys=['password']
        account=context.account

        Graphe=nx.DiGraph()
    
        key=0
         
        Graphe.add_nodes_from([(account, {'id':account,
                                            
                                        'checked' :0 ,
                                        'type':'group'

                                            
                                        } )])
        
        if context.group:

            print("group scraping")
            try:
                nx.set_node_attributes(Graphe, name='type', values='group')
                         
                Nodeslist = [v for v in Graphe.nodes()]

                i = 0
                while (i < len(Nodeslist)):
                   
                   v = Nodeslist[i]
                   i += 1
                   if  Graphe.nodes[v]['checked']==0 :
                         
                        Graphe.nodes[v]['checked']=1
                                
                      

                        # Add Post
                        if context.post==True:
                            limit_posts=context.limit_posts
                            Add_posts(email,password,account,Schema,Graphe, limit_posts, cookies)
                            time.sleep(2)
                    # val max==1
                   count_parsed=count_parsed+1
                   if count_parsed==1:
                         
                        self.set_graph(Graphe)
                        final_graph=self.get_graph()
                        #self.save_json(file_graphe+".json",final_graph)
                        json=json_graph.node_link_data(self.graphe)
                                
                        payload = json
                        payload["road_map"] = []
                        break
                      
                      # delivering payload
                      # locator.getPublisher().publish("Twitter",json.dumps(payload))

            except Exception as ex:
                print(ex)     




                    
            
            
                                
        
       

    
