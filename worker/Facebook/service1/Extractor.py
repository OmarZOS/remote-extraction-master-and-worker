
from asyncio.windows_events import NULL
import json
from click import option
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


class Extractor:
 
 
    file_graphe=''
    context=None
    Schema=[]
    graphe=NULL
    def __init__(self,file_graphe,context,Schema,cookies):
        print("Extractors")
         
      
        self.file_graphe=file_graphe
        self.context=context
        self.Schema=Schema

    
    def save_json(self,filename,graph):
        g = graph
        g_json = json_graph.node_link_data(g)
        json.dump(g_json,open(filename,'w'),indent=2)

    def get_graph(self):
        return self.graphe
    
    def set_graph(self,g):
        self.graphe=g

        
     
    def create_Graphe_friends(self,file_graphe,context,Schema,cookies):
       

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
        profile=get_profile(account,cookies=cookies[key])
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
                   #print(len(Nodeslist))
                   #print(Nodeslist[i])
                   v = Nodeslist[i]
                   i += 1
                   print(i)
                   print(v)
                   if  Graphe.nodes[v]['checked']==0 :
                         
                        Graphe.nodes[v]['checked']=1
                                
                                #récupérer friends 
                                  
                        limit_friend=context.limit_friends
                        list_friends=get_friends_user(email,password,v,limit_friend) 
                        #print(len(list_friends))
                        #print(list_friends)
                                
                        #Add friends
                            
                        Add_friends(Graphe,file_graphe,list_friends,limit_friend,Schema['user'],v,cookies)
                         

                        # Add Post
                        if context.post==True:
                             

                            limit_posts=context.limit_posts
                            Add_posts(email,password,account,Schema,Graphe,file_graphe,limit_posts, cookies)
                            time.sleep(2)

                   print('change nodelist')
                   count_parsed=count_parsed+1
                   Nodeslist = [v for v in Graphe.nodes()]
                   print( context.max_pars)
                   print(len(Nodeslist))
                   print(context.post)
                   print(count_parsed)
                   if count_parsed==context.max_pars:
                        print("Extraction complete...........*")
                        # Get Graph
                        # self.graphe=
                        self.set_graph(Graphe)
                        final_graph=self.get_graph()
                        self.save_json(file_graphe+".json",final_graph)
                        json=json_graph.node_link_data(self.graphe)
                         
                            
                         
                        print("dateeien")
                        print(json)
                        payload = json
                        payload["road_map"] = []
                        break
                        
        
                      # delivering payload
                      # locator.getPublisher().publish("Twitter",json.dumps(payload))
                   print("Sleeeeeeeeeep---*--*-*-*-*-*-*--*--*")
                    
                
                   time.sleep(3)
                print("alialaiai")
                self.set_graph(Graphe)
                final_graph=self.get_graph()
                self.save_json(file_graphe+".json",final_graph)
                loaded_json = json.loads(file_graphe+".json")
                #dateien = json_graph(Graphe)
                print("dateeien")
                print(loaded_json)
                payload = loaded_json
                payload["road_map"] = []
                                     
                        # delivering payload
                        # locator.getPublisher().publish("Twitter",json.dumps(payload)

            except Exception as ex:
                print("ops")
                print(ex)     


    def create_Graphe_group(self,file_graphe,context,Schema,cookies):
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
        """profile_group=get_group_info(account,cookies=cookies[key])
        key=(key+1)%len(cookies)
            
            
        print(key)
        for attr in Schema['group']:
            if attr in profile_group.keys():
             
              nx.set_node_attributes(Graphe, name=attr, values=str(profile_group[attr]))
           """
        if context.group:

            print("group scraping")
            try:
                nx.set_node_attributes(Graphe, name='type', values='group')
                         
                Nodeslist = [v for v in Graphe.nodes()]

                i = 0
                while (i < len(Nodeslist)):
                   print(len(Nodeslist))
                   print(Nodeslist[i])
                   v = Nodeslist[i]
                   i += 1
                   if  Graphe.nodes[v]['checked']==0 :
                         
                        Graphe.nodes[v]['checked']=1
                                
                      

                        # Add Post
                        if context.post==True:
                            limit_posts=context.limit_posts
                            Add_posts(email,password,account,Schema,Graphe,file_graphe,limit_posts, cookies)
                            time.sleep(2)

                   print('change nodlist')
                   count_parsed=count_parsed+1
                   Nodeslist = [v for v in Graphe.nodes()]
                   print(len(Nodeslist))
                   if count_parsed==context.max_pars:
                       print("end of extraction")
                       self.save_json(file_graphe,self.graph)
        
                       payload = json.loads(json_graph.dumps(self.graph))
                       payload["road_map"] = []
        
                      # delivering payload
                      # locator.getPublisher().publish("Twitter",json.dumps(payload))

            except Exception as ex:
                print(ex)     




                    
            
            
                                
        
       

    
