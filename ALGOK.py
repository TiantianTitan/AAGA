def knuth_random_generator(X):
    # Etape 1: Calculez Y = ⌊X / 10^9⌋
    Y = X // 10**9

    # Répéter les étapes 2 à 13 exactement (Y+1) fois
    for _ in range(Y + 1):
        # Etape 2: Calculez Z = ⌊X / 10^8⌋ mod 10
        Z = (X // 10**8) % 10

        # Aller directement à l'étape (3 + Z)
        step = 3 + Z

        while True:
            if step == 3:
                # Etape 3: Si X < 5·10^9, alors X = X + 5·10^9
                if X < 5 * 10**9:
                    X += 5 * 10**9
                step = 4

            elif step == 4:
                # Etape 4: X = ⌊X² / 10^5⌋ mod 10^10
                X = (X**2 // 10**5) % 10**10
                step = 5

            elif step == 5:
                # Etape 5: X = (1001001001 · X) mod 10^10
                X = (1001001001 * X) % 10**10
                step = 6

            elif step == 6:
                # Etape 6: Si X < 10^8, alors X = X + 9814055677. Sinon, X = 10^10 - X
                if X < 10**8:
                    X += 9814055677
                else:
                    X = 10**10 - X
                step = 7

            elif step == 7:
                # Etape 7: Inverser les 5 digits de poids fort avec les 5 de poids faible
                X = 10**5 * (X % 10**5) + X // 10**5
                step = 8

            elif step == 8:
                # Etape 8: X = (1001001001 · X) mod 10^10
                X = (1001001001 * X) % 10**10
                step = 9

            elif step == 9:
                # Etape 9: Décrémenter chaque digit strictement positif de 1
                X = int(''.join(str(int(d) - 1) if d != '0' else '0' for d in str(X)))
                step = 10

            elif step == 10:
                # Etape 10: Si X < 10^5, alors X = X^2 + 99999. Sinon, X = X - 99999
                if X < 10**5:
                    X = X**2 + 99999
                else:
                    X -= 99999
                step = 11

            elif step == 11:
                # Etape 11: Tant que X < 10^9, X = 10 · X
                while X < 10**9:
                    X *= 10
                step = 12

            elif step == 12:
                # Etape 12: X = ⌊X · (X − 1) / 10^5⌋ mod 10^10
                X = (X * (X - 1) // 10**5) % 10**10
                step = 13

            elif step == 13:
                # Etape 13: Si Y > 0, alors Y = Y − 1 et retournez à l’étape 2. Sinon l’algorithme se termine
                if Y > 0:
                    Y -= 1
                    Z = (X // 10**8) % 10
                    step = 3 + Z
                else:
                    return X

# Exemple d'utilisation
X_initial = 1234567890  # Vous pouvez changer cette valeur de départ
print(knuth_random_generator(X_initial))
