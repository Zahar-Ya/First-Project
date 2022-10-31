print('Hello World')
print('Отлично получается')
# чтобы прокоментировать сразу много: Ctrl + /
# nm = [] - список(массив)
# nm.append(элемент который добавить)
# nm.insert(№ позиции, что вставить)
# nm.extend(вставка массива)
# .sort()
# .reverse()
# .pop(индекс удаляемого эл)
# .remove(какой эл удалить, не индекс, а чему равен)
# .clear() 
# .count(какой эл)
l = int(input('lengh '))
i = 0
user = []
while i<l:
    i+=1
    user.append(input('введите элемент '))
print(user)
