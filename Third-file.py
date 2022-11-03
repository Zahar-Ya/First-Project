# СТРОКИ
F_str = 'Zahar'
S_str = 'Gold'
T_str = 'RuSSiA'
w = 'W,A,w'
t = [1, 2, 3, 5.5, 'Z']
# print(F_str.upper())
# (F_str.lower())
# (S_str.islower())
# (T_str.capitalize())
# (F_str.find('h'))
print(w.split(','))# разбивает строку на составляющие
d = w.split(',')
d[1] = d[1].lower()
print(d[1])
res = '.'.join(d)
print(res)

# print(F_str[1:])
# print(F_str[1::2])
# print(t[:2:2])
# print(t[::-1])

