import sys
import praw
import unicodedata

user_agent='bloppit_app'

if len(sys.argv) == 2:
	script, filename, subreddit = argv
else:
	subreddit = "opensource"
	filename = subreddit + ".txt"
	

r = praw.Reddit(user_agent)
submissions = r.get_subreddit(subreddit).get_hot(limit=100)
target = open(filename, 'w')

for x in submissions:
	line = (str(x.fullname) + ", " + str(x.title.encode("cp437","ignore"))[1:] + " , " + str(x.url.encode("cp437","ignore"))[1:].strip('"\'')) 
	print(line)
	target.write(line)
	target.write("\n")

target.close()

	
