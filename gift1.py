"""
ID: espoir.1
LANG: PYTHON3
TASK: gift1
"""

class Constants():
	pass
#Define constans here with @staticmethod functions

class Person():
	instances = []
	
	@classmethod
	def get(cls, name):
		for person in cls.instances:
			if person.name == name:		return person
		return None

	def __init__(self, name):
		self.name = name
		self.balance = 0

	def gift_to(self, friend, moni):
		self.balance -= moni
		friend.balance += moni

	def __str__(self):
		return self.name + " " + str(self.balance) + "\n" 

with open("gift1.in", "r") as infile:
	NP = int(infile.readline())
	# get the names & crate Person instances.
	for i in range(NP):
		name = infile.readline().rstrip()
		Person.instances.append(Person(name))

	# read the giver-recievers blocks
	for i in range(NP):
		gname = infile.readline().rstrip()
		captl, quant = map(int, infile.readline().split())
		if quant == 0:	continue # continue if there are no recievers
		giver = Person.get(gname)
		trans = captl//quant # get the transaction amount
		for i in range(quant):
			rname = infile.readline().rstrip()
			recvr = Person.get(rname)
			giver.gift_to(recvr, trans)



with open("gift1.out", "w") as outfile:
	for p in Person.instances:	outfile.write(str(p))
