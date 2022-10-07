s=input("Enter a string:")
d={}
if s.isspace():
    print("String is Empty")
elif s.isdigit():
    print("Enter characters only")
else:
    for i in s:
        d[i]=s.count(i)
    print(d)
    
    
"""
Output:
i.  Enter a string:hello
    {'h': 1, 'e': 1, 'l': 2, 'o': 1}
ii. Enter a string:likith kiran singh
    {'l': 1, 'i': 4, 'k': 2, 't': 1, 'h': 2, ' ': 2, 'r': 1, 'a': 1, 'n': 2, 's': 1, 'g': 1}   
iii. Enter a string:21bq1a4220
    {'2': 3, '1': 2, 'b': 1, 'q': 1, 'a': 1, '4': 1, '0': 1}
iv. Enter a string:56444
    Enter characters only
"""
