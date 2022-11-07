# ФАЙЛЫ
# f = open('file_location', 'open_method')
# r - на чтение
# w - содерж удал или созд нов файл
# a - на дозапись
# t - текст. режим
# + - чтение и запись
f = open('First-Project/Seventh-text.txt', 'w')
f.write('create new file!' + '\n')
f.close()


added_text = input('Введите текст:')
f = open('First-Project/Seventh-text.txt', 'a')
f.write(added_text + '\n')
f.close()


# It's working too.
f = open('First-Project/Seventh-text.txt', 'a')
f.write(input('Введите текст:') + '\n')
f.close()


f = open('First-Project/Seventh-text.txt', 'r')
# f.read(кол-во символов, если пусто, то выведет все)
# print(f.read())
# для построчного счит
for line in f:
    print(line) # разрыв при выводе, тк испльз метод \n
f.close()