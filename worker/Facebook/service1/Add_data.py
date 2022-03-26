from http import cookies
import json
from click import option
from facebook_scraper import get_posts,get_friends,get_profile
from facebook_scraper import get_group_info
import pandas as pd
from context  import Context
import time
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import os
import networkx as nx 
from get_data import get_driver,get_friends_user,get_id,get_user_name_password


def check_value1(post):

    try:

        content=post.find("div",{"class":"kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql"})
       
        return content

    except:
        return "error"


def check_value2(post):
    try:
        time.sleep(2)
        content2=post.find("div",{"class":"cxmmr5t8 oygrvhab hcukyx3x c1et5uql o9v6fnle ii04i59q"})
        
        return content2

    except:
        return "error"



 

def Add_friends(Graphe,file_graphe,list_friends,limit_friend,Schema,v,cookies):
     i=0
     
     for friend in list_friends:
         try:
             if i<limit_friend:
                    
                #print(friend)
                if str( friend) not in Graphe:
                    #print("friend")
                    Add_user(Graphe,file_graphe, Schema,friend,v, cookies )
                    #key=(key+1)%len(cookies)
                else:
                     Graphe.add_edge(v,str(friend),link_type="friend")
                    
                     nx.write_gexf(Graphe, file_graphe+".gexf") 


             time.sleep(2)
    
         except Exception as ex:
              print(ex)
              key=(key+1)%len(cookies)
              print(key-1)
              print("error add user key")
             

      


"""def Add_posts(Graphe,list_posts,limit_posts,Schema,v,cookies):
    key=0
    i=0
    for post in list_posts:
         if i< limit_posts:


             print("add post")
                                
             #Appel add post
             Add_post(Graphe, Schema['post'],post,v)
                
             if str( post["user_id"])not in Graphe:
                 try:
                     print("add user of comment")
                     Add_user(Graphe, Schema['user'],post["user_id"],v,cookies[key])
                     key=(key+1)%len(cookies)
                     time.sleep(20)
                 except Exception as ex:
                     print(ex)
                     key=(key+1)%len(cookies)

"""



