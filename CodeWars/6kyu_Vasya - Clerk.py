def tickets(people):
	change = []
	
	for cash in people:
		if cash == 25:
			pass
		elif cash == 50 and 25 in change:
			change.remove(25)
		elif cash == 100 and 25 in change and 50 in change:
			change.remove(25)
			change.remove(50)
		elif cash == 100 and (change.count(25) >= 3):
			change.remove(25)
			change.remove(25)
			change.remove(25)
		else:
			return("NO")
		change.append(cash)
	return("YES")

print(tickets([25, 25, 50]))
print(tickets([25, 100]))
print(tickets([25, 25, 50, 50, 100]))

'''
test.assert_equals(tickets([25, 25, 50]), "YES")
test.assert_equals(tickets([25, 100]), "NO")
test.assert_equals(tickets([25, 25, 50, 50, 100]), "NO")
'''
