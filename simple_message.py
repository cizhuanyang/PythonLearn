
# coding=utf-8
# 字符串
# 修改字符串的大小写
name = "abc lovelace"
print(name.title())
print(name.lower())
print(name.upper())
# 合并字符串
first_name = "abc"
last_name = "lovelace"
full_name = first_name + last_name
print(full_name)
# 使用制表符或换行符添加空白
print("Languages:\n\tJava\n\tC\n\tPython")
# 删除空白
favorite_language = "  Java  "
# 删除末尾空白
print("!" + favorite_language.rstrip() + "!")
# 删除开头空白favorite_language=favorite_language.lstrip()
print("!" + favorite_language.lstrip() + "!")
# 删除两端空白
favorite_language = favorite_language.strip()
print("!" + favorite_language.strip() + "!")
# python 2 中的print语句
name = "Eric"
print "Hello " + name + ",would you like to learn some Python today?"
# python 之禅
import this


# 列表
bicycles = ['trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
# 访问列表元素
print(bicycles[0].title())
# 在列表末尾插入元素
bicycles.append('mobike')
# 在列表中插入元素
bicycles.insert(0, '永久')
print(bicycles)
# 删除列表元素
bicycles.pop()
del bicycles[0]
print(bicycles)
# 弹出列表任意位置的元素
bicycles.pop(0)
bicycles.remove('redline')
print(bicycles)
# 组织列表
bicycles.sort()
# 遍历列表
NBAplayer = ['james', 'curry', 'cobe', 'wall']
for player in NBAplayer:
    print(player.title())
    print("maybe be the MVP")
print("these are my guess")
# 创建数值列表
for value in range(1, 5):
    print(value)
print(list(range(1, 11, 2)))
square = []
for value in range(1, 11):
    square.append(value**2)
print(square)
# 对数字列表进行简单的统计计算
digits = [1, 2, 3, 4, 5, 6, 7, 8]
print(min(digits))
print((max(digits)))
print(sum(digits))
# 列表解析
square = [value**2 for value in range(1, 11)]
print(square)
# 4.3使用for循环打印数字1~20
for value in range(1, 21):
    print(value)
# 4.4创建一个列表，包含数字1~1000000，再使用for循环打印这些数字
# million=[value for value in range(1,1000000)]
# for value in million:
# 	print(value)
# 4.5计算1~1000000的总和
million = [value for value in range(1, 1000001)]
print(min(million))
print(max(million))
print(sum(million))
# 4.9立方解析，使用列表解析生成一个列表，其中包含前十个整数的立方
cube = [value**3 for value in range(1, 11)]
print(cube)
# 列表切片
smartphone = ['iphone', 'smartisan', 'samsung', 'htc']
print(smartphone[1:3])
print(smartphone[:3])
print(smartphone[2:])
# 遍历切片
for phone in smartphone[:3]:
    print(phone.title())
smart_phone = smartphone
print(smart_phone)
# 复制列表
phone = smartphone[:]
phone.append('Nokia')
smartphone.append('sony')
print(phone)
print(smartphone)


# 元组
# 定义元组
dimension = (200, 50)
print(dimension[0])
print(dimension[1])
# 遍历元组中的所有值
for value in dimension:
    print(value)
# 修改元组变量
dimension = (300, 100)
for value in dimension:
    print(value)


# if语句
age = 12
if age > 18:
    print("you are old enough to vote")
else:
    print("sorry,you don't have right to vote")
# if-elif-else结构
if age < 4:
    print("<4")
elif age < 18:
    print("<18")
else:
    print(">18")
# 使用if语句处理列表
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry,we are out of green peppers right now")
    else:
        print("Adding  " + requested_topping + ".")


# 字典
# 一个简单的字典
alien0 = {'color': 'green', 'points': 5}
print(alien0['color'])
print(alien0['points'])
# 访问字典中的值
new_points = alien0['points']
print("you just earned " + str(new_points) + " points")
print(alien0)
# 添加键值对
alien0['x_position'] = 0
alien0['y_position'] = 25
print(alien0)
# 修改键值对
alien0['color'] = 'black'
print(alien0)
# 删除键值对
del alien0['points']
print(alien0)
# 遍历字典
for key, value in alien0.items():
    print("key: " + key)
    print("\tvalue：" + str(value))
# 遍历字典中的所有键
favorite_languages = {'jen': 'java',
                      'luna': 'C', 'peter': 'C#', 'john': 'python'}
for name in favorite_languages.keys():
    print("name:" + name)
# 遍历字典中的所有值
for language in favorite_languages.values():
    print(language)


# 嵌套
# 字典列表
alien_0 = {'color': 'red', 'points': 5}
alien_1 = {'color': 'green', 'points': 15}
alien_2 = {'color': 'yellow', 'points': 25}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 在字典中存储列表
pizza = {'crust': 'thick', 'toppings': ['mushrooms', 'extra cheese'], }
# 在字典中嵌套字典
users = {
    'aeinstein': {
        'first': 'elbert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}
for username, user_info in users.items():
    print("\nusername: " + username)
    full_name = user_info['first'] + user_info['last']
    location = user_info['location']
    print("\nfull_name: " + full_name.title())
    print("\tlocation: " + location.title())


# 输入和while循环
# 输入python3
#message=input("please unput some message")
# print(message)
# 输入python2
#message=raw_input("please unput some message")
# 使用int来获取数值输入
# age=raw_input("how old are you")
# age=int(age)
# 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
