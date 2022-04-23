import json
from stat import filemode

class work:
    f = open('data/data_2.json')
    # This line converts the json objects to a dictionary
    dict = json.load(f)

    #This line creates a dictionary
    req = {
        "required": "false"
    }
    #This line appends a dictionary to the existing dictionary to ensure the "required" tag is set to false 
    app = {**dict["message"], **req}

    with open('sample.json','w') as json_file:
        json.dump(app, json_file)
    
    f.close()
