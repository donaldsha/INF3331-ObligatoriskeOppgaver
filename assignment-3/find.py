import os
import sys

thefile = sys.argv[1]
directory = sys.argv[2]

for root, directories, files in os.walk(directory):
	for file in files:
		if file == thefile:
			sys.stdout.write(root)
			sys.stdout.write(thefile)
			print