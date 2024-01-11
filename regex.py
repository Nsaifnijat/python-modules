# -*- coding: utf-8 -*-
import re
#the following gives a tab
print('\tText')
#to handle it litterally we have to make it raw to find patterns
print(r'\tText')

text='this world is .big, but this . world is heavy, ha haha'

pattern=re.compile(r'world')
#print the matches
matches=pattern.findall(text)
print(matches)
#print the match objects
matches=pattern.finditer(text)
for match in matches:
    print(match)

#if you want to find the following metacharacters, you need to put an escape before them
 . ^ $ * + ? {} [ ] \ | ( )
#the followin will find all characters
pattern=re.compile(r'.')
matches=pattern.findall(text)
print(matches)
#but if we need to find the exact . character, do as follow
pattern=re.compile(r'\.')
matches=pattern.findall(text)
print(matches)
metacharacters_usage=''' 

.   -it matches any character there is in the text
\d  -it matches the digits(0-9)
\D  -it anything but not digits(0-9)
\w  -word characters(a-z,A-Z,0-9,_)
\W  -Not a word character
\s  -whitespace(space,tab,newline)
\S  -not whitespace(space,tab,newline)

\b  -words with boundaries(space,or tabs before them)
\B  -not word with boundaries

^  -begining of a string
$  -end of a string
[] -specific characters inside it are fetched, you dont need to escape or put the or  operator the dot or any of metachars inside this

|  -either or
()  -group

Quantifiers

*  -0 or more
+  -1 or more
?  -0 or one
{3} -exact number
{1,4} -range of numbers(minimum,maximum)

'''

pattern=re.compile(r'\bha')
#seaches if the sentence start with this
pattern=re.compile(r'^this')
#search if it is in the end of string
pattern=re.compile(r'haha$')
matches=pattern.findall(text)
print(matches)

text2='''
coreyms.com
332.774.8883
233-232-3233
244*544*3434

900-343-2323
800-343-1212

Mr.schafer
Mr smith
Ms Davis
Mrs. Robinson
Mr. T
'''
#finding patterns in the above text
#all three digits
pattern=re.compile(r'\d\d\d')
#the phone number pattern, it returns all of the above three phones
pattern=re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
#or
pattern=re.compile(r'\d{3}.\d{3}.\d{4}')
print(pattern.findall(text2))
#this pattern returns only the first two
pattern=re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
#first character is 8 or 9
pattern=re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
#- as range
pattern=re.compile(r'[0-9]')
#- as dash, its - or 0 or 9
pattern=re.compile(r'[-09]')
#lower case and  upper case
pattern=re.compile(r'[a-zA-Z]')
#if we put carret in a list, it negates, return everything other than the set pattern
#not range 0-9
pattern=re.compile(r'[^0-9]')

#Mr then \.? zero or one then \s space then A-Z uppercase then \w* zero or more word chars
pattern=re.compile(r'Mr\.?\s[A-Z]\w*')
#usage of groups ()
#Mr or Ms or Mrs then \.? zero or one then \s space then A-Z uppercase then \w* zero or more word chars
pattern=re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
#or
pattern=re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches=pattern.findall(text2)
print(matches)

emails='''
CoreyMSchafer@gmail.com
corey.shafer@university.edu
corey-321-schafer@my-work.net

'''
#READ EMAILS
pattern=re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches=pattern.findall(emails)
print(matches)

urls='''

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov

'''
#READ urls in groups or parts
pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

matches=pattern.finditer(urls)
for match in matches:  
    print(match.group(0))
    print(match.group(1))
#to reformat our urls
pattern=re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#we only return the last two groups
subbed_urls=pattern.sub(r'\2\3',urls)
print(subbed_urls)
#it looks for the match at the start of sentence
pattern=re.compile(r'https')
start_sentence=pattern.match(urls)
print(start_sentence)
#it looks for the whole sentence
pattern=re.compile(r'https')
whole_sentence=pattern.search(urls)
print(whole_sentence)

#flags, used to make case insensitive

pattern=re.compile(r'start',re.IGNORECASE)

















