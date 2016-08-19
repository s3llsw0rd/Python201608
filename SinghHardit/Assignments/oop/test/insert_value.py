def insert_val_at(index, my_list, value):  
    if index >= len(my_list):
        return False
    my_list.insert(index,value)
    return my_list

# print insert_val_at(2, [0,1,2,3,4], 100)
