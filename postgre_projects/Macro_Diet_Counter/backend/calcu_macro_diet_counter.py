from datetime import date

class MacroCalculator:
    def __init__(self) -> None:
        self.protein = 4 
        self.carbo = 4
        self.fat = 9


    def date_format(self) -> str:
        today = date.today()
    
        return f"{today.day}-{today.month}-{today.year}"
    

    def convert_to_calories(self, **macrolist) -> dict: #grams to calories
        macro_dict = {}
        date = self.date_format()

        breakfast_protein  = float(macrolist["bf_protein"]) * 4   #1g of protein == 4 calories
        breakfast_carbo = float(macrolist["bf_carbo"]) * 4       #1g of carbo == 4 calories
        breakfast_fat = float(macrolist["bf_fat"]) * 9           #1g of fat == 9 calories   
        lunch_protein = float(macrolist["lunch_protein"]) * 4
        lunch_carbo = float(macrolist["lunch_carbo"]) * 4
        lunch_fat = float(macrolist["lunch_fat"]) * 9
        dinner_protein = float(macrolist["dnr_protein"]) * 4
        dinner_carbo = float(macrolist["dnr_carbo"]) * 4
        dinner_fat = float(macrolist["dnr_fat"]) * 9
        maryenda_cal  = macrolist["maryenda"]
        total_breakfast = breakfast_protein + breakfast_carbo + breakfast_fat
        total_lunch = lunch_protein + lunch_carbo + lunch_fat
        total_dinner = dinner_protein + dinner_carbo + dinner_fat
        protein_total = float(macrolist["bf_protein"]) + float(macrolist["lunch_protein"]) + float(macrolist["dnr_protein"])
        fat_total = float(macrolist["bf_fat"]) + float(macrolist["lunch_fat"]) + float(macrolist["dnr_fat"])
        carbo_total = float(macrolist["bf_carbo"]) + float(macrolist["lunch_carbo"]) + float(macrolist["dnr_carbo"])
    
        #assigns to 
        macro_dict["date"] = date
        macro_dict["breakfast_protein"] = breakfast_protein
        macro_dict["breakfast_carbo"] = breakfast_carbo
        macro_dict["breakfast_fat"]  = breakfast_fat
        macro_dict["breakfast_total_cal"] = total_breakfast
        macro_dict["lunch_protein"] = lunch_protein
        macro_dict["lunch_carbo"] = lunch_carbo
        macro_dict["lunch_fat"] = lunch_fat
        macro_dict["lunch_total_cal"] = total_lunch
        macro_dict["dinner_protein"] = dinner_protein 
        macro_dict["dinner_carbo"] = dinner_carbo
        macro_dict["dinner_fat"] = dinner_fat
        macro_dict["dinner_total_cal"] = total_dinner
        macro_dict["maryenda_cal"] = maryenda_cal
        macro_dict["protein_total"] = protein_total
        macro_dict["fat_total"] = fat_total
        macro_dict["carbo_total"] = carbo_total
        macro_dict["total_cal"] = total_breakfast + total_lunch + total_dinner + float(maryenda_cal)

        return macro_dict
        

