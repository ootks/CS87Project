import praw

# un: 87project; pw: in our hangouts chat

# obtaining a reddit instance (required)
# do not change these values
reddit = praw.Reddit(client_id='FFkqA8RP6rqvbw',
                     client_secret='YR1cPFacvh4zrB5vTQ-v4pCHXDk',
                     user_agent='script:87project:v0 (by /u/87project)')

# assume you have a Reddit instance bound to variable `reddit`
subreddit = reddit.subreddit('wholesome' 'memes')

print(subreddit.display_name)  # Output: wholesomememes
print(subreddit.title)         # Output: Internet for the Spirit
print()

# be ready to decode to ascii to handle unicode (since reddit is OK with
# it, but python is not). 
# use .encode('ascii', 'ignore').decode('utf-8')

# iterate through the top 100 posts of all time
num_posts = 1
for submission in subreddit.top(limit=num_posts):
	s_title = submission.title.encode('ascii', 'ignore').decode('utf-8')
	# default comment sort is 'best'
	top_level_comments = list(submission.comments)
	print(s_title)
	print(top_level_comments)






