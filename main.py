import asyncio
from twikit.guest import GuestClient
from twikit.client import client

async def get_latest(username: str):
    gclient = GuestClient()
    realclient = client.Client()
    await realclient.load_cookies("badeline.json")

    await gclient.activate()
    user = await gclient.get_user_by_screen_name(username)

    tweets = await realclient.get_user_tweets(user.id, 'Tweets', count=2)
    latest = tweets[0]

    if hasattr(latest, "pinned") and latest.pinned:
        latest = tweets[1] if len(tweets) > 1 else (await tweets.next())[0]

    tweet_url = f"https://twitter.com/{username}/status/{latest.id}"
    output = f"{latest.text} {tweet_url} {latest.created_at}"

    with open("badeline.txt", "w", encoding="utf-8") as f:
        f.write(output)

    print(output)

if __name__ == "__main__":
    asyncio.run(get_latest("everyworddash"))
