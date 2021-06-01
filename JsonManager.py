import json

class JsonManager:
    def write_in_json():
        person_dict = {"name": "Bob",
        "languages": ["English", "Fench"],
        "married": True,
        "age": 32
        }

        with open('request.json', 'w') as json_file:
            json.dump(person_dict, json_file)
    
    def say():
        print('hi')