import json

#Json
x = '{"name":"Rith", "age":21, "gender":"Male", "major":"WEP Programing"}'
#Use json.loads for convert json to python
y = json.loads(x) 
print(y["name"]) 
print(y["major"])


#Convert pytho to json 
i = {
    "name":"Rith", 
    "age":21, 
    "gender":"Male", 
    "major":"WEP Programing"
    } #Array dict

#Use json.dumps() for convert python to json
#use indent=4 to make it easier to read the result
j = json.dumps(i, indent=4) 
print(j)


#Use the separators parameter to change the default separator:
#Use . and space to separate objects
#Use = and space to separate keys from their values
print(json.dumps(i, indent=4, separators=(". ", " = ")))

#Use the sort_keys to display alphabetically result (a, b, c ...)
print(json.dumps(i, indent=4, sort_keys=True))