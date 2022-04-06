
import os

YOUTUBE_SEARCH_URL = "https://www.googleapis.com/youtube/v3/search"
YOUTUBE_COMMENT_URL = "https://www.googleapis.com/youtube/v3/commentThreads"
SAVE_PATH = "output/"
YOUTUBE_TOKEN = str(os.getenv("YOUTUBE_KEY"))

MAXDEMANDS = int(os.getenv("MAXDEMANDS"))
REGIONCODE = str(os.getenv("REGIONCODE"))   # IT: international by default
