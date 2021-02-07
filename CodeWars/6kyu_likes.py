def likes(names):
	result = ''
	if names == []:
		return('no one likes this')
	
	namelist = [x for x in names]
	if len(namelist) == 1:
		return ''.join(namelist) + ' likes this'
	elif len(namelist) >= 4:
		result = ', '.join(namelist[:2]) + ' and ' + str(len(namelist[2:])) + ' others like this'
		return(result)
	else:
		result = ', '.join(namelist[:-1]) + ' and ' + ''.join(namelist[-1:]) + ' like this'
		return(result)


print(likes([]))
print(likes(['Peter']))
print(likes(['Jacob', 'Alex']))
print(likes(['Max', 'John', 'Mark']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))

'''
Test.assert_equals(likes([]), 'no one likes this')
Test.assert_equals(likes(['Peter']), 'Peter likes this')
Test.assert_equals(likes(['Jacob', 'Alex']), 'Jacob and Alex like this')
Test.assert_equals(likes(['Max', 'John', 'Mark']), 'Max, John and Mark like this')
Test.assert_equals(likes(['Alex', 'Jacob', 'Mark', 'Max']), 'Alex, Jacob and 2 others like this')
'''