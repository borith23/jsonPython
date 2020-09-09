import re

txt = "The rain in Spain"

#Check if "Portugal" is in the string:

x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")


txt = "The rain in Spain"
y = re.search("\s", txt)

print("The first white-space character is located in position:", y.start())


txt2 = "My name is Lunar"
z = re.split("\s", txt2)
z1 = re.split("\s", txt2, 1)
print(z)
print(z1)

a = re.sub("\s", "9", txt2)
print(a)
b = re.sub("\s", "10", txt2, 2)
print(b)
