import csv
import numpy as np
from time import sleep

# with open('../data/train.csv', 'rb') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     print spamreader
#     print ', '.join(spamreader)

# def isinteger(x):
#     return np.equal(np.mod(x, 1), 0)
trial = 0

target = []

features = []
feat = []

with open('../data/train.csv') as csvfile:
    dictreader = csv.DictReader(csvfile)
    # csvreader = csv.reader(csvfile)
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')

    csvreader.next() # skip the header line

    for row in csvreader:
    	trial += 1
    	# A = csvreader.next()
    	target.append(row[-1])

    	# features.append(row[100]

    	for j in range(100,200): 
    		feat.append(row[j])

        features.append(feat)
        feat = []

    	# print (row[100] + ', ' + row[101] + ', target: ' + target[-1])

    	# print (target, ', trial: ', trial) .
    	# print row

    	print features[0]

    	sleep(1)
