def cascadeDouble(list):
    for idx, val in enumerate(list):
    	list[idx] = val * 2
    return list

# Pas touche!
tests = (
    ([1, 2, 3], [2, 4, 6]),
    ([10], [20]),
    ([1, 1, 1, 1, 1], [2, 2, 2, 2, 2]),
    ([-12, 0, 50], [-24, 0, 100]),
)

for test in tests:
    print(f"L'appel  cascadeDouble({test[0]})  renvoie: {cascadeDouble(test[0])} (résultat attendu: {test[1]})")
