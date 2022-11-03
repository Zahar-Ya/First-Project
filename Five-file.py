# МНОЖЕСТВО
# множества не содержат повт. эл-ов и все эл-ы в случ порядке
a = set('hello')
print(a)
b = {1,2,3,4,3} # если прописывать только ключи, то создается множество
print(b)
# a.add(90) - add one element
# a.update([True, 'c', 8,1,1]) - add many elements
# a.remove(item) - delete element, that = item
# a.pop() - delete the first element
# a.clear() - clear set
n = [1,1,1,2,3,3]
new_n = set(n)