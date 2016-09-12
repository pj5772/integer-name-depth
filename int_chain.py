import inflect

p = inflect.engine()
f = open("out.csv", "w")

i = 0 

N = int(input("enter upper limit of domain: "))

def getlen(n):
	s = p.number_to_words(n)
	if (" and " in s): s = s.replace("and","")
	if ("thous" in s): s = s.replace("thous", "thousand")
	if (" " in s): s = s.replace(" ", "")
	if ("," in s): s = s.replace(",", "")
	return len(s)

def getDepth(n):
	count = 0
	while not (getlen(n) == 4):
		n = getlen(n)
		count += 1
	else: return count

while i <= N:
	i += 1
	f.write(str(i) + "," + str(getDepth(i)) + "\n")
else: f.close()