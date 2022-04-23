import json
from stat import filemode

class work:
    f = open('data/data_2.json')
    # this gives json object as a dictionary
    dict = json.load(f)

    # this converts dictionary to string
    str = json.dumps(dict)
    # this convverts json string to python
    load = json.loads(str)

    req = {
        "required": "false"
    }
    app = {**dict["message"], **req}

    print(list(app.keys()))
    # print(list(app.values()))
    # with open('sample.json','w') as json_file:
    #json.dump(app, json_file)
    # print(app)


    # print(str)
    # print(load["message"])

    f.close()
