import praw
import json

reddit = praw.Reddit(client_id = 'DnpX9tZO75idVbdUuDUgdg', 
                    client_secret = '8-8kRY17k-I0KsHRh7ey-ZCQjks8vA',
                    username = 'iammedesu',
                    password = 'FathanReddit123-',
                    user_agent= 'tugasakhirv1')

subreddit = reddit.subreddit('python')

hot_scrape = subreddit.hot(limit=5)

for submission in hot_scrape:
    print(submission)