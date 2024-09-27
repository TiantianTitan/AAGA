def knuth_random(X):
    # Vérification que X a bien 10 chiffres
    if not (0 <= X < 10**10):
        raise ValueError("X doit être un entier sur 10 chiffres décimaux.")
    
    while True:
        Y = X // 10**9  # Étape 1
        for _ in range(Y + 1):  # Étapes 2 à 13
            Z = (X // 10**8) % 10  # Étape 2
            step = 3 + Z  # Aller à l'étape 3 + Z

            if X < 5 * 10**9:  # Étape 3
                X += 5 * 10**9

            # Étape 4
            X = (X**2 // 10**5) % 10**10

            # Étape 5
            X = (1001001001 * X) % 10**10

            # Étape 6
            if X < 10**8:
                X += 9814055677
            else:
                X = 10**10 - X

            # Étape 7
            X = (10**5 * (X % 10**5)) + (X // 10**5)

            # Étape 8
            X = (1001001001 * X) % 10**10

            # Étape 9
            X = sum(max(digit - 1, 0) * 10**i for i, digit in enumerate(map(int, str(X)[::-1])))

            # Étape 10
            if X < 10**5:
                X = X**2 + 99999
            else:
                X -= 99999

            # Étape 11
            while X < 10**9:
                X *= 10

            # Étape 12
            X = (X * (X - 1) // 10**5) % 10**10

        # Étape 13
        if Y > 0:
            Y -= 1
        else:
            break  # Fin de l'algorithme

    return X  # Retourner la valeur finale de X
