from AutoFunctions import AutoFunctions

#This is the middle-ground that should properly parse strings passed to the backend
class InputParser:
	af = None

	def __init__(self,subreddit):
		#Instantiate Backend Functionality
		self.af = AutoFunctions(subreddit)

	#The spaghetti doing the logic. Ew.
	def parse(self,args):
		if(len(args)==0):
			return 'No command given'
		elif(args[0]==('enlist')):
			if(len(args)!=2):
				return 'Expecting 1 argument for enlistment'
			else:
				result = self.af.enlist(args[1])
				if(result):
					return 'Welcome aboard'
				else:
					return 'Application denied'
		else:
			return "Command not recognized"