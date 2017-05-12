import praw
from praw.models import MoreComments, Submission
import os

num_posts = 100
score_threshold = 10
parent_child_demarcator = '\x0b' # vertical tab
scraped_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'data/scraped')

# un: 87project; pw: in our hangouts chat

def sanitize(text):
    sanitized = text.encode('ascii', 'ignore').decode('utf-8')
    # Since comments are stored one per line, we need to replace newlines with
    # another character: tab character.
    sanitized = sanitized.replace('\n', '\t')
    return sanitized

# obtaining a reddit instance (required)
# do not change these values
reddit = praw.Reddit(client_id='FFkqA8RP6rqvbw',
                     client_secret='YR1cPFacvh4zrB5vTQ-v4pCHXDk',
                     user_agent='script:87project:v0 (by /u/87project)')

# assume you have a Reddit instance bound to variable `reddit`
subreddit = reddit.subreddit('wholesome' 'memes')

print("Scraping:", subreddit.display_name)  # Output: wholesomememes
print(subreddit.title)                      # Output: Internet for the Spirit
print()

# be ready to decode to ascii to handle unicode (since reddit is OK with
# it, but python is not). 
# use .encode('ascii', 'ignore').decode('utf-8')

# iterate through the top 100 posts of all time
post_num = 1
for submission in subreddit.top(limit=num_posts):
    s_title = sanitize(submission.title)
    # default comment sort is 'best'
    print("Scraping submission (%d/%d):" % (post_num, num_posts), s_title)
    submission.comments.replace_more()
    num_comments = 0
    with open(os.path.join(scraped_path, submission.id), 'w') as f:
        for comment in submission.comments.list():
            if isinstance(comment, MoreComments) \
                    or comment.score < score_threshold:
                continue
            line = ''
            parent = comment.parent()
            if isinstance(parent, Submission):
                line += s_title
            else:
                if parent.body == '[deleted]':
                    continue
                line += sanitize(parent.body)
            line += parent_child_demarcator
            line += sanitize(comment.body)
            line += '\n'
            f.write(line)
            num_comments += 1
    print("Done scraping %d comments" % num_comments)
    post_num += 1
