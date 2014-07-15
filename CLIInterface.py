import sys
from InputParser import InputParser

flag = True
command = ''

ip = InputParser('CenturyClub')

while(flag):
	sys.stdout.write('>>>')
	command = raw_input()
	if(command == 'exit'):
		flag = False
	else:
		print ip.parse(command.split(" "))
