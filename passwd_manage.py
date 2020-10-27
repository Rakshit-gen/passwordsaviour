import mysql.connector as msq
import random
k=[]
for x in range(65,91):
    w=chr(x)
    k.append(w)
print('Welcome to MyPass')
def show():
    print('What would you like to do?')
    print('1.Create a Password')
    print('2.Save a Password')
    print('3.Ask a password')
    while True:
        try:
            w=int(input('Enter your choice in the form of integer:'))
            if w==1:
                create_pass(k)
            if w==2:
                save_pass()
            
            if w==3:
                show_passwd()
            if w==4:
                showall()
            break
        except Exception as e:
            print(e)
            print('*********Error*********')
            print('*********Try Again*********')
def create_pass(k):
    while True:
        p=''
        for e in range(1,9):
            w=random.randint(0,25)
            p=p+k[w]
        print('Newly generated password is',p)
        q=input('Do you liked it y/n')
        if q=='y':
            yop=input('press s to save it')
            if yop=='s':
                save_pass()
                break
            else:
                show()
            return p
            break
        else:
            pass
        
def save_pass():
    a=str(input('Please Type your Password'))
    b=str(input('Please Type your Website'))
    a='"'+a+'"'
    b='"'+b+'"'
    pi='insert into passwd(website, password) values('+a+','+b+');'
    mycon=msq.connect(host='localhost',user='root',passwd='root')
    try:
        r=mycon.cursor()
        r.execute('use passwds')
        r.execute(pi)
        mycon.commit()
        print('Password',a,'saved for',b)
        show()
    
    except Exception as e:
        print(e)
        show()

def show_passwd():
    k=input('Enter your passwd')
    if k=='hello':
        y=input('Enter website name')
        y='"'+y+'"'
        mn='select * from passwd where password=' + y
        mycon=msq.connect(host='localhost',user='root',passwd='root')
        r=mycon.cursor(mn)
        r.execute('use passwds')
        p=r.execute(mn)
        data=r.fetchone()
        print(data)
        show()
    else:
        print('Wrong Password')
        
def showall():
    mp=input('You First Need To Enter Your Password')
    k=mp.encode('utf16')
    k=str(k)
    k='"'+k+'"'
    p=len(k)
    print(k[2:p-1:])
    mn='\xff\xfer\x00a\x00b\x00b\x00i\x00t\x00'
    if k[2:p-1:]==mn:
        print('ok')
    mycon=msq.connect(host='localhost',user='root',passwd='root')
    r=mycon.cursor()
    r.execute('use passwds')
    r.execute('select * from passwd')
    
    data=r.fetchall()
    print(data)    
    
if '__main__'==__name__:
    while True:
        show()
        
