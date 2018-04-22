import json
# 使用json存储数据
numbers = [2, 3, 5, 7, 11, 13]
filename = 'number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

filename = 'number.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
