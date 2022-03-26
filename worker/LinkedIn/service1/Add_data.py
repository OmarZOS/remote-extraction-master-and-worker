

import time 
import networkx as nx 
from context import Context
from get_data import get_comment_data ,get_post_page,get_post_url,get_user_comment_data


def Add_Posts_nodes(Graphe,context_obj,schema,list_url,page):
    print("Add Posts")
     
    username=context_obj.keys['username']
    password=context_obj.keys=['password']
     
    limit_posts=context_obj.limit_posts
    
    
    posts_data=get_post_page(username,password,page)
    
    
    print("get full posts data")
    
    time.sleep(3)
    indice=0
    for i in range(0,len(list_url)):
        
        try:
            data={}
            #create post node
            if list_url[i] in Graphe:
                print("continue")
                continue
            for sc in schema['post']:
      
                data[sc]=posts_data[sc][i]
                
            if indice > limit_posts:
               context_obj.graph=Graphe
               break
               
                
            data['checked']=2
            data['type']='post'
            
            Graphe.add_nodes_from([(list_url[i],data)])
            Graphe.add_edge(page,str(list_url[i]), link_type="published_in")
            
            context_obj.graph=Graphe 
        except Exception as ex:
            print(ex)
            context_obj.graph=Graphe
            
        
        



def Add_comment_user(linkedin,Graphe,context,username , password ,list_url,limit_comment,schema,add_user,add_comm):
    
    x=0
    for url in list_url:
        x=x+1
        more=True
        
        post=linkedin.get_post(post_link=url)
        time.sleep(5)
        time_post=post['body']['Time']
        
        comments= linkedin.get_comments()
        time.sleep(5)
       
        
        linkedin.click_load_more()
        time.sleep(3)
        comments= linkedin.get_comments()
        time.sleep(3)
         
       
        if comments['body']=={}:
            
            print("continue")
            continue
        
         
         
        for i in range(0,len(comments['body'])):
            if i%2==1:
                print("i%2==1")
                continue
            

            com=comments['body'][i]
            data_com=get_comment_data(com)
            user_com=comments['body'][i]
          
            data_user_com=get_user_comment_data(linkedin,user_com,schema)
            
            Graphe.add_nodes_from([(url+str(i),data_com)])

            if user_com['User Link'] not in Graphe:

                Graphe.add_nodes_from([(user_com['User Link'],data_user_com)])
             
             

            Graphe.add_edge(url+str(i),user_com['User Link'], link_type="comment_with")

        
            Graphe.add_edge(url ,user_com['User Link'], link_type="comment")
            context.graph=Graphe
 
 
    