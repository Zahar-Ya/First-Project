# ФУНКЦИИ
# def Func_name(parametr_name):
#     print('c')
# Func_name(1)
# def sum_f(a, b):
#     res = a + b
#     return res
# res = sum_f(1, 3)
# print(res)     
# print(sum_f(1, 3))


def b(g):
    el_max = g[0]
    for el in g:
        if el_max < el: el_max = el
    return el_max    
h = [2, 3, 4]
h.append(9)
print(b(h))


# Лямбда функции
func = lambda x, y: x+y
print(func(3, 8))