

def initialiseTwitterTokens(context,TWITTER_TOKENS_IDENTIFIER):

    import json
    import os

    tweet_consums = str(os.getenv("TWEET_CONSUM")).split(",")
    tweet_secrets = str(os.getenv("TWEET_SECRET")).split(",")
    tweet_keys = str(os.getenv("TWEET_KEY")).split(",")
    tweet_access_secrets = str(os.getenv("TWEET_ACCESS_SECRET")).split(",")

    creds_count = min(  len(tweet_consums),
                        len(tweet_secrets),
                        len(tweet_keys),
                        len(tweet_access_secrets))  
    
    for i in range(creds_count):
        creds = json.dumps({
                "TWEET_CONSUM":tweet_consums[i],
                "TWEET_SECRET":tweet_secrets[i],
                "TWEET_KEY":tweet_keys[i],
                "TWEET_ACCESS_SECRET":tweet_access_secrets[i]
            })
        context.set(TWITTER_TOKENS_IDENTIFIER,creds)

def choose_service(context,model,available_services): #------- TODO ----------------
    pass
    

