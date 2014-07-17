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
		elif(args[0].lower()==('enlist')):
			if(len(args)!=2):
				return 'Wrong number of enlistment args'
			else:
				result = self.af.enlist(args[1])
				if(result):
					return 'Welcome aboard'
				else:
					return 'Application denied'
		elif(args[0].lower()==('k')):
			return self.af.k()
		elif(args[0].lower()==('set:')):
			if('to:' in args or 'To:' in args or 'TO:' in args or 'tO:' in args):
				return self.af.set_custom(args)
			else:
				return '\"to: \" field not found (you need a space after \"to:\")'
		else:
			return self.af.get_custom(args)