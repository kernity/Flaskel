#! /usr/bin/env python

import subprocess
from optparse import OptionParser

def main():
	usage = "usage: %prog new <name>"
	parser = OptionParser(usage)
	(options, args) = parser.parse_args()

	if len(args) != 2:
		parser.error("incorrect number of arguments")
	name = args[1]
	print "Bootstraping Flaskel project"
	subprocess.call(["paster", "create", "-t", "flaskel", name])

if __name__ == "__main__":
	main()

