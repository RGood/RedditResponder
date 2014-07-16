import praw

class AutoFunctions:
	r = None
	sr = None
	c_names = None

	def __init__(self,subreddit,r=None):
		#Create Reddit Client and login
		if(r==None):
			self.r = praw.Reddit("AutoResponder")
			self.r.login()
		else:
			self.r = r

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

	def k(self):
		text = "    kkkkkkkkkkkkkkk    \n    kk   kkkkk   kk    \n    kk   kkkk   kkk    \n    kk   kkk   kkkk    \n    kk   kk   kkkkk    \n    kk   k   kkkkkk    \n    kk      kkkkkkk    \n    kk   k   kkkkkk    \n    kk   kk   kkkkk    \n    kk   kkk   kkkk    \n    kk   kkkk   kkk    \n    kkkkkkkkkkkkkkk"
		return text