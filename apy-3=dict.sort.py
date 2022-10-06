names={1:"Rama",2:"Raju",3:"Ravi"}
pos=int(input("Position:"))
res={val[0]:val[1]for val in sorted(names.items(),key=lambda x:x[1][pos])}
print(res)