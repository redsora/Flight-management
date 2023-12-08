import sqlite3
import mysql.connector
#_______mysql connector package
obj=mysql.connector.connect(host="localhost",user="root",passwd="admin")
#here obj is connection object
#CREATING DATABASE & TABLE
mycursor=obj.cursor()
 
#________cursor is used to row by row processing of record in the resultset
 
mycursor.execute("create database if not exists airlines") 
#______mycursor is cursor objec







#CREATING DATABASE
# mycursor.execute(“create database if not exists airlines”)
mycursor.execute("use airlines")




#CREATING TABLE FOR ODER FOOD
mycursor.execute("create table if not exists food_items(sl_no int(4) auto_increment primary key,food_name varchar(40)not null,price int(4) not null)")
mycursor.execute("insert into food_items values({},'{}',{})".format('null','pepsi',150))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','coffee',70))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','tea',50))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','water',60))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','milk shake',80))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','chicken burger',160))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','cheese pizza',70))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','chicken biryani',300))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','plane rice',80))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','aloo paratha',120))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','roti sabji',100))
mycursor.execute("insert into food_items values({},'{}',{})".format('null','omelette',50))




#CREATING TABLE FOR LUGGAGE ENTRY
mycursor.execute("create table if not exists luggage(luggage_id int(4) auto_increment primary key,weight int(3)not null,price int(4) not null)")


#CREATING TABLE FOR CUSTOMER DETAILS
mycursor.execute("create table if not exists cust_details(cust_id int(4) auto_increment primary key,cust_name varchar(40)not null,cont_no bigint(10) not null)")


#CREATING TABLE FOR CUSTOMER'S FLIGHT DETAILS
mycursor.execute("create table if not exists flight_details(cus_id int(4),cus_name varchar(40)not null,flight_id)")
obj.commit() 


#TO ENTER THE DETAILS OF LUGGAGE
def luggage():
    print("what do you want to do?")
    print("1. add luggage")
    print("2. delete luggage")
    x=int(input("enter your choice: "))
    if x==1:
        lname=input("enter luggage type: ")
        mycursor.execute("insert into luggage values({},'{}'".format('null',lname))

    elif x==2:
        lid=int(input("enter your luggage id: "))
        mycursor.execute("delete from luggage where luggage_id={}".format(lid))
        
    else:
        print(" **************** PLEASE ENTER A VALID OPTION **************************** ")
        food()
    obj.commit() 



#TO UPDATE THE INFORMATION OF FOOD DETAILS
def food():
    print("what do you want to do?")
    print("1. add new items")
    print("2. update price")
    print("3. delete items")
    x=int(input("enter your choice: "))
    if x==1:
        fname=input("enter food name: ")
        fprice=int(input("enter food price: "))
        mycursor.execute("insert into food_items values({},'{}',{}".format('null',fname,fprice))
    elif x==2:
        fid=int(input("enter food id: "))
        fprice=int(input("enter new price: "))
        mycursor.execute("update food_items set price={} where food_id={}".format(fid,fprice))
    elif x==3:
        fid=int(input("enter food id: "))
        mycursor.execute("delete from food_items where where food_id={}".format(fid))
    else:
        print(" **************** PLEASE ENTER A VALID OPTION **************************** ")
        food()
    obj.commit()






#TO UPDATE THE INFORMATION OF CLASSTYPE
def classtype():
    print("what do you wat to do? ")
    print("1. change the classtype name")
    print("2. change the price of classtype")
    x=int(input("enter your choice: "))
    if x==1:
        oname=input("enter old name: ")
        nname=input("enter new name: ")
        mycursor.execute("update classtype set '{}'='{}'".format(oname,nname))
        
def fooditems():
    print(" ")
    print(" ")

    print(" THE AVAILABLE FOODS ARE: ")
    print(" ")
    print(" ")
    mycursor.execute("select * from food_items")
    x=mycursor.fetchall()
    for i in x:
        print(" FOOD ID: ",i[0])
        print(" FOOD Name: ",i[1])
        print(" PRICE: ",i[2])

    print("__________________________________________________________________________________________")
    user()



