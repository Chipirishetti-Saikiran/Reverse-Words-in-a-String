s = "  hello world  "
l=list(map(str,s.split(" ")))
print(l)
l=l[::-1]
l = [item for item in l if item.strip()]
print(l)
st=""
for i in l:
    st+=str(i)+" "
print(st)    
