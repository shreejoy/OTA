from github import Github
import pymongo, json, requests

EDITION = 'NORMAL'
FILENAME = 'build.json'
REPO = 'PixysOS-Devices/official_devices'
BRANCH = 'master'
VERSION_CODE = 'ten'
MONGO_AUTH_URI = ''
MONGO_INIT = pymongo.MongoClient(MONGO_AUTH_URI)
DB = MONGO_INIT['PixysOS']
COLLECTION = DB['builds']

auth = Github('shreejoy')

try:
    DEVICES_JSON = json.loads(auth.get_repo('PixysOS/official_devices').get_contents(path="devices.json", ref="ten").decoded_content)
except:
    print('Error loading json')
    
codenames = []
for DEVICE_JSON in DEVICES_JSON:
    codename = DEVICE_JSON['codename']
    codenames.append(codename)
 
official_builds = auth.get_repo(REPO)
for codename in codenames:
    path = codename + '/' + FILENAME
    #content  = official_builds.get_contents(path=path, ref="ten").decoded_content
    try:
        content  = official_builds.get_contents(path=path, ref="ten").decoded_content
        content = json.loads(content)
    except:
        print(codename + ' build json is wrong')
        continue
    build = {}
    response = content['response'][0]
    build['filename'] = response['filename']
    build['md5'] = response['id']
    build['size'] = response['size']
    build['version'] = response['version']
    build['device'] = codename
    build['edition'] = EDITION
    build['version_code'] = VERSION_CODE
    build['url'] = requests.get('https://get.pixys.tools/utils/crypto/' + build['device'] + '/' + build['version_code'] + '/' + build['filename']).text
    print(build)
    COLLECTION.insert_one(build)
