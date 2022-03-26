





class Context:
    account=''
    post=False
    keys={}
    limit_posts=0
    limit_friends=0
    limit_comments=0
    group=False
    user=False
    max_pars=0
    
    


    def __init__(self,account,keys,limit_post,limit_friends,max_pars,post,group,user):
        
        self.account=account
        self.keys=keys
        self.limit_posts=limit_post
        self.limit_friends=limit_friends
        self.user=user
        self.group=group
        self.max_pars=max_pars
        self.post=post

    def get_post(self):
         return self.post
    def get_limit_post(self):

        return self.limit_posts