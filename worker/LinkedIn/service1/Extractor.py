

from asyncio.windows_events import NULL
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
from bot_studio import *
import re as re
from selenium.webdriver.common.by import By 
import win32clipboard
import os
from bs4 import BeautifulSoup as bs
from connect import connect
from context import Context
import networkx as nx 
from get_data import get_post_url
from Add_data import Add_comment_user,Add_Posts_nodes
import json
from networkx.readwrite import json_graph
from API_ExtractionService.Network_Extractor import Network_Extractor



class Extractor(NetworkExtractor):
    linkedin=None
    Graphe=None
    
    context=None
    Schema=[]
    context= None
    graphe=NULL

   

    def __init__(self,linkedin,context,Schema,publisher,roadmap,Graphe):
        print("Extractors")
        self.super().__init__("LinkedIn",context,Schema,publisher,roadmap)
        self.linkedin=linkedin
        self.Graphe=Graphe

        self.context=context
        self.Schema=Schema
        self.context=context
    def get_graph(self):
        return self.graphe
    
    def set_graph(self,g):
        self.graphe=g

    
    def save_json(self,filename,graph):
        g = graph
        g_json = json_graph.node_link_data(g)
        json.dump(g_json,open(filename,'w'),indent=2)


        
    def Scraper_page(self,username,password,page_url):
            driver=connect().connection(username,password)
             

            data={}
        
            
            driver.get(page_url) 
            time.sleep(3)
            src = driver.page_source
            soup = BeautifulSoup(src, 'lxml')
            time.sleep(5)
            
            intro = soup.find('div', {'class': 'block mt2'})
            
            
            name_loc = intro.find("h1")
            data["name"]=name_loc.get_text().strip()
            #print(name_loc.get_text().strip())
            
            
        
            
            works_at_loc = intro.find("div", {'class': 'inline-block'}).find_all('div')
            loc=works_at_loc[0].get_text().strip()
            data['localisation']=loc
            #print(loc)
            abonnee=works_at_loc[1].get_text().strip()
            data['abonnee']=abonnee
            #print(abonnee)
            description= soup.find('div', {'class': 't-14 t-black--light full-width break-words ember-view'})
            data['description']=description.get_text().strip()
        

            
            driver.close()
            
            return data
 


    @NetworkExtractor.data_publisher
    def create_graphe(self,linkedin,Graphe,file_graphe,context,Schema):
        print("-----create graphe--------")
        username=context.keys['username']
       
        password=context.keys['password']
       
        page=context.account
        
        limit_comment= context.limit_comments
        if Graphe.number_of_nodes() ==0:
        
        
            Graphe.add_nodes_from([(page, {'id':page,
                                            
                                            'checked' :0 ,
                                            'type':'page'
                                            
                                            } )])
            
            page_inf=self.Scraper_page(username,password,page)
            
            
        
            for attr in Schema['page']:
                
                nx.set_node_attributes(Graphe, name=attr, values=str(page_inf[attr]))
                    
    
        try:
                
            
            Nodeslist = [v for v in Graphe.nodes()]
            for v in Nodeslist:

                
                 
                if  Graphe.nodes[v]['checked']==0 :
                    
                    Graphe.nodes[v]['checked']=1
                    if  Graphe.nodes[v]['type']=='page':
                       
                        #Add Postprint()
                        limit_posts=context.limit_posts
                        
                        list_url=get_post_url(username,password,context.limit_posts,v)
                        time.sleep(4)
                        if len(list_url)==0:
                            print("no url selected")
                            break
                         
                        Add_Posts_nodes(Graphe,file_graphe,context,Schema,list_url,v)
                         
                        
                        #Add Comment
                        user_comment=context.user_comment
                        if(user_comment==True):
                            add_comm=context.add_comm
                            add_user=context.add_user
                            
                            Add_comment_user(linkedin,Graphe,context,file_graphe,username , password ,list_url,limit_comment,Schema,add_user,add_comm)

                            
                        
                    
                        


                    
                    Nodeslist = [v for v in Graphe.nodes()]
                    

            print("Extraction complete.")
            # Get Graph
           # self.graphe=Graphe
            self.set_graph(context.graph)
            final_graph=self.get_graph()
            self.save_json(file_graphe+".json",final_graph)
            loaded_json = json.loads(file_graphe+".json")
            #dateien = json_graph(Graphe)
            print("dateeien")
            print(loaded_json)
            payload = loaded_json
            payload["road_map"] = []
            # delivering payload
            # locator.getPublisher().publish("Twitter",json.dumps(payload))
        except Exception as ex:
            self.save_json(file_graphe+".json",context.graph)
            print(ex)       

