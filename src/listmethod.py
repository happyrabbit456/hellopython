a = ["bee", "moth"]
print(a)
a.append("ant")
print(a)

a = ["bee", "moth"]
print(a)
a.extend(["ant", "fly"])
print(a)

# Result
# ['bee', 'moth']
# ['bee', 'moth', 'ant', 'fly']

a = ["bee", "moth"]
print(a)
a.insert(0, "ant")
print(a)
a.insert(2, "fly")
print(a)

a = ["bee", "moth", "ant"]
print(a)
a.remove("moth")
print(a)

# Example 1: No index specified
a = ["bee", "moth", "ant"]
print(a)
a.pop()
print(a)

# Example 2: Index specified
a = ["bee", "moth", "ant"]
print(a)
a.pop(1)
print(a)
# Result
# ['bee', 'moth', 'ant']
# ['bee', 'moth']
# ['bee', 'moth', 'ant']
# ['bee', 'ant']

a = ["bee", "moth", "ant"]
print(a)
a.clear()
print(a)

a = ["bee", "ant", "moth", "ant"]
print(a.index("ant"))
print(a.index("ant", 2))
# Result
# 1
# 3

a = ["bee", "ant", "moth", "ant"]
print(a.count("bee"))
print(a.count("ant"))
print(a.count(""))
# Result
# 1
# 2
# 0

# sort(key=None, reverse=False)
a = [3,6,5,2,4,1]
a.sort()
print(a)

a = [3,6,5,2,4,1]
a.sort(reverse=True)
print(a)

a = ["bee", "wasp", "moth", "ant"]
a.sort()
print(a)

a = ["bee", "wasp", "butterfly"]
a.sort(key=len)
print(a)

a = ["bee", "wasp", "butterfly"]
a.sort(key=len, reverse=True)
print(a)

# Result
# [1, 2, 3, 4, 5, 6]
# [6, 5, 4, 3, 2, 1]
# ['ant', 'bee', 'moth', 'wasp']
# ['bee', 'wasp', 'butterfly']
# ['butterfly', 'wasp', 'bee']


a = [3,6,5,2,4,1]
a.reverse()
print(a)

a = ["bee", "wasp", "moth", "ant"]
a.reverse()
print(a)

# Result
# [1, 4, 2, 5, 6, 3]
# ['ant', 'moth', 'wasp', 'bee']
#


# WITHOUT copy()
a = ["bee", "wasp", "moth"]
b = a
b.append("ant")
print(a)
print(b)

# WITH copy()
a = ["bee", "wasp", "moth"]
b = a.copy()
b.append("ant")
print(a)
print(b)

# Result
# ['bee', 'wasp', 'moth', 'ant']
# ['bee', 'wasp', 'moth', 'ant']
# ['bee', 'wasp', 'moth']
# ['bee', 'wasp', 'moth', 'ant']

a = ["bee", "moth", "ant"]
print(len(a))
# Result
# 3

print(list())
print(list([]))
print(list(["bee", "moth", "ant"]))
print(list([["bee", "moth"], ["ant"]]))

a = "bee"
print(list(a))

a = ("I", "am", "a", "tuple")
print(list(a))

a = {"I", "am", "a", "set"}
print(list(a))

# Result
# []
# []
# ['bee', 'moth', 'ant']
# [['bee', 'moth'], ['ant']]
# ['b', 'e', 'e']
# ['I', 'am', 'a', 'tuple']
# ['am', 'I', 'a', 'set']

a = ["bee", "moth", "ant"]
print(max(a))

a = ["bee", "moth", "wasp"]
print(max(a))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]
print(max(a, b))

# Result
# moth
# wasp
# [1, 2, 3, 4, 5]

a = ["bee", "moth", "wasp"]
print(min(a))

a = ["bee", "moth", "ant"]
print(min(a))

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4]
print(min(a, b))

# Result
# bee
# ant
# [1, 2, 3, 4]

print(list(range(10)))
print(list(range(1,11)))
print(list(range(51,56)))
print(list(range(1,11,2)))

# Result
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [51, 52, 53, 54, 55]
# [1, 3, 5, 7, 9]