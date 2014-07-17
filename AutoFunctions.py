import praw
import os.path

class AutoFunctions:
	r = None
	sr = None
	c_names = []
	ranks = {}

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

		self.ranks = {}
		file = open('ranks.csv','r')
		for line in file:
			if(line!=''):
				info = line.split(',')
				self.ranks[info[0]] = info[1].rstrip()
		file.close()

	def enlist(self,user):
		if(self.is_contrib(user)):
			if(user in self.ranks.keys()):
				self.sr.set_flair(self.r.get_redditor(user),flair_text='',flair_css_class=self.ranks[user])
			else:
				self.ranks[user]='ensign'
				self.sr.set_flair(self.r.get_redditor(user),flair_text='',flair_css_class=self.ranks[user])
				file = open('ranks.csv','w')
				for k in self.ranks.keys():
					file.write(k+','+self.ranks[k]+'\n')
				file.close()
			return True
		else:
			return False

	def set_custom(self,args):
		field=0
		command = ''
		response = ''
		for w in args:
			if(('/' in w or '\\' in w) and field==0):
				return "Cannot have '\\' or '/' in command"
			if(w.lower()=='set:'):
				field = 0
			elif(w.lower()=='to:'):
				field = 1
			elif(field==0):
				if(command!='' or w==''):
					command+=' '
				command+=w
			elif(field==1):
				if(response!='' or w==''):
					response+=' '
				response+=w
		if(os.path.exists('custom_commands/'+command+'.txt')):
			return "Command already exists"
		else:
			f = open('custom_commands/'+command+'.txt','w+')
			f.write(response.encode('utf-8').strip())
			f.close()
			return "Command set"

	def get_custom(self,args):
		command = ''
		response = ''
		for w in args:
			if(command!=''):
				command+=' '
			command+=w
		if(os.path.exists('custom_commands/'+command+'.txt')):
			f =  open('custom_commands/'+command+'.txt','r')
			for line in f:
				response += line
		else:
			response = 'Command does not exist'
		return response

	def is_contrib(self,user):
		if(user.lower() in self.c_names):
			return True
		else:
			return False