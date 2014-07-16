from AutoFunctions import AutoFunctions

#This is the middle-ground that should properly parse strings passed to the backend
class InputParser:
	af = None

	def __init__(self,subreddit,r=None):
		#Instantiate Backend Functionality
		self.af = AutoFunctions(subreddit,r)

	#The spaghetti doing the logic. Ew.
	def parse(self,args):
		if(len(args)==0):
			return 'No command given'
		elif(args[0]==('enlist')):
			if(len(args)!=2):
				return 'Wrong number of enlistment args'
			else:
				result = self.af.enlist(args[1])
				if(result):
					return 'Welcome aboard'
				else:
					return 'Application denied'
		else:
			return "Command not recognized"