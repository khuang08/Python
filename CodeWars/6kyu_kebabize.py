def kebabize(string):
	string = (''.join(['-' + x.lower() if x.isupper() else '' if x.isdigit() else x for x in list(string)]))
	if string == '':
		return ''
	elif '-' in string[0]:
		string = string[1:]
	return string

print(kebabize('myCamelCasedString')) #'my-camel-cased-string'
print(kebabize('myCamelHas3Humps')) #'my-camel-has-humps'
print(kebabize('SOS')) #'s-o-s'
print(kebabize('42')) #''
print(kebabize('CodeWars')) #'code-wars'
print(kebabize('4Ao3Es')) #'ao-es'
