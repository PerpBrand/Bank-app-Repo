# REGULAR EXPRESSION == REGEX
# 1 - INTRODUCTION TO REGEX
# 2 - SIMPLE CHARACTER MATCHES
# 3 - CHARACTER CLASSES
# 4 - SPECIAL CHARACTERS
# 5 - QUANTIFIERS
# 6 - SUBSTITUTING
# 7 - COMPILING REGULAR EXPRESSION
# 8 - SPLIT FUNCTION USING REGEX


# COREY SCHAFER

import re

# 2 - SIMPLE CHARACTER MATCHES

'''
text = 'cat bat mat rat mat'
pattern = 'mat'

# re.findall('the pattern would go here','the text would go here')
output=re.findall(pattern,text)
print(output)

'''

'''text = 'cat bat mat rat mat'
pattern = 'dart'
output=re.findall(pattern,text)
print(output)
'''

'''text = 'The dog barks loudly'
pattern = 'dog'
output=re.findall(pattern,text)
print(output)
'''

# 3 - CHARACTER CLASSES
'''
text= 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
pattern=r'\d' # trying to get the matches for digits piece by piece
output=re.findall(pattern,text)
print(output)


text= 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
pattern=r'\d+' # trying to get the matches for digits just the way it was in the text file
output=re.findall(pattern,text)
print(output)


text= 'We have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
pattern=r'[a-z]+' # trying to extract for lowercase letters
output=re.findall(pattern,text)
print(output)


text= 'WE have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
pattern=r'[A-Z]+' # trying to extract for uppercase letters
output=re.findall(pattern,text)
print(output)

text = 'cat bat mat rat mat'
pattern = r'[^a]' # extract everything in the text aside 'a'
output=re.findall(pattern,text)
print(output)


text= 'WE have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
pattern=r'[a-zA-Z]+' # trying to extract for just alphabets
# pattern=r'\w'
output=re.findall(pattern,text)
print(output)


text= 'WE have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
pattern=r'[a-zA-Z\d]+' # trying to extract for just alphabets and numbers
output=re.findall(pattern,text)
print(output)



text= 'WE have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
#pattern=r'[^ a-zA-Z\d]'    # trying to extract for the dollar sign
pattern=r'[.]'
output=re.findall(pattern,text)
print(output)



text= 'WE have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40.'
pattern=r'[\s]'
output=re.findall(pattern,text)
print(output)



text= 'WE have 3 Apples and 14 Oranges in 1343 Avenue which is priced for $40'
pattern=r'[^a-zA-Z\d\s]'    # trying to extract for the dollar sign
# pattern=r'[$]'
output=re.findall(pattern,text)
print(output)


text= 'Hello World 1234567890'
pattern=r'[A-I]'
# pattern =r'[0-9] # can also be used to extract digits
output=re.findall(pattern,text)
print(output)

'''
# 4 - SPECIAL CHARACTERS

text = 'hello world hallo heeello'
pattern = r'h.llo' # extract for words starting 'h' and ending with 'llo' but has just one letter in between the aforementioned 
output=re.findall(pattern,text)
print(output)


text = 'hello world hallo heeello'
pattern = r'h.*llo' 
output=re.findall(pattern,text)
print(output)


text = 'heeello'
pattern = r'h.*llo' 
output=re.findall(pattern,text)
print(output)

text = 'hello world hallo heeello'
pattern = r'h.llo' 
output=re.findall(pattern,text)
print(output) # >>>>>>  [hello, hallo] 
 
text = 'dello world falld heeello'
pattern = r'.ld' 
output=re.findall(pattern,text)
print(output)

text = 'hello world hallo heeello'
pattern = r'h.*llo' 
output=re.findall(pattern,text)
print(output)

text = 'heeello'
pattern = r'h.*llo' 
output=re.findall(pattern,text)
print(output)


text = 'dello world falld heeello'
pattern = r'.*ld' 
output=re.findall(pattern,text)
print(output)

# 5 - QUANTIFIERS

text='a aa aaa aaaa aaaaa aaaaaa'
pattern = r'a*' # for the letter 'a' appearing zero or more times
output = re.findall(pattern,text)
print(output)


text='a aa aaa c aaaa aaaaa aaaaaa b v d'
pattern = r'a*' # for the letter 'a' appearing zero or more times
output = re.findall(pattern,text)
print(output)


text='a aa aaa aaaa aaaaa aaaaaa'
pattern = r'a+' # for the letter 'a' appearing one or more times
output = re.findall(pattern,text)
print(output)


text='a aa aaa aaaa aaaaa aaaaaa'
pattern = r'a{3}' # extract for the letter 'a' that has appeared three times
output = re.findall(pattern,text)
print(output)

print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')


text='a aa aaa aaaa aaaaa aaaaaa'
pattern = r'a{3,}' # for the letter 'a' appearing three or more times
output = re.findall(pattern,text)
print(output)


text='a aa aaa aaaa aaaaa aaaaaa'
pattern = r'a{3,5}' # for the letter 'a' appearing three to five times
output = re.findall(pattern,text)
print(output)



# 6 - SUBSTITUTING
text = 'Daniel and Marvelous are friends'
pattern = 'friends'
# re.sub('the pattern that we are trying to substitute', 'the replacement word', 'text)
output=re.sub(pattern,'enemies',text)
print(output)


# 8 - SPLIT FUNCTION USING REGEX

'''text.split() == text.split(' ') 
'''
# splitting using the normal string manipulation method
text = 'KAUTHAR and FIRDAUSI are friends'
print(text.split())

# now splitting using the REGEX (Regular Expression)
text = 'KAUTHAR and FIRDAUSI are friends'
pattern=r'\s+'
output = re.split(pattern,text)
print(output)
