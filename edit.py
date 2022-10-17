from pprint import pprint
import pathlib
from pathlib import Path

dir_path = pathlib.Path.cwd()
path = Path(dir_path, "files", "recipes.txt") 

cook_book = {}
dish_list = []


with open(path, 'rt', encoding= 'utf8') as file:
    for l in file:     
        dish_name = l.strip()   
        ingredients_list = []
        dish = {dish_name: ingredients_list}      
        dish_count = file.readline() 
        for i in range(int(dish_count)):           
            dsh = file.readline().strip().split(' | ') 
            ingredients_list.append({'ingredient_name': dsh[0],
                            'quantity': int(dsh[1]),
                            'measure': dsh[2]})
        dish_list.append(dish)                
        blank_line = file.readline()
        cook_book.update(dish)              

pprint(cook_book)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for loc in cook_book[dish]:
                person_q = int(loc['quantity']) * person_count
                dict_list = {loc['ingredient_name']: {'measure': loc['measure'], 'quantity': person_q}}
                shop_list.update(dict_list)
        return shop_list
    
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 7))


def  reading_files(*f123):
    all_text = {}
    for file in f123:
        with open(file, encoding='utf-8') as f:
            y = f.readlines()
            all_text[file] = y
    final_text = {j: all_text[j] for j in sorted(all_text, key=all_text.get, reverse=True)}
    for key1, value in final_text.items():
        with open('final_sorted.txt', 'a', encoding='utf-8') as f123:
            r = len(value)
            f123.writelines(key1)
            f123.writelines(f'\n{r}\n')
            f123.writelines(value)
            f123.writelines('\n')
reading_files('sorted\\1.txt','sorted\\2.txt','sorted\\3.txt')