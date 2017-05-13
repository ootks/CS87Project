import praw
from praw.models import MoreComments, Submission
import os

num_posts = 1000
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

if __name__ == '__main__':
    # obtaining a reddit instance (required)
    # do not change these values
    reddit = praw.Reddit(client_id='FFkqA8RP6rqvbw',
                         client_secret='YR1cPFacvh4zrB5vTQ-v4pCHXDk',
                         user_agent='script:87project:v0 (by /u/87project)')

    # assume you have a Reddit instance bound to variable `reddit`
    subreddit = reddit.subreddit('wholesome' 'memes')

    print('Scraping:', subreddit.display_name)  # Output: wholesomememes
    print(subreddit.title)                      # Output: Internet for the Spirit
    print()

    # be ready to decode to ascii to handle unicode (since reddit is OK with
    # it, but python is not). 
    # use .encode('ascii', 'ignore').decode('utf-8')

    # iterate through the top 100 posts of all time
    post_num = 1
    with open(os.path.join(scraped_path, 'top_%d_posts.txt' % num_posts), 'w') as f:
        for submission in subreddit.top(limit=num_posts):
            s_title = sanitize(submission.title)
            # default comment sort is 'best'
            print('Scraping submission %d/%d, score %d:' % \
                (post_num, num_posts, submission.score), s_title)
            submission.comments.replace_more(limit=None)
            num_comments = 0
            for comment in submission.comments.list():
                if isinstance(comment, MoreComments) \
                        or comment.score < score_threshold \
                        or comment.body == '[deleted]' \
                        or comment.body == '[removed]':
                    continue
                line = ''
                parent = comment.parent()
                if isinstance(parent, Submission):
                    line += s_title
                else:
                    if parent.body == '[deleted]' or parent.body == '[removed]':
                        continue
                    line += sanitize(parent.body)
                line += parent_child_demarcator
                line += sanitize(comment.body)
                line += '\n'
                f.write(line)
                num_comments += 1
            print('Done scraping %d comments' % num_comments)
            post_num += 1
