
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
# message=input("please unput some message")
# print(message)
# 输入python2
# message=raw_input("please unput some message")
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

 # 函数
 # 定义函数


def greet_user(username):
    """显示简单问候语"""
    print("Hello!" + username)


greet_user("Tom")

# 让实参变为可选参数


def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的名字"""
    if middle_name:
        full_name = first_name + '' + middle_name + '' + last_name
    else:
        full_name = first_name + '' + last_name
    return full_name.title()


musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'mike', 'james')
print(musician)

# 传递列表


def greet_users(names):
    """向列表中的每位用户发送问候"""
    for name in names:
        mes = "Hello " + name.title() + "!"
        print(mes)


usernames = ['james', 'kd', 'curry']
greet_users(usernames)

# 传递任意数量的实参


def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字实参


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein', location='physics')
print(user_profile)


# 类
# 创建dog类
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性的name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name + " rolled over!")


# 创建类的实例
my_dog = Dog('willie', 6)
print("my dog name is " + my_dog.name)
print("age is " + str(my_dog.age))
my_dog.roll_over()
my_dog.sit()

# car类


class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的信息描述"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def update_odometer(self, milleage):
        if milleage >= self.odometer_reading:
            self.odometer_reading = milleage
        else:
            print("You can not roll back an odometer!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())


class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# 
