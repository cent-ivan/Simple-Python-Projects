import psycopg2
uid = 1
with psycopg2.connect(host = "localhost", dbname = "macrodietdb", user = "postgres", password = "cyber25", port = "5432") as conn:
    with conn.cursor() as cur:
        query = """SELECT macro_list_tbl.date, 
                                      users_tbl.min_cal, 
                                      users_tbl.max_cal,
                                      macro_list_tbl.breakfast_protein,
                                      macro_list_tbl.breakfast_carbo, 
                                      macro_list_tbl.breakfast_fat, 
                                      macro_list_tbl.breakfast_total_cal, 
                                      macro_list_tbl.lunch_protein, 
                                      macro_list_tbl.lunch_carbo, 
                                      macro_list_tbl.lunch_fats, 
                                      macro_list_tbl.lunch_total_cal, 
                                      macro_list_tbl.dinner_protein, 
                                      macro_list_tbl.dinner_carbo, 
                                      macro_list_tbl.dinner_fat, 
                                      macro_list_tbl.dinner_total_cal, 
                                      macro_list_tbl.maryend_cal,
                                      macro_list_tbl.total_cal

                                FROM macro_list_tbl INNER JOIN users_tbl ON macro_list_tbl.user_id = users_tbl.user_id WHERE macro_list_tbl.user_id = %s ;
                            """
        cur.execute(query, (uid,))
        for row in cur.fetchall():
            for data in row:
                print()


        format = f"""
[DATE: 08-10-2024]
{"=" * 129}
\tBreakfast Protein\t|\tBreakfast Carbo\t\t|\tBreakfast Fat\t\t|\tTotal Calories\t\t|
+{"=" * 31}+{"=" * 31}+{"=" * 31}+{"=" * 31}+
    00.0g or 000.0 calories\t|    00.0g or 00.0 calories\t|    00.0g or 00.0 calories\t|     00.0g or 000.0 calories\t|
\n{"=" * 129}
\tLunch Protein\t\t|\tLunch Carbo\t\t|\tLunch Fat\t\t|\tTotal Calories\t\t|
+{"=" * 31}+{"=" * 31}+{"=" * 31}+{"=" * 31}+
    12.0g or 600.0 calories\t|    60.0g or 300.0 calories\t|    30.0g or 460.0 calories\t|     1569.0 calories\t\t|
\n{"=" * 129}
\tDinner Protein\t\t|\tDinner Carbo\t\t|\tDinner Fat\t\t|\tTotal Calories\t\t|
+{"=" * 31}+{"=" * 31}+{"=" * 31}+{"=" * 31}+
    12.0g or 600.0 calories\t|    60.0g or 300.0 calories\t|    30.0g or 460.0 calories\t|     4569.0 calories\t\t|

Maryenda Calories:  173.1 calories
Total Calories/day: 15048 calories
"""