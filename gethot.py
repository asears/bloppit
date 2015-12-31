import praw
import unicodedata

r = praw.Reddit(user_agent='bloppit_app')
submissions = r.get_subreddit('opensource').get_hot(limit=100)
for x in submissions:
	print (str(x.fullname) + ", " + str(x.title.encode("cp437","ignore"))[1:] + " , " + str(x.url.encode("cp437","ignore"))[1:].strip('"\'')) 
