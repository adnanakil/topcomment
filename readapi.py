import requests
from PIL import Image
from StringIO import StringIO
import praw
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')


user_agent = ("top comment puller by kulak85")
r = praw.Reddit(user_agent=user_agent)
# WHEN I REFRSH I KILL THE GENERATOR


def story():
	submissions = list(r.get_subreddit('news').get_top(limit=5))
	stories = [str(story.title) for story in submissions]
	top_comment = [x.comments[0].body for x in submissions]
	links = [link.url for link in submissions]
	zipper = zip(stories, top_comment, links)
	return zipper


# x = topcomment()
# print "i'm here!"
# print x[0]




# try:
# 	submission = next(submissions).comments
# 	comments = []
# 	comments = [str(x) for x in submission]
# 	print comments[0]	
# except:
# 	print "excepted!"

# for value in submissions:
#      top_comment = value.comments[0]
#      print top_comment

# >Anyone who has ever been to jail before knows this idea that they try to get
# >**Objective-Truth**: While a state senator, Senator Shitbag did not vote yes

# top_comment = [value.comments for value in submissions]