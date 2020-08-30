import json

# Getting data from a json file

with open("cars.json", "r") as pos_f:
    cars_data = json.load(pos_f) # load because suport files readers
    print(cars_data.get("cars"))
    print(type(cars_data))


# Getting data from a json string variable

string_json_data = """{
   "article": [

      {
         "id":"01",
         "language": "JSON",
         "edition": "first",
         "author": "Derrick Mwiti"
      },

      {
         "id":"02",
         "language": "Python",
         "edition": "second",
         "author": "Derrick Mwiti"
      }
   ],

   "blog":[
   {
       "name": "Datacamp",
       "URL":"datacamp.com"
   }
   ]
}
"""
as_dict = json.loads(string_json_data)
print(as_dict)