# -*- coding: utf-8 -*-

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":  # key为代码模板
		"Make a class named %%% that is-a %%%.", # value为解释模板
    "class %%%(object):\n\tdef __init__(self, ***)" : 
		"class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)": 
		"class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()": 
		"Set *** to an instance of class %%%.",
    "***.***(@@@)": 
		"From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'": 
		"From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())


def convert(snippet, phrase): # 接受一组PHRASES短语模板相互对应的key和value
    class_names = [w.capitalize() for w in # 大写首字母
					random.sample(WORDS, snippet.count("%%%"))] # 根据snippet（代码模板）中"%%%"的个数从WORD中随机取词
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
		for word in class_names:
			result = result.replace("%%%", word, 1)

        # fake other names
		for word in other_names:
			result = result.replace("***", word, 1)

        # fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result)

	return results


# keep going until they hit CTRL-D	
try:
    while True:
        snippets = PHRASES.keys() # 取短语模板PHRASES中的key（代码模板）组成snippets列表
        random.shuffle(snippets) # 洗牌，打乱snippets列表顺序

        for snippet in snippets: # 遍历
            phrase = PHRASES[snippet] # 将key对应的value赋值给phrase
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print question

            raw_input("> ")
            print "ANSWER: %s\n\n" % answer
except EOFError:
    print "\nBye"