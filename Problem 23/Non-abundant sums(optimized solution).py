def divisors(nb, extremum = False):
    divisors = []
    inf = 1 if extremum else 2
    for i in range(inf, int(nb**0.5)+1):
        q, r = divmod(nb, i)
        if r == 0:
            if q >= i:
                divisors.append(i)
                if q > i:
                    divisors.append(nb//i)
    return divisors

def is_abundant(n):
    return sum(divisors(n))+1 > n

#Génération d'une liste contenant tous les nombres abondants
#inférieurs à 28124
abundants = [i for i in range(2, 28124) if is_abundant(i)]

sommes = {}
#Génération de toutes les sommes possibles de 2 nombres abondants
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        somme = abundants[i] + abundants[j]
        if somme > 28123:
            break
        sommes[somme] = 1
#Différence entre la somme de tous les nombres et la somme
#de toutes les sommes de 2 nombres abondants
resultat = (28123*28124)//2 - sum(sommes.keys())
print(resultat)
