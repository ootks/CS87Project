import praw

# un: 87project; pw: in our hangouts chat

# obtaining a reddit instance (required)
# do not change these values
reddit = praw.Reddit(client_id='FFkqA8RP6rqvbw',
                     client_secret='YR1cPFacvh4zrB5vTQ-v4pCHXDk',
                     user_agent='script:87project:v0 (by /u/87project)')

# Output: True
print(reddit.read_only)

for submission in reddit.subreddit('wholesome' 'memes').hot(limit=10):
    print(submission.title)