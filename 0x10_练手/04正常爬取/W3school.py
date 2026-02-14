import requests

url = "https://w3schools.tech/zh-cn/tutorial/batch-script/index"
response = requests.get(url)
print(response.text)