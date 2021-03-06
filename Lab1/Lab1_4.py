import praw
import datetime as dt

reddit = praw.Reddit(client_id=[],
                     client_secret=[],
                     user_agent=[],
                     )

for submission in reddit.front.hot(limit=10):
    print(f"Title: {submission.title} \nTime created: {dt.datetime.fromtimestamp(submission.created)}\nBelongs to "
          f"subreddit: {submission.subreddit} \nUpvotes: {submission.score}\n")

