neighborhoods = ["Bole", "Piassa", "CMC", "Gerji"]
population = [2000,2200,3000,4000,5000]
area = {
    "name": "Bole",
    "population": 120000,
    "has_bus": True
}
#Q1
for i in neighborhoods:
    print(i)
#Q2
for j in population:
    if j>2500:
        print("High population: ",j)