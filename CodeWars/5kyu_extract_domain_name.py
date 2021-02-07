def domain_name(url):
	domain = []
	if 'http' in url:
		link = (url.split('://')[1]).split('.')
	else:
		link = (url.split('.'))
	
	for item in link:
		if 'www' in item:
			pass	
		elif '/' in item or 'co' == item:
			domain = '.'.join(domain)
			return(domain)
		else:
			domain.append(item)
	
	domain = '.'.join(domain[:-1])

	return(domain)

print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("http://www.zombie-bites.com"))
print(domain_name("http://test.mywebsite.com"))
print(domain_name("www.xakep.ru"))
print(domain_name("http://www.more.test.thiswebsite.com/page.aspx"))
print(domain_name("codewars.com"))

'''
domain_name("http://github.com/carbonfive/raygun") == "github" 
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"

Test.assert_equals(domain_name("http://google.com"), "google")
Test.assert_equals(domain_name("http://google.co.jp"), "google")
Test.assert_equals(domain_name("www.xakep.ru"), "xakep")
Test.assert_equals(domain_name("https://youtube.com"), "youtube")
'''