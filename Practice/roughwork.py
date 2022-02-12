from cgi import test


empty_tuple = ()
print(type(empty_tuple))

test1 = 1,2,3,4
test2 = 1,

print(test1)
print(test2)

print("Working With Turple Unpacking")
survey = (21, "Switzerland", 'False')
age, country, knows_python = survey

print("Age =", age)
print("Country =", country)
print("Know_Pyton =", knows_python)