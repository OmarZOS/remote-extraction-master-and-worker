





from asyncio.windows_events import NULL
from matplotlib.style import context


class Context:
    account=''
    
    post=False
    keys={}
    limit_posts=0
    limit_friends=0
    limit_comments=0
    user_comment=True
    add_user=True
    add_comm=True
    user_comment=True
    graph=NULL
     
    


    def __init__(self,account,keys,limit_post,limit_friends,limit_comments,user_comment,add_user,add_comm,post ):
        
        self.account=account
        self.keys=keys
        self.limit_posts=limit_post
        self.limit_friends=limit_friends
        self.limit_comments=limit_comments
        self.user_comment=user_comment
        self.add_comm=add_comm
        self.add_user=add_user
        self.post=post
        


    def get_post(self):
         return self.post
    def get_limit_post(self):

        return self.limit_posts