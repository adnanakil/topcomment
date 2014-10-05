import requests
from StringIO import StringIO
import praw
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')


user_agent = ("top comment puller by kulak85")
r = praw.Reddit(user_agent=user_agent)
# WHEN I REFRSH I KILL THE GENERATOR


def story():
	s_reddit = 'news'
	submissions = list(r.get_subreddit(s_reddit).get_top(limit=5))
	stories = [str(story.title) for story in submissions]
	top_comment = [x.comments[0].body for x in submissions]
	links = [link.url for link in submissions]
	zipper = zip(stories, top_comment, links)
	return zipper





def top_hn():
	r = requests.get('http://api.ihackernews.com/page')
	top_hn = r.json()
	hn_title = str(top_hn['items'][0].get('title'))
	hn_url = str(top_hn['items'][0].get('url'))