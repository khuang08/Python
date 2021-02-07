def order(sentence):
	nums = []
	words = sentence.split()
	
	for i in sentence:
		if i.isdigit():
			nums.append(i)

	combined = dict(zip(nums,words))
	result = ' '.join([value for (key, value) in sorted(combined.items())])
	return result

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))

'''
Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
Test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
Test.assert_equals(order(""), "")
'''