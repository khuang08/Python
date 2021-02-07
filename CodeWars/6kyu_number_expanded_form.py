def expanded_form(num):
	num = str(num)
	expanded = []
	count = 1

	for i in num:
		if i != '0':
			expanded.append(i + ('0' * (len(num) - count)))
		count += 1
	
	return(' + '.join(expanded))


print(expanded_form(12))
print(expanded_form(42))
print(expanded_form(70304))
print(expanded_form(39536))

'''
test.assert_equals(expanded_form(12), '10 + 2');
test.assert_equals(expanded_form(42), '40 + 2');
test.assert_equals(expanded_form(70304), '70000 + 300 + 4');
'''