def solution(s):
	result = []
	for letter in s:
		if letter.isupper():
			result.append(' ')
		result.append(letter)
	return ''.join(result)

print(solution("helloWorld"))
print(solution("camelCase"))
print(solution("breakCamelCase"))

'''
Test.assert_equals(solution("helloWorld"), "hello World")
Test.assert_equals(solution("camelCase"), "camel Case")
Test.assert_equals(solution("breakCamelCase"), "break Camel Case")
'''
