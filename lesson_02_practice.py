neighborhoods = ["bole","piassa","megenagna","addisu gebeya","cmc"]
population = [10000,2000,2300,4000,5000]

total_population = sum(population)
average = total_population / len(population)

for pop in population:
    print(pop)

print(f"Average population is {average}")


city = {
    "name":"bole",
    "population":10000,
    "has_bus_access":True,
}

for key, value in city.items():
    print(key, ":", value)

print(city["name"])