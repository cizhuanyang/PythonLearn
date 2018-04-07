
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
#创建数值列表
for value in range(1,5):
	print(value)