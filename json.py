'''json code to push into sql database'''
import json

def json_to_sql(json_file):
    '''function to convert json to sql'''
    with open(json_file) as file:
        data = json.load(file)
    return data