word=input("Enter a word or a sentence:")
vowels=('a','e','i','o','u','A','E','I','O','U')
count=0
for v in vowels:
    if v in word:
        count=count+1
if count>=5:
    print("Sentence has all vowles")
else:
    print("sentence does not have all the vowels")
