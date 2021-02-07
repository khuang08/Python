def count_smileys(arr):
	count = 0
	eyes = [':', ';']
	nose = ['-', '~']
	mouth = [')','D']

	for i in arr:
		if len(i) == 3 and i[0] in eyes and i[1] in nose and i[2] in mouth:
			count += 1
		elif len(i) == 2 and i[0] in eyes and i[1] in mouth:
			count += 1

	return count


print(count_smileys([]))
print(count_smileys([':D',':~)',';~D',':)']))
print(count_smileys([':)',':(',':D',':O',':;']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))

'''
Test.describe("Basic tests")
Test.assert_equals(count_smileys([]), 0)
Test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
Test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
Test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)
'''

