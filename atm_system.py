money=0
def deposte():
    global money
    depo=int (input("enter thr amount you want to deposte"))
    money+=depo
def with_draw():
    global money
    WD=int(input("enter the amount you want to with draw"))
    if WD>money:
        print ("you balance is in sufficent")
    else:
        money-=WD
def check():
    print(money)
while True:
    print("------------bank ATM-------------")
    print("1.deposte")
    print ("2.with draw ")
    print("3.check balance ")
    print("4.exist")
    choice=int(input("choice the number you want"))
    if choice==1:
        deposte()
    elif choice==2:
        with_draw()
    elif choice==3:
        check()
    elif choice==4:
        print("tanks for using our app")
        break
    else:
        print("unknown comand")
