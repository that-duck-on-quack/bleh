
import json
import os 


#functions utils
def loaddata(file):
    current_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.abspath(os.path.join(current_dir, '..'))

    data_path = os.path.join(project_root, 'data', file)

    with open(data_path, 'r') as f:
        return json.load(f)