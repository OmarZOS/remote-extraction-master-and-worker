import os

CONTEXT_HOST = (os.getenv("CONTEXT_RPC_HOST"))
CONTEXT_PORT = int(os.getenv("CONTEXT_RPC_PORT"))
CONTEXT_SCHEME =  os.getenv("CONTEXT_RPC_SCHEME")

SERVING_HOST = (os.getenv("PROXY_HOST"))
SERVING_PORT = int(os.getenv("PROXY_PORT"))

# DO NOT MODIFY HERE, GOTO varnames.env in the root of the project directory
TWITTER_TOKEN_IDENTIFIER = str(os.getenv("TWITTER_TOKEN_IDENTIFIER"))
TWITTER_TOKEN_FIELDS=str(os.getenv("TWITTER_TOKEN_FIELDS")).split(",")

TWEET_CONSUM_VARNAME=str(os.getenv("TWEET_CONSUM_VARNAME"))
TWEET_SECRET_VARNAME=str(os.getenv("TWEET_SECRET_VARNAME"))
TWEET_KEY_VARNAME=str(os.getenv("TWEET_KEY_VARNAME"))
TWEET_ACCESS_SECRET_VARNAME=str(os.getenv("TWEET_ACCESS_SECRET_VARNAME"))

TWITTER_GLOBAL_VARIABLES=str(os.getenv("TWITTER_GLOBAL_VARIABLES")).split(",")

FACEBOOK_TOKENS_IDENTIFIER = str(os.getenv("FACEBOOK_TOKENS_IDENTIFIER"))
FACEBOOK_TOKEN_FIELDS = str(os.getenv("FACEBOOK_TOKEN_FIELDS")).split(",")
FB_EMAIL_VARNAME=str(os.getenv("FB_EMAIL_VARNAME"))
FB_PASSWORD_VARNAME=str(os.getenv("FB_PASSWORD_VARNAME"))
FB_COOKIE_VARNAME=str(os.getenv("FB_COOKIE_VARNAME"))

FACEBOOK_GLOBAL_VARIABLES=str(os.getenv("FACEBOOK_GLOBAL_VARIABLES")).split(",")

LINKEDIN_TOKENS_IDENTIFIER=str(os.getenv("LINKEDIN_TOKENS_IDENTIFIER"))
LINKEDIN_EMAIL_VARNAME=str(os.getenv("LINKEDIN_EMAIL_VARNAME"))
LINKEDIN_PASSWORD_VARNAME=str(os.getenv("LINKEDIN_PASSWORD_VARNAME"))

LINKEDIN_TOKEN_FIELDS=str(os.getenv("LINKEDIN_TOKEN_FIELDS")).split(",")
LINKEDIN_GLOBAL_VARIABLES=str(os.getenv("LINKEDIN_GLOBAL_VARIABLES")).split(",")
