menu = {"pizza": 150,
        "nachos": 90,
        "popcorn": 56,
        "fries": 78,
        "chips": 99,
        "soda": 45,
        "lemonade": 49}
cart = []
total = 0
print('--------MENU--------')
for key, value in menu.items():
    print(f"{key:10} :{value} rupess")
print("---------------------")

while True:
    food = input("select an item (q to exit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------your order-------")
for food in cart:
    total = total + menu.get(food)
    print(food, end=" ")
print()
print(f"total is : {total} rupees")
