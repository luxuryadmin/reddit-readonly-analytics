import praw
import os

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent="readonly-analytics-demo"
)

def fetch_posts(subreddit, limit=10):
    posts = []
    for post in reddit.subreddit(subreddit).new(limit=limit):
        posts.append({
            "id": post.id,
            "created_utc": post.created_utc,
            "subreddit": subreddit,
            "title": post.title
        })
    return posts
