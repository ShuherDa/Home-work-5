def get_cook_book():
    cook_book = {}
    with open("data.txt") as data_file:
        for line in data_file:
            line_strip = line.strip()
            if line_strip not in cook_book:
                cook_book[line_strip] = list()
            ingridients_quantity = int(data_file.readline().strip())
            for i in range(ingridients_quantity):
                ingridients_line = data_file.readline().strip().split("|")

                ingridients_dict = {"ingridient_name":ingridients_line[0].strip(),
                                    "quantity":int(ingridients_line[1].strip()),
                                    "measure":ingridients_line[2].strip()}
                cook_book[line_strip].append(ingridients_dict)
            data_file.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_boook):
    composition = {}
    for dish in dishes:
        for ingridient in cook_boook[dish]:
            if ingridient["ingridient_name"] not in composition:
                composition[ingridient["ingridient_name"]] = {}
                quantity = ingridient["quantity"] * person_count
            else:
                composition_line = composition[ingridient["ingridient_name"]]
                quantity = composition_line["quantity"] + ingridient["quantity"] * person_count
            composition[ingridient["ingridient_name"]] = {"measure": ingridient["measure"], "quantity": quantity}
    return composition

cook_book = get_cook_book()
composition = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_book)
print(composition)
composition = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, cook_book)
print(composition)