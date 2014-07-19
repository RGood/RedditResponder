import praw
import os.path

class AutoFunctions:
	r = None
	sr = None

	def __init__(self,r=None):
		#Create Reddit Client and login
		if(r==None):
			self.r = praw.Reddit("AutoResponder")
			self.r.login()
		else:
			self.r = r

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
			try:
				f = open('custom_commands/'+command+'.txt','w+')
				f.write(response.encode('utf-8').strip())
				f.close()
				return "Command set"
			except:
				return "Setting command failed"

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