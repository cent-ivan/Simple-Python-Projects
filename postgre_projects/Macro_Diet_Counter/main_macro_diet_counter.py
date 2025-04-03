import backend.db_macro_diet_counter as db
import backend.calcu_macro_diet_counter as calcu 

db_password = "cyber25"
database = "macrodietdb"

class MacroDietCounter:
    
    def __init__(self, db_password, database) -> None:
        self.db_password = db_password
        self.database =database
        self.db_conn =  db.DataBase(host="localhost", default_db="postgres", user="postgres", password= db_password, port="5432", database= database)
        self.calc = calcu.MacroCalculator()

        self.uid = 0


    def create_db(self) -> None: #connects to database function
        self.db_conn.check_DB()


    def user_login(self) -> None: #User_login
        try:
            print()
            print("-" * 20)
            print("User Log In")
            user_name = input("Name: >>> ")
            pass_id = input("Password: >>> ")

            if user_name == "" or pass_id == "": #check for empty inputs
                print("\n[!] Please fill up all the inputs\n")
                self.user_login()
            else:
                result = self.db_conn.log_in(user_name, pass_id) #stores user data in dict
                self.uid = result["uid"]

                if self.uid != 0: #correct log in
                    self.dashboard()
                else:
                    print("\n[!] Incorrect user name or password. Try Again\n")
                    self.user_login()
            
        except TypeError as error:
            print(f"\n[!] Entry Error - User Log In: {error}\n")
    

    def dashboard(self) -> None:
        try:
            print("-" * 20)
            print("DASHBOARD")
            #ask next user input
            ask = int(input("\n[1] Enter Macro\n[2] View My Macro\n[3] Log Out\n>>> "))
            print("-" * 20)
            if ask == 1:
                self.enter_macro()
            elif ask == 2:
                self.view_macro()
            elif ask == 3:
                print("\nLogging Out...")
            else:
                print("\n[!] Invalid command")
                self.dashboard()


        except TypeError as error:
            print(f"\n[!] Entry Error - User Dashboard: {error}\n")
            self.dashboard()
                

    def user_signin(self) -> None: #User Sign
        try:
            print("-" * 10)
            print("User Registeration")
            user_name = input("Name: >>> ")
            height_cm = input("Height(cm): >>> ")
            weight_lb = input("Weight(lb): >>> ")
            min_cal = input("Enter Minimum Calories: >>> ")
            max_cal = input("Enter Maximum Calories: >>> ")
            pass_id = input("Enter Number Password: >>> ")

            if user_name == "" or height_cm == "" or weight_lb == "" or min_cal == "" or max_cal == "" or pass_id == "": #checks for empty strings
                print("\n[!] Please fill up all the inputs\n")
                self.user_signin()
            else:
                self.db_conn.insert_user(user_name, height_cm, weight_lb, min_cal, max_cal, pass_id)
                enter()

        except TypeError as error:
            print(f"\n[!] Entry Error - User Sign In: {error}\n")
    

    def enter_macro(self) -> None: #enters macro list
        print()
        print("-" * 10)
        print("Enter Macro")
        breakfast_protein = input("Enter BREAKFAST Protein(g): >>> ")
        breakfast_carbo = input("Enter BREAKFAST Carbo(g): >>> ")
        breakfast_fat = input("Enter BREAKFAST Fat(g): >>> ")
        lunch_protein = input("Enter LUNCH Protein(g): >>> ")
        lunch_carbo = input("Enter LUNCH Carbo(g): >>> ")
        lunch_fat = input("Enter LUNCH Fat(g): >>> ")
        dinner_protein = input("Enter DINNER Protein(g): >>> ")
        dinner_carbo = input("Enter DINNER Carbo(g): >>> ") 
        dinner_fat = input("Enter DINNER Fat(g): >>> ")
        maryenda = input("Enter MARYENDA(cal): >>> ")

        if breakfast_protein == "" or breakfast_carbo == "" or  breakfast_fat == "" or lunch_protein == "" or  lunch_carbo == "" or lunch_fat == "" or  dinner_protein == "" or dinner_carbo == "" or dinner_fat == "" or maryenda == "": #checks for empty strings
            print("\n[!] Please fill up all the inputs\n")
            self.enter_macro()
        else:
            macro_list = self.calc.convert_to_calories(bf_protein = breakfast_protein, 
                                                        bf_carbo = breakfast_carbo, 
                                                        bf_fat = breakfast_fat,
                                                        lunch_protein = lunch_protein,
                                                        lunch_carbo = lunch_carbo,
                                                        lunch_fat = lunch_fat,
                                                        dnr_protein = dinner_protein,
                                                        dnr_carbo = dinner_carbo,
                                                        dnr_fat = dinner_fat,
                                                        maryenda = maryenda
                                                        )
            
            #inserts to db
            self.db_conn.insert_macrolist(uid = self.uid,
                                          date = macro_list["date"],
                                          breakfast_protein = macro_list["breakfast_protein"],
                                          breakfast_carbo = macro_list["breakfast_carbo"], 
                                          breakfast_fat  = macro_list["breakfast_fat"], 
                                          breakfast_total_cal  = macro_list["breakfast_total_cal"], 
                                          lunch_protein  = macro_list["lunch_protein"], 
                                          lunch_carbo  = macro_list["lunch_carbo"], 
                                          lunch_fat  = macro_list["lunch_fat"], 
                                          lunch_total_cal  = macro_list["lunch_total_cal"], 
                                          dinner_protein  = macro_list["dinner_protein"], 
                                          dinner_carbo  = macro_list["dinner_carbo"], 
                                          dinner_fat  = macro_list["dinner_fat"], 
                                          dinner_total_cal  = macro_list["dinner_total_cal"], 
                                          maryenda_cal  = macro_list["maryenda_cal"],
                                          protein_total = macro_list["protein_total"],
                                          fat_total = macro_list["fat_total"],
                                          carbo_total = macro_list["carbo_total"],
                                          total_cal  = macro_list["total_cal"]
                                          )
        self.dashboard()


    def view_macro(self) -> None:
        data = {}
        rows = self.db_conn.view_macrolist(self.uid)
        
        for row in rows:
            data["date"] = row[0]
            data["min_cal"] = row[1]
            data["max_cal"] = row[2]
            data["breakfast_protein"] = row[3]
            data["breakfast_carbo"] = row[4]
            data["breakfast_fat"] = row[5]
            data["breakfast_total_cal"] = row[6]
            data["lunch_protein"] = row[7]
            data["lunch_carbo"] = row[8]
            data["lunch_fats"] = row[9]
            data["lunch_total_cal"] = row[10]
            data["dinner_protein"] = row[11]
            data["dinner_carbo"] = row[12]
            data["dinner_fat"] = row[13]
            data["dinner_total_cal"] = row[14]
            data["maryend_cal"] = row[15]
            data["protein_total"] = row[16]
            data["fat_total"] = row[17]
            data["carbo_total"] = row[18]
            data["total_cal"] = row[19]

            original_total = 0.00 if data["maryend_cal"] == 0 else data["total_cal"] - data["maryend_cal"]

            #display format
            format = f"""\n
[DATE: {data["date"]}]
{"=" * 129}
\tBreakfast Protein\t|\tBreakfast Carbo\t\t|\tBreakfast Fat\t\t|\tTotal Calories\t\t|
+{"=" * 31}+{"=" * 31}+{"=" * 31}+{"=" * 31}+
    {data["breakfast_protein"] / 4}g or {data["breakfast_protein"]} calories\t|    {data["breakfast_carbo"] / 4}g or {data["breakfast_carbo"]} calories\t|    {data["breakfast_fat"] / 9}g or {data["breakfast_fat"]} calories\t|     {data["breakfast_total_cal"]} calories\t
{"=" * 129}
\tLunch Protein\t\t|\tLunch Carbo\t\t|\tLunch Fat\t\t|\tTotal Calories\t\t|
+{"=" * 31}+{"=" * 31}+{"=" * 31}+{"=" * 31}+
    {data["lunch_protein"] / 4}g or {data["lunch_protein"]} calories\t|    {data["lunch_carbo"] / 4}g or {data["lunch_carbo"]} calories\t|    {data["lunch_fats"] / 9}g or {data["lunch_fats"]} calories\t|     {data["lunch_total_cal"]} calories\t
{"=" * 129}
\tDinner Protein\t\t|\tDinner Carbo\t\t|\tDinner Fat\t\t|\tDinner Calories\t\t|
+{"=" * 31}+{"=" * 31}+{"=" * 31}+{"=" * 31}+
    {data["dinner_protein"] / 4}g or {data["dinner_protein"]} calories\t|    {data["dinner_carbo"] / 4}g or {data["dinner_carbo"]} calories\t|    {data["dinner_fat"] / 9}g or {data["dinner_fat"]} calories\t|     {data["dinner_total_cal"]} calories\t
Maryenda Calories:  {data["maryend_cal"]} calories

Protein: {data["protein_total"]}g or {data["protein_total"] * 4} calories| Fat: {data["fat_total"]}g or {data["fat_total"] * 9} calories | Carbo: {data["carbo_total"]}g or {data["carbo_total"] * 4} calories
Total Calories/day no maryenda: {original_total} calories
Total Calories/day: {data["total_cal"]} calories

"""

            if data["total_cal"] < data["min_cal"]:
                format += f"Calories below minimum {data["min_cal"]} eat some more"
            elif data["total_cal"] > data["min_cal"] and data["total_cal"] < data["max_cal"]:
                format += f"Calories is somewhat balance {data["total_cal"]} good job"
            else:
                format += f"Calories above maximum {data["max_cal"]} you may gain some weight"
            

            print(format)
        self.dashboard()


app = MacroDietCounter(db_password, database)
def enter() -> None:
    
        ask = int(input("[1] Log In\n[2] Sign In\n>>> "))
        if ask == 1:
            app.user_login()
        elif ask == 2:
            app.user_signin()
        else:
            print("\n[!] Invalid command. Try again\n")
            enter()




def main() -> None:
    app.create_db()
    enter()
    


if __name__ == "__main__":
    main()