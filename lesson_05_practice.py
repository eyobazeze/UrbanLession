def pop_density(pop, area):
    return pop/area

density = pop_density(12000, True)

def transit_priority(dense, has_bus):
    if dense > 10000 and not has_bus:
        return "High priority"
    elif dense > 5000:
        return "Medium priority"
    else:
        return "Low priority"


print(transit_priority(density, True))