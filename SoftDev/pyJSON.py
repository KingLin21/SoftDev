#
import json


#
data1 = {
    'name':'Sebastian',
    'age':23,
    'city':'Seattle, WA',
    'interests':['Magic the Gathering, DnD, Movies, Video Games, Cars'],
    'is_student': True

}

with open('data1.json','w') as json_file:

    json.dump(data1,json_file,indent=4)

print("You have successfully written to data1.json")


