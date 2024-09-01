import os
import time

os.chdir(r"C:/Users/Client/My_Codes") #set path

json_data = {
}

with open('barangay.txt', 'r') as file:
    #put nests here
        
    count = 0


    data_list = file.read().split('\n') #converts first the files into list by new line
    for content in data_list:
        count += 1
        #---------CHANGE HERE THE JSON KEY--------------
        name = content.split(',')
        json_key = ''.join(name[0].split(' ')) #removes whitespaces into json key
        #----------------------------------------------

        json_data[json_key] = content
    print("Total:", count)

    print(f"\nRaw converted to Json:\n{json_data}\n")

    #--OPTIONAL------------ 
    print("\nCopy Json data here:------------------------------------\n")
    for values in json_data:
        print('\t"%s" : {"name" : \"%s\"} ,'%(values, json_data[values])) 


#save json to device
def save_json():
    filename = input("\nEnter filename (Save as): ")

    if filename in os.listdir():
        print("\nFile already existed")
    else:
        #write json file
        with open(f"{filename}.json", 'a') as file:
            file.write('{\n')

            for values in json_data:
                file.write('\t"%s" : { "name" : \"%s\" } ,\n'%(values, json_data[values]))

            file.write('}')
            
        time.sleep(1.5)
        print("Done...")

ask = int(input("\nSave to Device? \n[1] - Yes \n[0] - No \n>>> "))
if ask == 1:
    save_json()
else:
    print("\nGoodbye")