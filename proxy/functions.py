

def initialiseTwitterTokens(context,TWITTER_TOKENS_IDENTIFIER):

    import json
    import os

    creds_0 = {"TWEET_CONSUM":str(os.getenv("TWEET_CONSUM")),
                "TWEET_SECRET":str(os.getenv("TWEET_SECRET")),
                "TWEET_KEY":str(os.getenv("TWEET_KEY")),
                "TWEET_ACCESS_SECRET":str(os.getenv("TWEET_ACCESS_SECRET"))}
                

    creds_1 = {"TWEET_CONSUM":str(os.getenv("TWEET_CONSUM1")),
                "TWEET_SECRET":str(os.getenv("TWEET_SECRET1")),
                "TWEET_KEY":str(os.getenv("TWEET_KEY1")),
                "TWEET_ACCESS_SECRET":str(os.getenv("TWEET_ACCESS_SECRET1"))
                }

    creds_2 = {"TWEET_CONSUM":str(os.getenv("TWEET_CONSUM2")),
                "TWEET_SECRET":str(os.getenv("TWEET_SECRET2")),
                "TWEET_KEY":str(os.getenv("TWEET_KEY2")),
                "TWEET_ACCESS_SECRET":str(os.getenv("TWEET_ACCESS_SECRET2"))
                }

    creds_3 = {"TWEET_CONSUM":str(os.getenv("TWEET_CONSUM3")),
                "TWEET_SECRET":str(os.getenv("TWEET_SECRET3")),
                "TWEET_KEY":str(os.getenv("TWEET_KEY3")),
                "TWEET_ACCESS_SECRET":str(os.getenv("TWEET_ACCESS_SECRET3"))
                }

    creds_0 = json.dumps(creds_0)
    creds_1 = json.dumps(creds_1)
    creds_2 = json.dumps(creds_2)
    creds_3 = json.dumps(creds_3)

    context.set(TWITTER_TOKENS_IDENTIFIER,creds_0)
    context.set(TWITTER_TOKENS_IDENTIFIER,creds_1)
    context.set(TWITTER_TOKENS_IDENTIFIER,creds_2)
    context.set(TWITTER_TOKENS_IDENTIFIER,creds_3)
