# -*- coding: utf-8 -*-

import random
from urllib import urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
	"class %%%(%%%):": # key为代码模板
		"Make a class named %%% that is-a %%%.", # value为解释模板
	"class %%%(object):\n\tdef __init__(self, ***)":
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
if len(sys.argv) == 2 and sys.argv[1] == "english": # 判断argv的情况，确定是否反转question和answer
	PHRASE_FIRST = True
else:
	PHRASE_FIRST = False
	
# load up the words from the website
for word in urlopen(WORD_URL).readlines():
	WORDS.append(word.strip()) 
	# 从WORD_URL对应网站上逐行取字符串，写入WORD列表
	
	
def convert(snippet, phrase): # 接收PHRASES短语模板相互对应的key和value（两个字符串）
	class_names = [w.capitalize() for w in # w.capitalize():大写首字母
					random.sample(WORDS, snippet.count("%%%"))] 
					# 根据snippet（字符串）中"%%%"的个数从WORD列表中随机取词，并大写单词首字母，放入class_names列表中
	# 由于遍历每个元素，组成list，加[]
	# 现在我们得到数量与"%%%"个数对应的单词组成的列表class_names
	other_names = random.sample(WORDS, snippet.count("***")) # random.sample()从列表WORD中抽取，组成列表other_names
	results = []
	param_names = []
	
	for i in range(0, snippet.count("@@@")):
		param_count = random.randint(1, 3) # 以1，3为上下限生成随机数，赋值给param_count
		param_names.append(', '.join(random.sample(WORDS, param_count)))
		# 根据param_count的数值，从WORDS中随机取词组成列表，用', '连接，整体作为一个字符串加入param_names列表中
	
	# for result in snippet, phrase: # ！！！存疑！！！用这句for语句替换下两行，未发现异常
	for sentence in snippet, phrase:
		result = sentence[:] # ！！！存疑！！！如果snippet和phrase都是str,那么这个切片复制应该是没有意义的，为什么不直接用sentence操作下面的步骤？
		# print "type(snippet) is %r" % type(snippet) # 用于测试，已确定snippet, phrase, sentence, result均为字符串
		# print "type(phrase) is %r" % type(phrase)
		# print "type(sentence) is %r" % type(sentence)
		# print "type(result) is %r" % type(result)
		
		# fake class names
		for word in class_names: # 做class_names列表中的个数（对应snippet中"%%%"个数）次循环
			# print "at first, result is %r" % result # 配合下两句注释中的print语句，确认result为str，每循环一次，替换一个"%%%"
			result = result.replace("%%%", word, 1) # 替换result中的"%%%"。第三个参数"1"表示替换不超过1次
			# print "then, result is %r" % result
			# print "type(result) is %r" % type(result)
		
		# fake other names
		for word in other_names:
			result = result.replace("***", word, 1)
			
		# fake parameter lists
		for word in param_names:
			result = result.replace("@@@", word, 1)

		results.append(result) # 将替换过的字符串result添加到列表results中
		
	return results # 返回列表results
	

# keep going until they hit CTRL-D
try: # ！！！异常处理语句，具体内容需学习！！！
	while True:
		snippets = PHRASES.keys() # 取短语模板PHRASES中的key（代码模板）组成snippets列表
		random.shuffle(snippets) # 洗牌，打乱snippets列表顺序
		
		for snippet in snippets: # （遍历）读取snippets中的元素写入snippet（一个字符串）
			phrase = PHRASES[snippet] # 将key对应的value赋值给phrase（一个字符串）
			# 此时我们得到一个字典PHRASES的key列表snippets以及和他对应的value列表phrase
			# print "type(snippet) is %r" % type(snippet) # 用于测试，已确定snippet和phrase为字符串
			# print "type(phrase) is %r" % type(phrase)
			question, answer = convert(snippet, phrase) # 函数convert读取两个字符串snippet, phrase并生成两个str
			# print "question is %r" % question # 用于测试
			# print "type(question) is %r" % type(question)
				
			if PHRASE_FIRST:
				question, answer = answer, question
			print question
			
			raw_input("> ")
			print "ANSWER: %s\n\n" % answer
except EOFError:
	print "\nBye"