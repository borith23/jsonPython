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