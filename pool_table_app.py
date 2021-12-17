# import json

from pool_table_class import PoolTable
from datetime import date
today = date.today()
current_date = today.strftime("%m/%d/%y")

pool_tables = []

for index in range(1, 13):
    pool_table = PoolTable(index)
    pool_tables.append(pool_table)

def occupiedStatus(is_occupied):
    if is_occupied:
        return "Occupied"
    else:
        return "Not Occupied"

def display_all_tables():
    for table in pool_tables:
      print(f"{table.table_number} Table {occupiedStatus(table.is_occupied)} - {table.start_time}")

def save_to_file(table_number):
    with open ("time_log.txt","a") as file:
        for table in pool_tables:
            if table.table_number == table_number:
                file.write(f'Table number: {table.table_number} {table.end_time} {table.time_duration} {table.total_cost} \n')
    
while True:
    print("**********************************\n")
    print("---Welcome to K8's Pool Lounge!---")
    print(f" \t   {current_date}\n")
    print("**********************************\n")
    print("___________________________________\n")
    print("Enter 1 to checkout table: ")
    print("Enter 2 to checkin table: ")
    print("Enter 3 to display all tables: ")
    print("Enter q to quit: ")
    print("___________________________________\n")

    choice = input("Enter choice: ")
    try:
        if choice == "1":
                display_all_tables()
                table_number = int(input("Enter table number to checkout: "))
                pool_table = pool_tables[table_number -1]
                if pool_table.is_occupied == False: 
                    pool_table.check_out()
                elif pool_table.is_occupied == True:
                    print("This table is already checked out.")
                    display_all_tables()
                    table_number = int(input("Please enter a different table number: "))
                    pool_table = pool_tables[table_number -1]
                    pool_table.check_out()



        elif choice == "2":
            table_number = int(input("Enter table number to checkin: "))
            pool_table = pool_tables[table_number -1]
            if pool_table.is_occupied == True: 
                pool_table.check_in()
            elif pool_table.is_occupied == False:
                print("This table has not been checked out.")
                display_all_tables()
                table_number = int(input("Please enter a different table number: "))
                pool_table = pool_tables[table_number -1]
                pool_table.check_in()
            print(f"time played {pool_table.time_duration}")
            print(f"total cost $ {pool_table.total_cost}")
            save_to_file(table_number)

        elif choice == "3":
            display_all_tables()

        elif choice == "q":
            break
    except ValueError:
        print("Please select enter a valid table number: ")
    except:
        print("Oops! Something went wrong!")        
