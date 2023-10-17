import time

CASHIER_DATA = {"Johanne Johnson":11245, "James Web":11269}

#---Log In Dashboard-------------------------------------------------
print("""
[][][][][][][][][][][][][][][][][][][][[]
[]                                     []
[]        JULLY'S BURGER LOG IN        []
[]                                     []
[][][][][][][][][][][][][][][][][][][][[]
|""")

#User log in logic flow
USER = input("[] Enter User Name: ")
if USER in CASHIER_DATA:
    User_Pass = int(input("[] Enter Password: "))
else:
    print("\n[!]SYSTEM >>> Invalid User")
    pass

time.sleep(1)

#---------------------------------------------------------------------

#---Receipt Code------------------------------------------------------
def receipt(total,ORDERS):
    print("""
\n#########################################
#                                       #
#        JULLY'S BURGER RECEIPT         #
#                                       #
#########################################""")

    for items in ORDERS:
        print(f"\t{items}")
    
    print("\tTotal:",sum(total))
    print("[][][][][][][][][][][][][][][][][][][][[]")
    dashboard()


#---Order-------------------------------------------------------------
def Order(MENU):
    ORDERS = []
    total = []
    def order_compute(total,ORDERS):
        print()
        print("---" * 20)

        FTYPE = input("\nEnter Food Type \nB - Burger\nS - Sides\nD - Drinks \n: ").upper()
        CODE = input("Enter Food Code: ").upper()
        QUANTITY = int(input("Quantity: "))
        promptText = f"{QUANTITY}x {CODE} = TOTAL: Php {MENU[FTYPE][CODE] * QUANTITY}"
        
        newOrder = input("\nEnter New Order? [Y|N]: ").upper()
        if newOrder == "Y":
            ORDERS.append(promptText)
            total.append(MENU[FTYPE][CODE] * QUANTITY)
            order_compute(total,ORDERS)
        elif newOrder == "N":
            ORDERS.append(promptText)
            total.append(MENU[FTYPE][CODE] * QUANTITY)
            total_price = sum(total)
            print(f"\nTotal: Php {total_price}")
            receipt(total, ORDERS)
        else:
            print("\n[!]SYSTEM >>> Invalid Input. TRY AGAIN")
            Order()
        
    order_compute(total,ORDERS)
    

#--------------------------------------------------------------------


#---Dashboard UI------------------------------------------------------
def dashboard():
    print()
    print("""
    #####################################################################################################
    #              BURGERS               #              SIDES             #           DRINKS            #
    #####################################################################################################
    #                                    #                                #                             #
    #  B1-Regular Burger      -Php25.00  #  F1-Reguar Fries    -Php10.00  #  D1-Coke         -Php13.00  #
    #  B2-Cheese Burger       -Php30.00  #  F2-Fries w/ cheese -Php12.00  #  D2-Sprite       -Php13.00  #
    #  B3-Double Patty Burger -Php55.00  #  S1-Green Salad     -Php25.00  #  D3-Diet Coke    -Php15.00  #
    #  B4-Family Burger       -Php110.00 #                                #  D4-Coke Float   -Php20.00  #
    #                                    #                                #  W -Water        -Free      #
    #                                    #                                #                             #
    #####################################################################################################""")
    
    MENU_DATA = {"B":
        {"B1":25.00, "B2":30.00, "B3":55.00, "B4":110.00},
        "S":
        {"F1":10.00, "F2":12.00, "S1":25.00},
        "D":
        {"D1":13.00, "D2":13.00, "D3":15.00, "D4":20.00, "W":0.00}
    }

    def ask_():
        ask = input("\nNew Order? [Y]|[N]: ").upper()
        if ask == "Y":
            Order(MENU_DATA)
        elif ask == "N":
            print("\nGoodbye")
        else:
            print("\n[!]SYSTEM >>> Invalid Input. TRY AGAIN")
            ask_()
    ask_()
#--------------------------------------------------------------------


if User_Pass == CASHIER_DATA[USER]:
    print("\n\nWelcome",USER)
    dashboard()
else:
    print("\nGoodbye")