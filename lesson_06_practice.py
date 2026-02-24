with open("urban_data.csv", "r") as file:
    next(file)

    for line in file:
        data = line.strip().split(",")

        neighborhood = data[0]
        population = int(data[1])
        area = float(data[2])

        density = population / area

        print(neighborhood, "density:", round(density, 2))
