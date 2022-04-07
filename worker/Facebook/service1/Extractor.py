
# COPYRIGHT 2022 LAMRI Ali, ZAIDI Omar

from asyncio.windows_events import NULL
#from API_ExtractionService.Network_Extractor import Network_Extractor, NetworkExtractor
import json
from API_ExtractionService.Network_Extractor import NetworkExtractor
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
    #NetworkExtractor
    
    context=None
    Schema=[]
    graphe=NULL
    cookies=''
    def __init__(self,zos_context,Schema,publisher,roadmap):#,publisher,roadmap
        # print("Extractors")

        self.super().__init__("Facebook",zos_context,Schema,publisher,roadmap)
        
        Schema=Schema
        account=zos_context.get("FB_ACCOUNT")
        self.cookies= zos_context.get("FB_COOKIE")
        creds={'email':zos_context.get("FB_EMAIL"),'password': zos_context.get("FB_PASSWORD")}
        post=zos_context.get("POST")
        limit_post=zos_context.get("LIMIT_POSTS")
        limit_friends=zos_context.get("LIMIT_FRIENDS")
        max=zos_context.get("MAX_PARS")
        # file_graphe="fb_graphe"
        
        self.context=Context(account,creds,limit_post,limit_friends,max,post,False,True)

        # this was painful to adapt..
        self.Schema=Schema
        try:
            cookies=list(zos_context.get("FB_COOKIE"))
            self.create_Graphe_friends()
        except Exception as ex:
            print(ex)

    
    def save_json(self,filename,graph):
       try:
            g = graph
            g_json = json_graph.node_link_data(g)
            json.dump(g_json,open(filename,'w'),indent=2)
       except Exception as ex:
           print(ex)

    def get_graph(self):
        return self.graphe

    def set_graph(self,g):
        self.graphe=g

    
    @NetworkExtractor.data_publisher
    def create_Graphe_friends(self):
        Schema=self.Schema
        context=self.context
        cookies=self.cookies
        count_parsed=0
        email= context.keys["email"]
        password=context.keys["password"]
        
        account=context.account
       

        Graphe=nx.DiGraph()
    
        key=0
         
        Graphe.add_nodes_from([(account, {'id':"",
                                            
                                        'checked' :0 ,
                                            
      
                                            } )])
        try:
            profile=get_profile(account)
        except Exception as ex:
            print(str(ex))
           # profile=get_profile(account,cookies=cookies)

        

       # key=(key+1)%len(cookies)
        #profile=get_profile("100009975842374",cookies="ali.txt")
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
                   
                   if  Graphe.nodes[v]['checked']==0:
                         
                        Graphe.nodes[v]['checked']=1
                                
                                #récupérer friends 
                                  
                        limit_friend=context.limit_friends
                        list_friends=get_friends_user(email,password,v,limit_friend) 
                        print(len(list_friends))
                        
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
                   
                   if count_parsed>=int(context.max_pars):
                        print("Extraction complete...........*")
                        
                        self.set_graph(Graphe)
                        self.graph=self.get_graph()
                        # self.save_json("file_graphe.json",final_graph)
                        # json=json_graph.node_link_data(self.graphe)
                         
        
                      # delivering payload
                      # locator.getPublisher().publish("Twitter",json.dumps(payload))
                    
                   print("sleep")
                   time.sleep(3)
                  
                   Nodeslist= [v for v in Graphe.nodes()]


               
                
                
            
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




                    
            
            
                                
        
       

    
