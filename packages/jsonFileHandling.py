import json

def jsonFileCheck(fileName = 'users.json'):
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            # get json file content
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
            # get json file content
            content = file.read().strip()
            # if content not existing
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
    # get 'users' array from json file
    users = readJsonFile()
    
    for user in users:
        # if matching usename
        if user['username'] == username:
            # update 'users' array
            user.update(newData)
            
            # overwrite 'users' array in json file then exit
            saveDataToJson(users)
            break
            