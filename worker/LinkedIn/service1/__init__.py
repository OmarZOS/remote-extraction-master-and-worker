from Extractor import Extractor
from context import Context
import  networkx as nx
from bot_studio import *

keys={'username':'','password':''}
account="https://www.linkedin.com/company/ouedkniss/"
val=20

G=nx.DiGraph()
user_comment=True
add_user=True
add_comm=True
context1=Context(account,keys,val,val,val,user_comment,add_user,add_comm,True)
schema={'page':['name','localisation','description','abonnee'],'post':["Date_Posted","Media_Type" , "Post_Text" ,"Post_Likes" ,"Post_Comments" , "Media_Links"],'user':["Info","Education","Current Company","About"]}

linkedin=bot_studio.linkedin()    
linkedin.login(context1.keys['username'] , context1.keys['password'] )


 
ex=Extractor(linkedin,G,"first_graphe",context1,schema)
ex.create_graphe(linkedin,G,"first_graphe",context1,schema)