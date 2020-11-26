import requests


file_ob = {'File': open(r'D:\11.txt', 'rb')}
print(file_ob)
payload = {
    'Remark1': 'hey',
    'Remark2': 'hello',
}

headers = {
  'Content-Type': 'application/json'
}
r = requests.post("http://127.0.0.1:8080/api/7zfile/upload/", data=payload, headers=headers)

print(r.status_code)