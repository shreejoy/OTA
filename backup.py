from github import Github
import pymongo, json

EDITION = 'NORMAL'
FILENAME = 'build.json'
REPO = 'PixysOS-Devices/official_devices'
BRANCH = 'master'
VERSION_CODE = 'ten'

try:
    DEVICES_JSON = json.loads(auth.get_repo('PixysOS-Devices/official_devices').get_contents(path="devices.json", ref="ten").decoded_content)
except:
    print('Error loading json')
    
codenames = []
for DEVICE_JSON in DEVICES_JSON:
    codename = DEVICE_JSON['codename']
    codenames.append(codename)
 
official_builds = auth.get_repo(REPO).get_branch(BRANCH)
for codename in codenames:
    path = codename + '/' + FILENAME
    content official_builds.get_content(path=path).decoded_content
    try:
        content = json.loads(content)
    break:
        print(codename + ' build json is wrong')
        break
    build = {}
    response = content['response'] 
    build['filename'] = response['filename']
    build['md5'] = response['id']
    build['size'] = response['size']
    build['url'] = response['url']
    build['version'] = 
    build['edition'] = EDITION
    build['version_code'] = VERSION_CODE
    
    