#Admin Interface after verifying password
def admin1():
    print("************ WHAT'S YOUR TODAYS GOAL? ****************")
    print("1. update details")
    print("2. show details")
    print("3. job approval")
    x=int(input("select your choice: "))
    while True:
        if x==1:
            print("1. classtype")
            print("2. food")
            print("3. luggage")
            x1=int(input("enter your choice"))
            if x1==1:
                classtype()
            elif x1==2:
                food()
            elif x1==3:
                luggage()
            else:
                print(" ********************** PLEASE ENTER A VALID OPTION ******************************** ")
                admin1()
                
            
        elif x==2:
            print("1. classtype")
            print("2. food")
            print("3. luggage")
            print("4. records")
            y=int(input("from which table: "))
            if y==1:
                mycursor.execute("select * from classtype")
        else:
            mycursor.execute("select * from customer_details")
            z=mycursor.fetchall()
            for i in z:
                print(i)
            print("**************** THESE ABOVE PEOPLE HAVE BOOKED TICKET *****************************")
            break


#Admin Interface
def admin():
    while True:
        sec=input("enter the password: ")
        if sec=="admin":
            admin1()
        else:
            print("************YOUR PASSWORD IS INCORRECT*********")
            print("***********PLEASE TRY AGAIN*****************")
            admin()
        break



#TO SEE THE RECORDS OF THE CUSTOMER
def record():
    cid=int(input("enter your customer id: "))
    mycursor.execute(" select * from customer_details where cus_id={}".format(cid))
    d=mycursor.fetchall()

    print("YOUR DETAILS ARE HERE...........")
    print("customer id: ",d[0])
    print("name: ",d[1])
    print("mobile number: ",d[2])
    print("flight id: ",d[3])
    print("flight name",d[4])
    print("classtype: ",d[5])
    print("departure place",d[6])
    print("destination",d[7])
    print("flight day: ",d[8])
    print("flight time: ",d[9])
    print("price of ticket: ",d[10])
    print("date of booking ticket: ",d[11])



#TO BOOK THE TICKETS
def ticketbooking():
    cname=input("enter your name: ")
    cmob=int(input("enter your mobileno: "))
    if cmob==0000000000:
        print(" MOBILE NUMBER CANT BE NULL ")
        ticketbooking()
        fid=int(input("enter flight id: "))
        fcl=input("enter your class: ")
        fname=input("enter your flight name")
        dept=input("enter departure place: ")
        dest=input("enter destination: ")
        fday=input("enter flight day: ")
        ftime=input("enter flight time: ")
        fprice=input("enter ticket rate: ")
        mycursor.execute("insert into customer_details values({},'{}',{},{},'{}','{}','{}','{}','{}','{}',{}".format('null',cname,cmob,fid,fname,fcl,dept,dest,fday,ftime,"curdate()"))
        obj.commit()



#TO SEE THE AVAILABLE FLIGHTS
def flightavailable():
    print(" ")
    print(" ")

    print(" THE AVAILABLE FLIGHTS ARE: ")
    print(" ")
    print(" ")
    mycursor.execute("select * from flight_details")
    x=mycursor.fetchall()
    for i in x:
        print(" ")
        print(" Flight ID: ",i[0])
        print(" Flight Name: ",i[1])
        print(" departure: ",i[2])
        print(" Destination: ",i[3])
        print(" Take off Day: ",i[4])
        print(" Take off time : ",i[5])
        print(" bussiness : ",i[6])
        print(" middle : ",i[7])
        print(" economic : ",i[8])

        print("__________________________________________________________________________________________")

    user()



#USER INTERFACE
def user():
    while True:
        print("************** MAY I HELP YOU? *****************")
        print("1. flight details")
        print("2. food details")
        print("3. book ticket")
        print("4. my details")
        print("5. exit")
        x=int(input("enter your choice: "))
        if x==1:
            flightavailable()
        elif x==2:
            fooditems()
        elif x==3:
            ticketbooking()
        elif x==4:
            records()
        else:
            print("************ PLEASE CHOOSE A CORRECT OPTION ************")
            user()
        break
    print("****************** WELCOME TO LAMNIO AIRLINES  **********************")
    print("************ MAKE YOUR JOURNEY SUCCESS WITH US!  *****************")
    print(" ")
    print(" ")
    print(" ")
    print(" ")
    print(" ")

# user()




#Main Interface
def menu1():
    print("**************** YOUR DESIGNATION? *******************")
    print("1. admin")
    print("2. user")
    print("3. exit")
    x=int(input("choose a option: "))
    while True:
        if x==1:
            admin()
        elif x==2:
            user()
        else:
            print("************PLEASE CHOOSE A CORRECT OPTION******************")
            menu1()
        break
menu1()





















