#Use try for prevent code that has error or block code that errors
#If try block don't have error code it will print try block
try:
    print(v)
except:
    print("hello")

#Use NameError it will print NameError block
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")


#Use else when try block is true and then it will print try block and else block
#If try block error it will display except block
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")



#The finally block gets executed no matter if the try block raises any errors or not:
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


#Try block will raise an error when trying to a read-only file
try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
