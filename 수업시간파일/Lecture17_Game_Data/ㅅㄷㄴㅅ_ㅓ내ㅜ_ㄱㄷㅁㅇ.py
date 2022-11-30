import json

with open('data.json', 'r') as f:  #close 안써도 자동으로 꺼짐
    data = json.load(f)

print(data)