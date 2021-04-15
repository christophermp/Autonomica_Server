import requests
import json
from .models import Task

def taskParser(screen_pk):


    url = 'http://10.0.0.111:8090/getconfiguration'
    # connection = sqlite3.connect("../db.sqlite3")
    # cursor = connection.cursor()

    read_content = json.loads(requests.get(url).text)

    #with open('./json.json') as access_json:
    # read_content = json.load(access_json)
    #print(type(read_content))
    #print(read_content)
    workspaceAccess = read_content['workspaces'][0]['tasks']
    workspaceName = read_content['workspaces'][0]['name']
    workspaceVersion = read_content['workspaces'][0]['version']
    workspaceEnabled = read_content['workspaces'][0]['enabled']
    workspaceLastModified = read_content['workspaces'][0]['lastModifiedTime']
    #print(type(workspaceAccess))
    print(workspaceName)
    print(workspaceEnabled)
    print(workspaceVersion)
    print(workspaceLastModified)

    #print(workspaceAccess[4]['name'], workspaceAccess[4]['devicesReferenced'][0]['type'])

    for questionData in workspaceAccess:
        #print(questionData)
        repliesData = questionData['devicesReferenced']
        repliesName = questionData['name']
        #print(repliesData)
        #print(repliesName)
        for data in repliesData:
            #print('Task Name: ', questionData['name'])
            name = data['name']
            message = data['message']
            type = data['type']
            print('Name and info: ', questionData['name'], name, message, type)
            task = Task(screen_id=screen_pk, task_name = questionData['name'],
                           version = workspaceVersion, modified = workspaceLastModified, macro_name = questionData['name'],
                           device = name, type = type, message = message)
            task.save()