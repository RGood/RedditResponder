import praw
from InputParser import InputParser

r = praw.Reddit("Input Getter")
r.login()

ip = InputParser('CenturyClub',r)

attentionCommand = 'randybot:'

post_script = "\n\n________\n\n^^This ^^response ^^was ^^generated ^^by ^^my ^^robot ^^half. ^^If ^^there ^^are ^^problems, ^^please ^^send ^^me ^^a [^^private ^^message](http://www.reddit.com/message/compose/?to=The1RGood&subject=Bot-Problem)."

commandQueue = []

def exec_commands():
	for c in commandQueue:
		if(c.body.find('enlist')==0):
			command = (c.body + ' ' + c.author.name).split(' ')
			print(command)
			c.reply(ip.parse(command))
		else:
			command = (c.body).split(' ')
			print(command)
			c.reply(ip.parse(command)+post_script)

	while(len(commandQueue)>0):
		commandQueue.pop()


flag = True
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
					m.body = m.body[len(attentionCommand):].lstrip().rstrip().lower()
					commandQueue.insert(0,m)
		exec_commands()
	except KeyboardInterrupt:
		flag = False

print("Ended.")