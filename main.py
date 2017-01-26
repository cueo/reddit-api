import praw
from data import *

reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, password=password, user_agent=user_agent, username=username)

# Print the user
print reddit.user.me()

# Print the list of subscribed subreddits
print list(reddit.user.subreddits())

# Subscribe to a list of subreddits (subs)
for subreddit in subs:
	print 'Subscribing:', subreddit
	try:
		reddit.subreddit(subreddit).subscribe()
	except Exception as e:
		print 'Couldn\'t subscribe to', subreddit
		print 'Reason:', e