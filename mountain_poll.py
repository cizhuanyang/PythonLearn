# coding=utf-8
# 使用用户输入来填充字典
responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
    # 提示输入名字和回答
    name = input("what is your name?")
    response = input("which mountain would you like to climb")
    # 将答案存储于字典中
    responses[name] = response
    # 看看是否还有人参与调查
    repeat = input("would you like to let another person respond")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print(responses)
print("\n---Poll Result")
for name, response in responses.items():
    print(name + "would you like to climb " + response + ".")
