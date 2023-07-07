import json

data_reg = {}
with open('reg1.json', 'w') as f:
    json.dump(data_reg, f)


def register(login, passwd):
    with open('reg1.json', 'r') as f:
        data_reg = json.load(f)
    if login not in data_reg.keys():
        data_reg[login] = passwd
        with open('reg1.json', 'w') as f:
            json.dump(data_reg, f)
        print('Успешная регистрация')
    else:
        print('Этот логин уже занят')


def login_function(login, passwd):
    with open('reg1.json', 'r') as f:
        data_reg = json.load(f)
    if login in data_reg.keys():
        if data_reg[login] == passwd:
            print('Успешный вход')
    else:
        print('Неверный логин или пароль')


while True:
    q1 = input('Вход или регистрация')
    if q1 == 'регистрация':
        register(input('логин'), input('пароль'))
    elif q1 == 'вход':
        login_function(input('логин'), input('пароль'))
    s = input('Хотите закончить?')
    if s == 'да':
        break
