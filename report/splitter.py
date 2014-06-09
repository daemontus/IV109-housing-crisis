from random import randint
import sys

f = open(sys.argv[1])	

head = True
entries = 2
values = [ [] for x in range(entries) ]
labels = []
for line in f:
	if head:
		head = False
	else:
		split = line.split()
		labels.append(split[0])
		split = split[1:]
		nsplit = []
		for l in split:
			l = l.replace(',','')
			nsplit.append(l)
		split = nsplit
		split = map(float, split)
		#values.append(split)
		for x in range(entries):
			values[x].append(split[x])

for x in range(len(labels)):
	if x%2 == 0:
		labels[x] = ''

print "var lineChartData = {"
print "	labels :", labels,","
print "	datasets : ["
first = True

colors = [
	(139,0,139),
]

for entry in values:
	if not first:
		print "		,"
	else:
		first = False
	print "		{"
	print "			strokeColor : \"rgba(%d,%d,%d,1)\"," % (randint(0,255), randint(0,255), randint(0,255))
	print "			fillColor : \"rgba(220,220,220,0)\","
	print "			pointStrokeColor : \"#fff\","
	print "			data : ", entry, ","
	print "		}"
print "	]"
print "}"