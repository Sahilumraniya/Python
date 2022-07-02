"""d={"Sahil":24,"kajal":4}
print(d["Sahil"])"""

party = {
    "Jap": "Maggie",
    "Tejas": 13,
    "Dhiraj": ("Khichdi", "Sabji", "Buttermilk"),
    "Krishna": ["soup", "main course", "browny"],
    "Alakh": {"soup", "main course", "browny"},
    "Madhusudan Sir": frozenset({"Khichdi", "Sabji", "Buttermilk"}),
    "Rahul": {"BF": "Poha", "Lunch": "Punjabi", "Dinner": "South indian"}
}
print(party)
key = input("Enter name of person ")
if key == "Rahul":
    time = input("Enter time : ")
    print(party[key][time])
else:
    print(party[key.capitalize()])
