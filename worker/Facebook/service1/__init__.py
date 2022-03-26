from http import cookies
from Extractor import Extractor
from context import Context
import  networkx as nx
 
from facebook_scraper import get_posts,get_friends,get_profile,get_group_info



 
cookie=['s.txt']
Schema={'user':['id','Name','Friend_count','Follower_count','About'],'post':['post_id','post_text','comments','user_id','reaction_count','page_id','fetched_time']}
account='100012000482675'
email="alilamri350@gmail.com"
password="aliali19980*"
keys={'email':email,'password':password}
post=True
limit_post=1
limit_friends=3
file_graphe="fb_graphe"
max=1
cxt=Context(account,keys,limit_post,limit_friends,max,post,False,True)
#print(get_profile("100009975842374"))
#print(get_group_info("journalmaracanaalgerie") )

ex =Extractor('Fb',cxt,Schema,cookie)
ex.create_Graphe_friends(file_graphe,cxt,Schema,cookie)
#ex.create_Graphe_group(file_graphe,cxt,Schema,cookies)
