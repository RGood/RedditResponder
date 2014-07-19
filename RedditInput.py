import praw
from InputParser import InputParser

r = praw.Reddit("Input Getter")
r.login()

flag = True

ip = InputParser(r)

attentionCommand = 'hey_bucket:'

kill_command = u'shutdown auth=8675309' #Hardcoded kill command

bot_admins = [] #Initialize list of people with kill-permission
file = open('data/bot_admins.txt','r')
for line in file:
	bot_admins+=[line.strip()]
file.close()

restricted = [] #Initialize list of restricted subs
rs = open('data/restricted_subs.txt','r')
for line in rs:
	restricted+=[line.lower().strip()]
rs.close()

post_script = u'' #Initialize bot post-script
ps = open('data/post_script.txt','r')
for line in ps:
	post_script += line
ps.close()

commandQueue = []

def exec_commands():
	to_return = True
	for c in commandQueue:
		if(c.subreddit.name.lower() in restricted):
			pass
		elif(c.body.lower().find('exclude')==0):
			command = (c.body + ' ' + c.author.name.lower()).split(' ')
			print(command)
			try:
				if(command[1].find('/r/')==0):
					command[1] = command[1][3:]
				sub = r.get_subreddit(command[1])
				mod = r.get_redditor(command[2])
				if(mod in sub.get_moderators() and sub.display_name.lower() not in restricted):
					restricted.append(sub.display_name.lower())
				c.reply('This bot will no longer post in /r/' + sub.display_name + post_script)
			except:
				c.reply('That subreddit is already private and cannot be accessed' + post_script)
			
		elif(c.body.find(kill_command)==0 and c.author.name.lower() in bot_admins):
			print 'Shutdown executed'
			to_return = False
		else:
			command = (c.body).split(' ')
			print(command)
			c.reply(ip.parse(command).decode('utf-8')+post_script)

	while(len(commandQueue)>0):
		commandQueue.pop()
		
	return to_return



curMail = []

print("Scrubbing Inbox...")

while(flag):
	try:
		mail = r.get_inbox(limit = 5)
		for m in mail:
			if(m.name not in curMail):
				curMail.insert(0,m.name)
				if(len(curMail)>50):
					curMail.pop()
				if(m.body.lower().find(attentionCommand.lower())==0):
					m.body = m.body[len(attentionCommand):].lstrip().rstrip()
					commandQueue.insert(0,m)
				elif(m.body.lower().find('/u/'+r.user.name.lower()+':')==0):
					m.body = m.body[len('/u/'+r.user.name+':'):].lstrip().rstrip()
					commandQueue.insert(0,m)
		flag = exec_commands()
	except KeyboardInterrupt:
		flag = False

print('Bot shutting down...')

rs = open('data/restricted_subs.txt','w')
for r in restricted:
	rs.write(r+'\n')
rs.close()

print("Ended.")