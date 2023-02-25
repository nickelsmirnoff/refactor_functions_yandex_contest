def d(p,k):
    return {i["name"]:i[k]for i in p}
def get_people_with_min_age(p):
    a=d(p,"age")
    return sorted([i for i in a.keys() if a[i]==min(a.values())])
def get_people_with_max_age(p):
    a=d(p,"age")
    return sorted([i for i in a.keys() if a[i]==max(a.values())])
def get_people_with_min_height(p):
    a=d(p,"height")
    return sorted([i for i in a.keys() if a[i]==min(a.values())])
def get_people_with_max_height(p):
    a=d(p,"height")
    return sorted([i for i in a.keys() if a[i]==max(a.values())])
def get_people_with_min_weight(p):
    a=d(p,"weight")
    return sorted([i for i in a.keys() if a[i]==min(a.values())])
def get_people_with_max_weight(p):
    a=d(p,"weight")
    return sorted([i for i in a.keys() if a[i]==max(a.values())])
# ________________________________________________________
# age name height weight
people_array = \
[
{"name": "Max2", "age": 20, "height": 180, "weight": 80},
{"name": "Peter2", "age": 40, "height": 160, "weight": 50},
{"name": "Alex2", "age": 12, "height": 120, "weight": 40},
{"name": "Stan2", "age": 80, "height": 170, "weight": 80},
{"name": "Max", "age": 20, "height": 180, "weight": 80},
{"name": "Peter", "age": 40, "height": 160, "weight": 50},
{"name": "Alex", "age": 12, "height": 120, "weight": 40},
{"name": "Stan", "age": 80, "height": 170, "weight": 80}
]
print(get_people_with_max_weight(people_array))
# ['Max', 'Max2', 'Stan', 'Stan2']
print(get_people_with_min_weight(people_array))
# ['Alex', 'Alex2']
print(get_people_with_max_age(people_array))
# ['Stan', 'Stan2']
print(get_people_with_min_age(people_array))
# ['Alex', 'Alex2']
print(get_people_with_max_height(people_array))
# ['Max', 'Max2']
print(get_people_with_min_height(people_array))
# ['Alex', 'Alex2']