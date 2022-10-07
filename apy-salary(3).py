n=int(input("Enter no of employees:"))
l=[]
bonus=100
total=0
names=[]
print("------------------------------------------")
for i in range(n):
    name=input("Enter Employeee Name:")
    names.append(name)
    sal=int(input("Enter Employee Salary:"))
    l.append(sal)
    emp_id=input("Enter Employee id:")
    exp=int(input("Enter Employee Experience:"))
    if exp<=2:
        print("No Bonus")
    else:
        net_sal=sal+bonus
        print("Net salary of the employee is ",net_sal)
    print("------------------------------------------")
print("Name : Salary")
for i in range (n):
    print(names[i],":",l[i])
l=sorted(l)
print("Highest Salary :",l[-1])
print("Lowest Salary :",l[0])

for i in range(n):
    total=total+l[i]
Avg=total/n
print("Avg Salary is ",Avg)