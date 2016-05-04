snippet = "class %%%(%%%):"
phrase = "Make a class named %%% that is-a %%%."
word = ["Apple", "Orange"]
for sentence in snippet, phrase:
	result = sentence[:]
	print "result = %r" % result
	print "sentence = %r" % sentence
	for wo in word:
		result = result.replace("%%%", word, 1)
		print "wo = %r" % wo
	print "sentence = %r" % sentence
	print "snippet = %r" % snippet
	print "phrase = %r" % phrase