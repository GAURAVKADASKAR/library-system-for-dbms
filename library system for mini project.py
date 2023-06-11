import mysql.connector as g
con=g.connect(host='localhost',user='root',password='root',database='dbms')
def addbook():
    bname=input("ENTER THE BOOK NAME : ")
    bc=input("ENTER THE BOOK CODE : ")
    to=input("TOTAL NUMBER OF BOOK'S : ")
    sub=input("ENTER THE SUBJECT : ")
    tt=(bname,bc,to,sub)
    data="insert into book values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(data,tt)
    con.commit()
    print("--------------------BOOK ENTERED SUCCESSFULLY--------------------")
    main()
def issuebook():
    sname=input("ENTER YOUR NAME : ")
    enum=input("ENTER YOUR ENROLLMENT NUMBER : ")
    sbc=input("ENTER THE BOOK CODE TO ISSUE : ")
    idate=input("ENTER THE ISSUE DATE : ")
    dd=(sname,enum,sbc,idate)
    a="insert into issue values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(a,dd)
    con.commit()
    print("--------------------BOOK ISSUED SUCCESSFULLY--------------------")
    print("BOOK ISSUED TO ",sname)
    rebook(co,-1)
def returnbook():
    sname=input("ENTER YOUR NAME : ")
    enum=input("ENTER YOUR ENROLLMENT NUMBER : ")
    sbc=input("ENTER THE BOOK CODE: ")
    rdate=input("ENTER THE RETURN DATE : ")
    pp=(sname,enum,sbc,rdate)
    aaa="insert into submit values(%s,%s,%s,%s)"
    c=con.cursor()
    c.execute(aaa,pp)
    con.commit()
    print("--------------------BOOK RETURN SUCCESSFULLY--------------------")
    rebook(co,1)
def rebook(co,n):
    a="select total from book where bcode=%s"
    data=(co,)
    c=con.cursor()
    c.execute(a,data)
    result=c.fetchone()
    t=result[0]+n
    ss="update book set total=%s where bcode=%s"
    d=(t,ss)
    c.execute(ss,d)
    con.commit()
    main()

def delbook():
    bbc=input("ENTER THE BOOK CODE TO DELETE : ")
    a="delete from book where bcode=%s"
    dd=(bbc,)
    c=con.cursor()
    c.execute(a,dd)
    con.commit()
    main()
def disbook():
    a="select * from book"
    c=con.cursor()
    c.execute(a)
    result=c.fetchall()
    for i in result:
        print("BOOOK NAME : ",i[0])
        print("BOOK CODE : ",i[1])
        print("TOTAL : ",i[2])
        print("SUBJECT : ",i[3])
        print("----------------------------------------------------------------")
    main()
def main():
    while(1):
        print("--------------------WELCOME TO LIBRARY SYSTEM--------------------")
        print("1.ADD BOOK'S TO DATA")
        print("2.ISSUE BOOK'S")
        print("3.RETURN BOOK")
        print("4.DELETE BOOK'S FROM DATA")
        print("5.DISPLAY ALL BOOK'S")
        print("6.EXIT")
        choice=int(input("ENTER YOUR CHOICE : "))
        if choice==1:
            addbook()
        if choice==2:
            issuebook()
        if choice==3:
            returnbook()
        if choice==4:
            delbook()
        if choice==5:
            disbook()
        if choice==6:
            quit()
        else:
            print("incorrect choice")
            main()
def pas():
    pa=input("ENTER THE PASSWORD : ")
    if pa=='LMS' or pa=='lms':
        main()
    else:
        print("wrong password : ")
        pas()

pas()

        
        
