
def occupiedStatus(is_occupied):
    if is_occupied:
        return "Occupied"
    else:
        return "Not Occupied"

def display_all_tables(pool_tables):
    for table in pool_tables:
      print(f"{table.table_number} Table {occupiedStatus(table.is_occupied)} - {table.start_time}")

def save_to_file():
    with open ("time_log.txt","w") as file:
        for table in pool_tables:
            file.write(f'Table number: {table.table_number} {table.end_time} {table.time_duration} {table.total_cost} \n')
