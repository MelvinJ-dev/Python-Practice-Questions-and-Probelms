
# Simple password Cracker
## Works only in a perfect ascending order


password = [1,2,3,43,75,84,89]

length = len(password)
new_lst = []                                                        
for i in range(length):
    j=0
    for j in range(100):
        if(password[i]==j):
            new_lst.append(j)
print(new_lst)

# while loop


sp = [
    "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", 
    "-", "_", "=", "+", "{", "}", "[", "]", ":", ";", 
    "\"", "'", "<", ">", ",", ".", "?", "/", "\\", "|", "~","()"
]
i=0
s=0
nw_lst = []
j=0
k=0
passwords = [1,2,3,43,75,84,89,'@',"'",",","()"]
lenght = len(passwords)
sp_length = len(sp)

while True:
    if(type(passwords[i])==int):
        if(len(nw_lst)>=lenght):
            break
        else:
            if(passwords[j]==k):
                nw_lst.append(k)
                j+=1
                i+=1
            else:
                k+=1                
    else:
        if(len(nw_lst)>=lenght):
            break
        else:
            if(s<=sp_length-1):
                if(passwords[j]==sp[s]):
                    nw_lst.append(sp[s])
                    j+=1
                else:
                    s+=1
            else:
                break
print(nw_lst)                       

           



