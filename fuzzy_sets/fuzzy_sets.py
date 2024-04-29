import numpy as np

# Function to perform Union of fuzzy sets
def fuzzy_union(set1, set2):
    return np.maximum(set1, set2)

# Function to perform Intersection of fuzzy sets
def fuzzy_intersection(set1, set2):
    return np.minimum(set1, set2)

# Function to find Complement of a fuzzy set
def fuzzy_complement(set1):
    return 1 - set1

# Function to find Difference of two fuzzy sets
def fuzzy_difference(set1, set2):
    return np.minimum(set1, 1 - set2)

# Function to perform Cartesian product of two fuzzy sets
def cartesian_product(set1, set2):
    cartesian_result = np.zeros((len(set1), len(set2)))
    for i in range(len(set1)):
        for j in range(len(set2)):
            cartesian_result[i][j] = min(set1[i], set2[j])
    return cartesian_result

# Function to perform max-min composition on two fuzzy relations
def max_min_composition(relation1, relation2):
    composition_result = np.zeros((len(relation1), len(relation2[0])))
    for i in range(len(relation1)):
        for j in range(len(relation2[0])):
            max_min = 0
            for k in range(len(relation2)):
                max_min = max(max_min, min(relation1[i][k], relation2[k][j]))
            composition_result[i][j] = max_min
    return composition_result

# Example usage
set1 = np.array([0.2, 0.5, 0.8])
set2 = np.array([0.4, 0.6, 0.7])

# Union
print("Union:", fuzzy_union(set1, set2))

# Intersection
print("Intersection:", fuzzy_intersection(set1, set2))

# Complement
print("Complement of set1:", fuzzy_complement(set1))

# Difference
print("Difference of set1 and set2:", fuzzy_difference(set1, set2))

# Cartesian product
print("Cartesian product of set1 and set2:")
print(cartesian_product(set1, set2))

# Max-min composition
relation1 = np.array([[0.2, 0.5], [0.4, 0.3]])
relation2 = np.array([[0.6, 0.2], [0.1, 0.8]])
print("Max-min composition of relation1 and relation2:")
print(max_min_composition(relation1, relation2))