thistuple = tuple(("apple", "banana", "cherry"))
print(len(thistuple))

a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


