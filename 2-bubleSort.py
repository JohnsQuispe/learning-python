#Bubble Sort Algorithm using D. Flores method
#JohnsQuispe - 08/28/2018

def bubbleSort(list, order):
    changed = True
    while changed:
        changed = False
        for i in range (len(list) - 1):
            if list[i] > list[i+1] and order or list[i] < list[i + 1] and not order:
                changed = True
                aux = list[i + 1]
                list[i + 1] = list[i]
                list[i] = aux

option = ""
order = False
li = [5,4,7,9,3,11,15,1,8,7]

print("\n\tBUBBLE SORT ALGORITHM USING D. FLORES METHOD")

print(f"\nThis list will be sorted: {li}")

while True:
    option = input("\nSelect: \n\tI - Increase \n\tD - Descrease\nOption: ")
    if not option == "I" and not option == "D":
        print("\nInvalid option")
    else:
        order = (option == "I")
        break


bubbleSort(li, order)
print (f"Sorted list: {li}")

