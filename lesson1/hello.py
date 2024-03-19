last_name = input('Введите вашу фамилию: ')
first_name = input('Введите ваше имя: ')
name = first_name + ' ' + last_name
full_name = name.title()
message = "Hello, " + full_name + "!"
if full_name == 'Roman Rzyanin':
    print(message)
else:
    print('Идите на куй, я вас не знаю!')