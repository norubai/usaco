"""
ID: espoir.1
LANG: PYTHON3
TASK: ride
"""

class Constant():
	@staticmethod
	def MOD():
		return 47

def getHash(name):
	hash = 1
	for c in name: 	hash = (hash*(ord(c)-ord('A')+1))%Constant.MOD()
	return hash

# with closes whatever theres to close.
with open("ride.in", "r") as oku:
    comet, nerds = oku.read().splitlines()

hn, hc = 1, 1
for c,n in zip(comet, nerds):
	hn = (hn*(ord(n)-ord('A')+1))%Constants.MOD()
	hc = (hc*(ord(c)-ord('A')+1))%Constants.MOD()


with open("ride.out", "w") as yaz:
	if hn == hc: 	yaz.write("GO\n")
	else: 			yaz.write("STAY\n")
