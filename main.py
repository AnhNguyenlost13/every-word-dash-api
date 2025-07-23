import asyncio
import re
from twikit.guest import GuestClient
from twikit.client import client

async def get_latest(username: str):
    gclient = GuestClient()
    
    realclient = client.Client()
    realclient.load_cookies("badeline.json")
    # await realclient.activate()
    
    await gclient.activate()
    user = await gclient.get_user_by_screen_name(username)
    
    tweets = await realclient.get_user_tweets(user.id, 'Tweets', count=1)
    latest = tweets[0]
    if getattr(latest, "pinned", False):
        if len(tweets) > 1:
            latest = tweets[1]
        else:
            more = await tweets.next()
            latest = more[0]

    with open("latest_tweet.txt", "w", encoding="utf-8") as f:
        f.write(re.sub(r"\shttps://t\.co/\w+$", "", latest.text.strip()))

asyncio.run(get_latest("everyworddash"))
