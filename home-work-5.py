def get_cook_boook():
    cook_boook = {}
    with open("data.txt") as data_file:
        for line in data_file:
            if line not in cook_boook.keys():
                cook_boook[line.strip()] = list()
            ingridients_quantity = int(data_file.readline().strip())
            index = 1
            while index <= ingridients_quantity:
                index += 1
                ingridients_line = data_file.readline().strip().split("|")

                ingridients_dict = {"ingridient_name":ingridients_line[0],"quantity":int(ingridients_line[1]),"measure":ingridients_line[2]}
                cook_boook[line.strip()].append(ingridients_dict)
            data_file.readline()
    return cook_boook

def get_shop_list_by_dishes(dishes, person_count, cook_boook):
    composition = {}
    for dish in dishes:
        for ingridient in cook_boook[dish]:
            if ingridient["ingridient_name"] not in composition.keys():
                composition[ingridient["ingridient_name"]] = {}
                quantity = ingridient["quantity"] * person_count
            else:
                composition_line = composition[ingridient["ingridient_name"]]
                quantity = composition_line["quantity"] + ingridient["quantity"] * person_count
            composition[ingridient["ingridient_name"]] = {"measure": ingridient["measure"], "quantity": quantity}
    return composition

cook_boook = get_cook_boook()
composition = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2, cook_boook) #ошибка в ответе домашннего задания в примере
print(composition)
composition = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2, cook_boook)
print(composition)