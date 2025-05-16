List = [12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
Counter = {}

for Element in List:
    if (Counter.get(Element) == None):
        Counter[Element] = 1
    else:
        Counter[Element] += 1
        
print(Counter)