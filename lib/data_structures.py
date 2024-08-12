
import ipdb

spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for i in range(len(spicy_foods)):
        names.append(spicy_foods[i]["name"])
    return names

def get_spiciest_foods(spicy_foods):
    names = []
    for i in range(len(spicy_foods)):
        if spicy_foods[i]["heat_level"] > 5:
            names.append(spicy_foods[i])
    return names

def print_spicy_foods(spicy_foods):
    for i in range(len(spicy_foods)):
        heat = spicy_foods[i]['heat_level']
        my_string = heat * "🌶"
        print(f"{spicy_foods[i]['name']} ({spicy_foods[i]['cuisine']}) | Heat Level: " + my_string)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in range(len(spicy_foods)):
        if spicy_foods[i]['cuisine'] == cuisine:
            return spicy_foods[i]
        else:
            pass

def print_spiciest_foods(spicy_foods):
    print_spicy_foods(get_spiciest_foods(spicy_foods))

def get_average_heat_level(spicy_foods):
    heat = []
    for i in range(len(spicy_foods)):
        heat_food = spicy_foods[i]['heat_level']
        heat.append(heat_food)
    avg = int(sum(heat) / (len(spicy_foods)))
    return avg

def create_spicy_food(spicy_foods, spicy_food):
    new_list = spicy_foods
    new_list.append(spicy_food)
    return new_list

'''new_list = create_spicy_food(spicy_foods, {
        'name': 'Griot',
        'cuisine': 'Haitian',
        'heat_level': 10,
    })
    '''
#ipdb.set_trace()