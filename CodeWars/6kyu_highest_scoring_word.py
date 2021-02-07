def high(x):
	top_score = 0
	top_word = ''

	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

	words = x.split()

	for word in words:
		score = 0
		for letter in word:
			score += alphabet.index(letter) + 1

		if score > top_score:
			top_score = score
			top_word = word
	return(top_word)


print(high('man i need a taxi up to ubud'))
print(high('what time are we climbing up the volcano'))
print(high('take me to semynak'))
   

'''
test.assert_equals(high('man i need a taxi up to ubud'), 'taxi')
test.assert_equals(high('what time are we climbing up the volcano'), 'volcano')
test.assert_equals(high('take me to semynak'), 'semynak')
'''