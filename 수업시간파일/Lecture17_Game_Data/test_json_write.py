# json으로 직렬화
import json

data = {'x' : 10, 'y' : 20, 'size' : 1.5}
with open('data.json', 'w') as f:  #close 안써도 자동으로 꺼짐
    json.dump(data, f)