words=['Arun','Varun','Kent','Pot','net','Peak','Peacock','Zebra','Nato','Toe','Poke','Knife','Peot','Venus','Ant']
let=['A','K','E','O','T','P','N']
ans=[]
for w in words:
    count=0
    for l in let:
        if l in w.upper():
            count=count+1
    if count==len(w):
        ans.append(w)
print("Result:",ans)