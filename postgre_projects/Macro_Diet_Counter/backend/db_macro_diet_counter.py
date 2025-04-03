import psycopg2
from psycopg2 import sql


class DataBase:
    def __init__(self, **params) -> None:
        self.host = params["host"]
        self.default_db = params["default_db"]
        self.user = params["user"]
        self.password = params["password"]
        self.port = params["port"]
        self.database = params["database"]
        

    def check_DB(self) -> None: #checks if the db exists
        try:
            isPresent = False
            with psycopg2.connect(host = self.host, dbname = self.default_db, user = self.user, password = self.password, port = self.port) as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT * FROM pg_database;")
                    for row in cur.fetchall():
                        if row[1] == self.database:
                            isPresent = True
                        else:
                            continue
            if isPresent:
                self.create_TBL()
            else:
                self.create_DB()
                

        except psycopg2.Error as Error:
            print("Error in Postgre (CHECKING DB):", Error)


    def create_DB(self) -> None: #creates table
        try:
            conn = psycopg2.connect(host = self.host, dbname = self.default_db, user = self.user, password = self.password, port = self.port)
            conn.autocommit = True #After executing sql query it auto commits
            cur = conn.cursor()

            cur.execute(sql.SQL("CREATE DATABASE {db}").format(db = sql.Identifier(self.database))) #identify python string as sql object such as database name, table name
            print("Database created...")

            cur.close()
            conn.close()

            self.create_TBL()

        except psycopg2.Error as Error:
            print("Error in Postgre (CREATING DB):", Error)

        
    def create_TBL(self) -> None: #creates table
        try:
            with psycopg2.connect(host = self.host, dbname = self.database, user = self.user, password = self.password, port = self.port) as conn:
                with conn.cursor() as cur:

                    cur.execute("SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';") #check for table
                    result = cur.fetchone()
                    if result:
                        print("Table exists...")
                    else:
                        #creates table of user
                        cur.execute("""--sql
                            CREATE TABLE users_tbl(
                                    user_id SERIAL PRIMARY KEY,
                                    user_name VARCHAR(60) NOT NULL,
                                    height_cm DECIMAL(10, 2) NOT NULL,
                                    weight_lb DECIMAL(8,2) NOT NULL,
                                    min_cal DECIMAL(20, 2) NOT NULL,
                                    max_cal DECIMAL(20, 2) NOT NULL,
                                    pass_id INT NOT NULL
                            );
                        """)

                        #create table of macro list
                        cur.execute("""--sql
                            CREATE TABLE macro_list_tbl(
                                    user_id INT,
                                    date VARCHAR(10) NOT NULL,
                                    breakfast_protein DECIMAL(10,2) NOT NULL,
                                    breakfast_carbo DECIMAL(10,2) NOT NULL,
                                    breakfast_fat DECIMAL(10,2) NOT NULL,
                                    breakfast_total_cal DECIMAL(20, 2) NOT NULL,
                                    lunch_protein DECIMAL(10,2) NOT NULL,
                                    lunch_carbo DECIMAL(10,2) NOT NULL,
                                    lunch_fats DECIMAL(10,2) NOT NULL,
                                    lunch_total_cal DECIMAL(20, 2) NOT NULL,
                                    dinner_protein DECIMAL(10,2) NOT NULL,
                                    dinner_carbo DECIMAL(10,2) NOT NULL,
                                    dinner_fat DECIMAL(10,2) NOT NULL,
                                    dinner_total_cal DECIMAL(20, 2) NOT NULL,
                                    maryend_cal DECIMAL(20, 2) NOT NULL,
                                    protein_total DECIMAL(20, 2) NOT NULL,
                                    fat_total DECIMAL(20, 2) NOT NULL,
                                    carbo_total DECIMAL(20, 2) NOT NULL,
                                    total_cal  DECIMAL(20, 2) NOT NULL,
                                    CONSTRAINT fk_users_tbl
                                        FOREIGN KEY (user_id)
                                        REFERENCES users_tbl (user_id)
                            );  
                        """)
                        print("Table Created")

        except psycopg2.Error as Error:
            print("Error in Postgre (CREATING TABLE):", Error)

    
    def log_in(self, user_name, pass_id) -> dict:
        try:
            user = {}
            with psycopg2.connect(host = self.host, dbname = self.database, user = self.user, password = self.password, port = self.port) as conn:
                with conn.cursor() as cur:
                    query = "SELECT user_id, user_name  FROM users_tbl WHERE user_name = %s AND pass_id = %s ;"
                    cur.execute(query, (user_name, pass_id))
                    
                    qry_result = cur.fetchone()
                    #assigns to dictionary
                    user["uid"] = qry_result[0]
                    user["name"] = qry_result[1]

                    print("LOGGED IN as:", qry_result)
            
            return user
                    
                
        except psycopg2.Error as Error:
            print("Error in Postgre (LOGGING IN):", Error)


    def insert_user(self, user_name, height_cm, weight_lb, min_cal, max_cal, pass_id) -> None: #inserts user data
        try:
            with psycopg2.connect(host = self.host, dbname = self.database, user = self.user, password = self.password, port = self.port) as conn:
                with conn.cursor() as cur:
                    query = "INSERT INTO users_tbl(user_name, height_cm, weight_lb, min_cal, max_cal, pass_id) VALUES ( %s , %s , %s , %s , %s , %s );"
                    cur.execute(query, (user_name, height_cm, weight_lb, min_cal, max_cal, pass_id)) #safe insert
                    print("Inserted to user")

        except psycopg2.Error as Error:
            print("Error in Postgre (INSERTING USER):", Error)

    
    def insert_macrolist(self, **macrolist) -> None:
        try:
            with psycopg2.connect(host = self.host, dbname = self.database, user = self.user, password = self.password, port = self.port) as conn:
                with conn.cursor() as cur:
                    query = """INSERT INTO macro_list_tbl(user_id, 
                                                          date, 
                                                          breakfast_protein,
                                                          breakfast_carbo, 
                                                          breakfast_fat, 
                                                          breakfast_total_cal, 
                                                          lunch_protein, 
                                                          lunch_carbo, 
                                                          lunch_fats, 
                                                          lunch_total_cal, 
                                                          dinner_protein, 
                                                          dinner_carbo, 
                                                          dinner_fat, 
                                                          dinner_total_cal,
                                                          maryend_cal,
                                                          protein_total,
                                                          fat_total,
                                                          carbo_total,
                                                          total_cal)
                                VALUES ( %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s );"""
                    cur.execute(query, (  macrolist["uid"],
                                          macrolist["date"],
                                          macrolist["breakfast_protein"],
                                          macrolist["breakfast_carbo"], 
                                          macrolist["breakfast_fat"], 
                                          macrolist["breakfast_total_cal"], 
                                          macrolist["lunch_protein"], 
                                          macrolist["lunch_carbo"], 
                                          macrolist["lunch_fat"], 
                                          macrolist["lunch_total_cal"], 
                                          macrolist["dinner_protein"], 
                                          macrolist["dinner_carbo"], 
                                          macrolist["dinner_fat"], 
                                          macrolist["dinner_total_cal"], 
                                          macrolist["maryenda_cal"],
                                          macrolist["protein_total"],
                                          macrolist["fat_total"],
                                          macrolist["carbo_total"],
                                          macrolist["total_cal"]
                                        )
                                )
            print("Inserted to macros")


        except psycopg2.Error as Error:
            print("Error in Postgre (INSERTING MACRO LIST):", Error)

    def view_macrolist(self, uid) -> list: #gets the data
        try:
            data = []
            with psycopg2.connect(host = self.host, dbname = self.database, user = self.user, password = self.password, port = self.port) as conn:
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
                                      macro_list_tbl.protein_total,
                                      macro_list_tbl.fat_total,
                                      macro_list_tbl.carbo_total,
                                      macro_list_tbl.total_cal

                                FROM macro_list_tbl INNER JOIN users_tbl ON macro_list_tbl.user_id = users_tbl.user_id WHERE macro_list_tbl.user_id = %s ;
                            """
                    cur.execute(query, (uid,))
                    data =  cur.fetchall()

            return data

        except psycopg2.Error as Error:
            print("Error in Postgre (CREATING DB):", Error)

 