#Importing the class library of json.
import json

#Creating Data dictionary.

data = {
    'name': 'John Doe',
    'age':  '23',
    'city': 'New York, NY',
    'interests': ['Traveling','Painting','Videogames', 'Crafting','Reading', 'volleyball' ]
}

#Creating a json file and writing the object contents to the json file.
with open('data.json','w') as json_file:

    json.dump(data,json_file,indent=4)

print("Data has been written to data.json")

#
with open('data.json','r') as json_file:
    #Creation of object called loaded_data.Load the json file into the agrument parameter.
    loaded_data = json.load(json_file)

print("Sucessfully able to read data.json")
print(loaded_data)

#Altering the json objects.
loaded_data['age'] = 25
loaded_data['interests'].append('Secret Hobby')

#Rewrite the changes to the json file.
with open('data.json','w') as json_file:

        json.dump(loaded_data,json_file,indent=4)

print("Data has been re-written to data.json")

