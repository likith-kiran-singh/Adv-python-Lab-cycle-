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
"""
Output:
Enter no of employees:3
Enter Employeee Name:a
Enter Employee Salary:123
Enter Employee id:1
Enter Employee Experience:2
No Bonus
Enter Employeee Name:b
Enter Employee Salary:456
Enter Employee id:2
Enter Employee Experience:5
Net salary of the employee is  556
Enter Employeee Name:c
Enter Employee Salary:789
Enter Employee id:3
Enter Employee Experience:9
Net salary of the employee is  889
a : 123
b : 456
c : 789
Highest Salary : 789
Lowest Salary : 123
Avg Salary is  456.0
>>> %Run 'apy-salary(3).py'
Enter no of employees:5
------------------------------------------
Enter Employeee Name:abc
Enter Employee Salary:50000
Enter Employee id:sd49d84c
Enter Employee Experience:5
Net salary of the employee is  50100
------------------------------------------
Enter Employeee Name:def
Enter Employee Salary:600000
Enter Employee id:d6c51we
Enter Employee Experience:9
Net salary of the employee is  600100
------------------------------------------
Enter Employeee Name:ghi
Enter Employee Salary:75000
Enter Employee id:df65we5eth
Enter Employee Experience:2
No Bonus
------------------------------------------
Enter Employeee Name:jkl
Enter Employee Salary:29292
Enter Employee id:jjk55hj
Enter Employee Experience:3
Net salary of the employee is  29392
------------------------------------------
Enter Employeee Name:mno
Enter Employee Salary:98765
Enter Employee id:lkj6655
Enter Employee Experience:4
Net salary of the employee is  98865
------------------------------------------
Name : Salary
abc : 50000
def : 600000
ghi : 75000
jkl : 29292
mno : 98765
Highest Salary : 600000
Lowest Salary : 29292
Avg Salary is  170611.4"""
