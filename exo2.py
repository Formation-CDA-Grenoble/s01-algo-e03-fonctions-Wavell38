def conditionalDouble(number):
    return number if number < 1 else (number*2)



# Pas touche!
tests = (
    (2, 4),
    (7, 14),
    (0, 0),
    (-3, -3),
)

for test in tests:
    print(f"L'appel  conditionalDouble({test[0]})  renvoie: {conditionalDouble(test[0])} (résultat attendu: {test[1]})")
