population_density = 5000000
avg_commute_time = 100
bus_availability = True

#Question 1
if population_density > 3000000:
    print("High density area")
else:
    print("Low density area")

#Question 2
if avg_commute_time <= 50:
    print("Good commute time")
elif avg_commute_time <= 100:
    print("Moderate commute time")
else:
    print("Poor commute time")

#Question 3
if population_density > 10000 and not bus_availability:
    print("Transit upgrade needed")

#Example
area = {
    "name": "Kazanchis",
    "population": 90000,
    "has_bus": True
}

if area["population"] < 100000 and area["has_bus"]:
    print(area["name"], "has bus access with a big population")
