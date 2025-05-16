Dictionary = {
    "Mikel": 3,
    "Ane": 8,
    "Amaia": 12,
    "Unai": 5,
    "Jon": 8,
    "Ainhoa": 7,
    "Maite": 5,
}

List = []

for Values in Dictionary.values():
    if (List.count(Values) == 0):
        List.append(Values)
    
print(List)