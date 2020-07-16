usernameInput = input("Username :")
passwordInput = input("Password :")
if usernameInput  == "customer"  and passwordInput == "1234" :
    print("Done !")
    print("----- AriawaShop -----")
    print("1. Espresso    : 70  THB")
    print("2. Americano   : 50  THB")
    print("3. Cappuccino  : 80  THB")
    print("4. Latte       : 70  THB")
    print("5. Macchiato   : 120 THB")
    userSelected = int(input("เลือกรายการสินค้า : "))
    if userSelected == 1:
        amount = int(input("จำนวน : "))
        price = 70
        menu = "Espresso"
        result = price*amount
        print(menu,result,"THB")
    elif userSelected == 2:
        amount = int(input("จำนวน : "))
        price = 50
        menu = "Americano"
        result = price*amount
        print(menu, result, "THB")
    elif userSelected == 3:
        amount = int(input("จำนวน : "))
        price = 80
        menu = "Cappuccino"
        result = price*amount
        print(menu, result, "THB")
    elif userSelected == 4:
        amount = int(input("จำนวน : "))
        price = 80
        menu = "Latte"
        result = price*amount
        print(menu, result, "THB")
    elif userSelected == 5:
        amount = int(input("จำนวน : "))
        price = 120
        menu = "Macchiato"
        result = price*amount
        print(menu, result, "THB")
    else:
        print("คุณไม่ได้เลือกรายการ")

