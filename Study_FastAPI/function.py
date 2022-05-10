
''' Define a function '''


def get_full_name(first_name:str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name:str, age:int):
    name_with_age = name + " is this old: " + str(age) # str(age)-> type check
    return name_with_age

def get_items(item_a:str, item_b:int, item_c: float, item_d:bool, item_e:bytes):
    return item_a, item_b, item_c, item_d, item_e

print(get_full_name("john","doe"))
print(get_name_with_age("Yebin",23))
print(get_items("hello", 23, 35.2, True, 128))


