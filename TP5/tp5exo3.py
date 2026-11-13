string=input()
string2=str()
string=string.lower()
paly=True
for i in string:
    if i.isalpha():
        string2+=i

for i in range (len(string2)):
    if string2[i]!=string2[len(string2)-1-i]:
        paly=False

if paly:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")