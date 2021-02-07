def abbreviate(s):
	result = ''
	word = ''

	for letter in s:
		if letter.isalpha():
			word += letter
		else:
			if len(word) >= 4:
				result += word[0:1] + str(len(word[1:-1])) + word[-1:] + letter
				word = ''
			else:
				result += word + letter
				word = ''

	if len(word) > 0:
		result += word[0:1] + str(len(word[1:-1])) + word[-1:]
	
	return result


print(abbreviate("internationalization"))
print(abbreviate("accessibility"))
print(abbreviate("Accessibility"))
print(abbreviate("elephant-ride"))
print(abbreviate("elephant-rides are really fun!"))
print(abbreviate("elephant-rides are elephant-rides"))
print(abbreviate("monolithic"))
print(abbreviate("mat'"))

'''
Test.assert_equals(abbreviate("internationalization"), "i18n")
Test.assert_equals(abbreviate("accessibility"), "a11y")
Test.assert_equals(abbreviate("Accessibility"), "A11y")
Test.assert_equals(abbreviate("elephant-ride"), "e6t-r2e")
Test.assert_equals(abbreviate("elephant-rides are really fun!"), "e6t-r3s are r4y fun!")
'''