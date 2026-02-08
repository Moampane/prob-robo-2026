# Part 1: Sense and Act
# Scrap type counts
metal = 100
plastic = 230
organic = 73
composite = 20
toxic = 5

total = metal + plastic + organic + composite + toxic

# Probability of each category of scrap
p_c_metal = metal / total
p_c_plastic = plastic / total
p_c_organic = organic / total
p_c_composite = composite / total
p_c_toxic = toxic / total

# P (Label | Category)
p_l_composite_c_metal = 0.2
p_l_composite_c_plastic = 0.05
p_l_composite_c_composite = 1

p_l_toxic_c_plastic = 0.05
p_l_toxic_c_organic = 0.4
p_l_toxic_c_toxic = 1

# Probability of a label of scrap
p_l_composite = (
    p_l_composite_c_metal * p_c_metal
    + p_l_composite_c_plastic * p_c_plastic
    + p_l_composite_c_composite * p_c_composite
)

p_l_toxic = (
    p_l_toxic_c_plastic * p_c_plastic
    + p_l_toxic_c_organic * p_c_organic
    + p_l_toxic_c_toxic * p_c_toxic
)

# P (Category | Label)
p_c_metal_l_composite = p_l_composite_c_metal * p_c_metal / p_l_composite
p_c_plastic_l_composite = p_l_composite_c_plastic * p_c_plastic / p_l_composite
p_c_composite_l_composite = p_l_composite_c_composite * p_c_composite / p_l_composite

p_c_plastic_l_toxic = p_l_toxic_c_plastic * p_c_plastic / p_l_toxic
p_c_organic_l_toxic = p_l_toxic_c_organic * p_c_organic / p_l_toxic
p_c_toxic_l_toxic = p_l_toxic_c_toxic * p_c_toxic / p_l_toxic

# Part 2 Evaluation
wrong_unit_cost = 150

wrong_metal = metal * p_l_composite_c_metal
wrong_plastic = plastic * (p_l_composite_c_plastic + p_l_toxic_c_plastic)
wrong_organic = organic * p_l_toxic_c_organic

wrong_cost = wrong_unit_cost * (wrong_metal + wrong_plastic + wrong_organic)

print(f"Expected cost of wrong sorts: {wrong_cost}")

print(f"Wrongly sorted metal: {wrong_metal}")
print(f"Wrongly sorted plastic: {wrong_plastic}")
print(f"Wrongly sorted organic: {wrong_organic}")
