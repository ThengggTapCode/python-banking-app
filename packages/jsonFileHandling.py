import json

def jsonFileCheck(fileName = 'users.json'):
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            
            # if file is empty
            if not content:
                with open(fileName, 'w', encoding='utf-8') as writeFile:
                    writeFile.write('[]')
                    
    # if file dont exist
    except FileNotFoundError:
        with open(fileName, 'w', encoding='utf-8') as file:
            file.write('[]')

def readJsonFile(fileName = 'users.json'):
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            
            if not content:
                # create the file
                with open(fileName, 'w', encoding='utf-8') as writeFile:
                    # update file's content
                    writeFile.write('[]')
                    return []
            return json.loads(content)
        
    # if file dont exist
    except FileNotFoundError:
        with open(fileName, 'w', encoding='utf-8') as file:
            file.write('[]')
            return []
        
def saveDataToJson(data, fileName = 'users.json'):
    with open(fileName, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
        
def updateJsonData(newData, username):
    users = readJsonFile()
    
    for user in users:
        if user['username'] == username:
            user.update(newData)
            saveDataToJson(users)
            break
            