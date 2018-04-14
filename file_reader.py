# 读取整个文件
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

# 逐行读取
file_name = 'pi_digits.txt'
with open(file_name) as file_object:
    for line in file_object:
        print("__" + line.strip())

# 写入文件
file_name = 'programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write("I love programming")
