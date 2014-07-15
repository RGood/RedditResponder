import praw

class AutoFunctions:
	r = None
	sr = None
	c_names = None

	def __init__(self,subreddit):
		#Create Reddit Client and login
		self.r = praw.Reddit("AutoResponder")
		self.r.login()

		#Create object pointing to the subreddit this is for
		self.sr = self.r.get_subreddit(subreddit)

		#Dynamically instantiate the contributors list. (Should take about 10 seconds)
		contribs = self.sr.get_contributors(limit=None)
		self.c_names = []
		for c in contribs:
			self.c_names.append(c.name.lower())

	def enlist(self,user):
		if(self.is_contrib(user)):
			self.sr.set_flair(self.r.get_redditor(user),flair_text='',flair_css_class='ensign')
			return True
		else:
			return False

	def is_contrib(self,user):
		if(user.lower() in self.c_names):
			return True
		else:
			return False