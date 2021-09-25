import random
wordsfilepath = "text"
missedfilepath = "missed"


""" process data from text file """

def getWordDict():
	d = {}
	# {word: [(definition, example), (definition), (definition, example)], word: ...}

	f = open(wordsfilepath, "r")
	word = ""
	example = ""
	definition = ""
	lines = f.readlines()
	i = 0
	d = {}
	while i < len(lines):

		line = lines[i]
		word = line.replace("\n", "")
		d[word] = []

		i += 1
		line = lines[i]
		while not line.startswith("=="):
			if line.startswith("Eg:"):
				# code for adding eg to dict
				d[word][-1].append(line.replace("\n", ""))
			else:
				# code for adding definition to dict
				d[word].append([line.replace("\n", "")])
			i += 1
			line = lines[i]

		i += 1
	return d

def quiz(mydict):
	words = list(mydict)
	random.shuffle(words)
	for word in words:
		input(f"think of the meaning of {word}. Press enter when done: ")
		for item in d[word]:
			print()
			for subitem in item:
				print(subitem)
		print()
		yn = input("were you able to remember it? (y/n)")
		if yn == "n":
			with open(missedfilepath+"(1)", "a") as myfile:
				myfile.write(word+"\n")
		print("===================")

def getMissedDict(wordDict):
	missedDict = {}
	f = open(missedfilepath, "r")
	words = f.read().splitlines()
	for word in words:
		missedDict[word] = wordDict[word]
	return missedDict

def study(mydict):
	words = list(mydict)
	random.shuffle(words)
	for word in words:
		input(f"Try to think of the meaning of {word}. Press enter when done: ")
		for item in mydict[word]:
			print()
			for subitem in item:
				print(subitem)
		print()
		yn = input("Press enter to move on.")
		print("===================")
	

wordDict = getWordDict()
missedDict = getMissedDict(wordDict)
#quiz(mydict=missedDict)
study(mydict=missedDict)