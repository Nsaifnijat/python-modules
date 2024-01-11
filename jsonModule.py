# -*- coding: utf-8 -*-
import json
  
'''

The JSON package in python has a function called json.dumps() that helps in converting a dictionary to a JSON object.

It takes two parameters:

dictionary – name of dictionary which should be converted to JSON object.
indent – defines the number of units for indentation
After converting dictionary to a JSON object, simply write it to a file using the “write” function
'''
# Data to be written
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
  
# Serializing json 
json_object = json.dumps(dictionary, indent = 4)
  
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
'''  
 Using json.dump()

Another way of writing JSON to a file is by using json.dump() method

The JSON package has the “dump” function which directly writes the dictionary to a file in the form of JSON, without needing to convert it into an actual JSON object.

It takes 2 parameters:

dictionary – name of dictionary which should be converted to JSON object.
file pointer – pointer of the file opened in write or append mode.   
    '''
#method 2  
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
    
#method 3
with open('file.json', 'a') as outfile:
    outfile.write(json.dumps(data))
    outfile.write(",")
    outfile.close()


import json

dictionary ={
    'message':
        {
    "name" : "",
    "rollno" :"" ,
    "cgpa" : "",
    "phonenumber" : ""
    },

    'reply':
        {
        "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
    },
        'modify':{
            
            
            }
}
  

    
with open("sample.json", "w") as outfile:
    json.dump(dictionary,outfile, indent=2)
    
        
with open("sample.json") as outfile:
    data=json.load(outfile)
    print(type(data))
    data.append('message')
    print(data.keys())