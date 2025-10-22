list_of_items = input("Enter a list of items separated by spaces: ").split()
unique_list_items = set()

for item in list_of_items:
    if item in unique_list_items:
        print("duplicate: ", item)
        break
    unique_list_items.add(item)


