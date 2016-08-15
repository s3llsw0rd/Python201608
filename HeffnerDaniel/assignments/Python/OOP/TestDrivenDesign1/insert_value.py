def insert_val_at(index, my_list, value):
	if index > len(my_list)-1:
		return False
	my_list.append(my_list[len(my_list)-1])
	idx = len(my_list)-1
	while idx > index:
		my_list[idx] = my_list[idx-1]
		idx -= 1
	my_list[index] = value
	return my_list