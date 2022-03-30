from http import cookies
from Extractor import Extractor
from context import Context
import  networkx as nx
 
from facebook_scraper import get_posts,get_friends,get_profile,get_group_info



 











cxt=Context(account,creds,limit_post,limit_friends,max,post,False,True)
#print(get_profile("100009975842374"))
#print(get_group_info("journalmaracanaalgerie") )

ex =Extractor('Fb',cxt,Schema,cookie)
ex.create_Graphe_friends(file_graphe,cxt,Schema,cookie)
#ex.create_Graphe_group(file_graphe,cxt,Schema,cookies)
