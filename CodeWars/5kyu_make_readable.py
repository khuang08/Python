def make_readable(seconds):
	hours = seconds // 3600
	minutes = (seconds - hours*3600) // 60
	seconds = seconds % 60
	return('%02d:%02d:%02d' % (hours,minutes,seconds))
	
print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
'''
Test.assert_equals(make_readable(0), "00:00:00")
Test.assert_equals(make_readable(5), "00:00:05")
Test.assert_equals(make_readable(60), "00:01:00")
Test.assert_equals(make_readable(86399), "23:59:59")
Test.assert_equals(make_readable(359999), "99:59:59")
'''