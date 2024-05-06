s=input()
voules = ['a', 'e', 'i', 'o', 'u', 'y']
ind = []
for i in range(len(s)):
    if s[i].lower() in voules:
        ind.append(i+1)
n=0
_max=0
ind.append(len(s)+1)
for i in range(len(ind)):
    if i==0:
        x= ind[i]
        _max = max(_max, x)
        continue
    x= ind[i] - ind[n]
    _max = max(_max, x)
    n+=1
 
print(_max)