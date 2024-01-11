import requests

r = requests.get('https://imgs.xkcd.com/comics/python.png')

print(r)

#to show us attributes 
print(dir(r))

#detailed explanation of the object
print(help(r))
print(r.text)
print(r.content)

#the above url is an image, that we can access from content of the r object and save it

with open('comic.png','wb') as f: #wb stands for write byte
    f.write(r.content)
#response types, 200=success, 300= redirect, 400=client errors when you want access a link that you are not allowed, 
#500 = server errors when server is down
print(r.status_code)
#if there is a server error, the following will be false otherwise for anyting less than 500 its true
print(r.ok)

print(r.headers)


#to query a url, we can do the following suppose we have the following url, we do two ways

#1
r = requests.get('https://httpbin.org/get?page=2&count=25')
print(r.text)
#2
payload = {
    "page": 2,
    "count":25
    
    }
r = requests.get('https://httpbin.org/get', params = payload)

print(r.text)
print(r.url)


#in the following we post data to a form

payload = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data = payload)


#folllowing method converts r.text to  a dictionary

r_dict = r.json()

print(r_dict['form'])


#now to authorize using the above credentials
r = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey','testing'))

print(r.text)

#it gives the result after three seconds
r = requests.get('https://httpbin.org/delay/', timeout=3)
print(r.text)















