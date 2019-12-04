def double(number):
    return number*2
	
    



# Pas touche!
tests = (
    (2, 4),
    (7, 14),
    (0, 0),
    (-3, -6),
)

for test in tests:
    print(f"L'appel  double({test[0]})  renvoie: {double(test[0])} (résultat attendu: {test[1]})")
