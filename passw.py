import random
import os
a=[]
p=[]
for x in range(65,91):
    s=chr(x)
    a.append(s)
while True:
    for y in range(8):
        q=random.randint(0,8)
        p.append(a[q])
    p=''.join(p)
    print(p)
    s=input('Do you like it y/n')
    if s=='y':
        k=input('Website Name')
        tr=os.listdir()
        if k in tr:
            print('file already exists')
            s=input('Do you want to save new password y/n')
            if s=='y':
                os.remove(k)
                st=open(k,'w')
                st.write(p)
                st.write('/')
                st.write(k)
                st.close()
            else:
                pass
        w=open(k,'w')
        w.write(p)
        w.write('/')
        w.write(k)
        w.close()
        o=open(k,'r')
        print(o.read())
        o.close()
        break
    else:
        re=input('Enter your password')
        we=input('Website')
        st=open(we,'w')
        st.write(re)
        st.write('/')
        st.write(we)
        st.close()
        break
        
        pass