def Add_posts(email,passd,account,schema,graphe,file_graphe,nb_post,cookies):
    print("scrapping post")
    list_post={}
    
    driver1=get_driver ()
    driver1.get("https://www.facebook.com")
    try:
        #login
        username_el=driver1.find_element(By.ID, "email")
        password=driver1.find_element(By.ID, "pass")
        sub=driver1.find_element(By.NAME,'login')
        username_el.send_keys( email)

        password.send_keys(passd)  
 
        print(driver1.title)
        sub.click()
        length=0
        time.sleep(3)


        driver1.get("https://www.facebook.com/"+account)
        time.sleep(4)
         
         
        
        content_list=[]
        content_list2=[]
        time_list=[]
        name_list=[]
        while True:
            time.sleep(3)

            print("ok while")
            
            soup=BeautifulSoup(driver1.page_source,"html.parser")
            all_post=soup.find_all("div",{"class":"du4w35lb k4urcfbm l9j0dhe7 sjgh65i0"})
            time.sleep(3)

         
            
            print(len(all_post))
            for post in all_post:
                time.sleep(3)
                try:
                    publisher_a=post.find("a",{"class":"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p"})
              
                    
                    h=publisher_a.get('href').split("/")
                    publisher=account
                    if 'groups'in h:

                        
                        publisher=h[4]
                    if publisher not in graphe:
                        #print('notnotnot')
                        Add_user(graphe,schema['user'],publisher,account,cookies)
                    else:
                        print("exist")
                        
                except:
                        print('no publisher')
               
                
               
                 
                data={}
            
                try:
                    name=post.find("a",{"class":"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gpro0wi8 oo9gr5id lrazzd5p"})
                      
                    name_list.append(name.text) 
                    data["name"]=name.text

                except :
                    name="name not found "
                    data["name"]=''
                    print(name)
                try:
                    if check_value1(post)!='error':
                         # content=post.find("div",{"class":"kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql ii04i59q"})
                         content= check_value1(post)
                         if content=="error":
                             content_list.append('')
                         else:
                             
                            content1=content.find ("div",{"style":"text-align: start;"})
                            content_list.append(content1.text)
                            print("content1")
                            data["content1"]=content1.text
                except:
                    content_list.append("")
                    data["content1"]=''

                try:

                    if check_value2(post)!='error':
                        time.sleep(2)

                        #content2=post.find("div",{"class":"cxmmr5t8 oygrvhab hcukyx3x c1et5uql o9v6fnle ii04i59q"})
                        content2=check_value2(post)
                        content3= content2.find ("div",{"style":"text-align: start;"})
                        content_list2.append(content3.text)
                        print("content3")
                        data["content2"]=content3.text
               
                except Exception as ex:
                    print(ex) 
                    content_list2.append("")
                    data["content2"]=''

                
                try:
                    print("kayen time ")
                    

                    time1=post.find("a",{"class":"oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8 b1v8xokw"})
                    time.sleep(3)
                    time_list.append(time1.text)
                    data["time"]= time1.text
                except Exception as ex:
                    print(ex) 
                    print("time not found")
                
                try:
                      Likes=post.find("span",{"class":"pcp91wgn"})
                      data['reactions']=Likes.text
                      comment_nbre=post.find("span",{"class":"d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain"})
                      data['comment_count']=comment_nbre.text
                except Exception as ex:
                    print(ex)
                    data['reactions']=''
                    data['comment_count']=''
                

               
                 
                
                # add to graphe
                data['type']='post'
                data['checked']=2
                
                length=length+1
                graphe.add_nodes_from([( str(length)+account,  data )])
                
                
                if account!=publisher:

                    graphe.add_edge(publisher,str(length)+account, link_type="publisher")
                    graphe.add_edge(account,publisher , link_type="member")
                    
                else:
                    print("!=!=!=!=")
                    graphe.add_edge(account,str(length)+account, link_type="publisher")


                nx.write_gexf(graphe, file_graphe+".gexf") 
 
               
                if length>nb_post:
                     
                    break
            
            print(length)
           
            if length>nb_post:
                
                break

            #scroll  
            y=500
             
            for i in range(0,25):
                driver1.execute_script("window.scrollTo(0, "+str(y)+")")
                y=y+500
        
            
       
        print("end add posts")
        return list_post
        driver1.close()




    except Exception as ex :
        print(ex)
        print("error")
        return list_post
        driver1.close()


    

            
def Add_user(Graphe,file_graphe,context,id,v,cookies) :

    key=0
    
    
    data = {}
    try:
         
        profile_friend=get_profile(str(id) )
        time.sleep(2)
        #print(profile_friend)
                    
        
        data['checked']=0
        data['type']='user'
        try:
                
            for c in context:
                data[c] = str(profile_friend[c])
        except:
            print(data)
            Graphe.add_nodes_from([(id,data)])
        
            Graphe.add_edge(v,str(id),link_type="friend")
            nx.write_gexf(Graphe,file_graphe+".gexf") 
            return 1


        
        if id not in Graphe:
            Graphe.add_nodes_from([(id,data)])
            
            Graphe.add_edge(v,str(id),link_type="friend")
                        
            nx.write_gexf(Graphe,file_graphe+".gexf") 
        else:
             Graphe.add_edge(v,str(id),link_type="friend")

    except Exception as ex:
        print(ex)
        return 1


def Add_post(Graphe_post, context,post,v):
     try:
         print("add post")
         data={}
         for c in context:
             data[c] = str(post[c])
         data['type']='post'
         Graphe_post.add_nodes_from([(post["post_id"],  data )])
         Graphe_post.add_edge(v,str(post["user_id"]), link_type="publish")
         nx.write_gexf(Graphe_post, "Graph_friends2.gexf") 
     except Exception as ex:
         print(ex)
         return 1

         



    
 
