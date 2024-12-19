import json

def jsonFileCheck(fileName = 'users.json'):
    try:
        with open(fileName, 'r') as file:
            content = file.read().strip()
            
            # if file is empty
            if not content:
                with open(fileName, 'w') as writeFile:
                    writeFile.write('[]')
                    
    # if file dont exist
    except FileNotFoundError:
        with open(fileName, 'w') as file:
            file.write('[]')

def readJsonFile(fileName = 'users.json'):
    try:
        with open(fileName, 'r') as file:
            content = file.read().strip()
            
            if not content:
                # create the file
                with open(fileName, 'w') as writeFile:
                    # update file's content
                    writeFile.write('[]')
                    return '[]'
            return json.loads(content)
        
    # if file dont exist
    except FileNotFoundError:
        with open(fileName, 'w') as file:
            file.write('[]')
            return '[]'