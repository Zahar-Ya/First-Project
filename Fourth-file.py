# КОРТЕЖ И СЛОВАРЬ
# tuple - картеж
a =[1,2,3]#список, больше памяти и можно изм эл-ты
b = (1,2,3)#картеж, меньше памяти, нельзя изм эл-ты
c = 1,2,3
d = 1, #картеж из одного эл-та
e = 'Zahar'
# u can use '.count(element)' and '.len()'
new_a = tuple(a)
new_e = tuple(e)
# print(b[2])
# print(c)
# print(new_a)
# print(new_e)


# Словарь - Dict {key: item, key1: item1}
User = {'name': 'Zahar', 'age': '18', 'country': 'Russsia'}
User1 = dict(name='Zahar')
# print(User['name'])
# print(User1['name'])
# print(User.items())
for i in User:  #выводит только ключи
    print(i)
for key, item in User.items():
    print(key, ' - ', item)
# User.pop(key) - удалит ключ с объектом
# User.popitem() - удаляет, но только последний элемент
# print(User.keys() or User.values()) - вывод ключей/значений
# User['age'] = 'new item'
a = {'a1':{'b1':{'c1':'d1', 'c2':'d2'},'b2':{'q':'o'}}, 'a2':{}}
print(a['a1']['b1']['c1'])