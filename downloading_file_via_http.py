import requests
import os
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Example1.txt"
r=requests.get(url)
print(r.headers)
path=os.path.join(os.getcwd(),'Example1.txt')
with open(path,'wb') as f:
    f.write(r.content)

