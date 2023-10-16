def get_eular_totient(n):
    phi = [0] * (n + 1)
    phi[0] = 0
    phi[1] = 1
    for i in range(2, n + 1):
        phi[i] = i - 1

    for i in range(2, n + 1):
        for j in range(2 * i, n + 1, i):
            phi[j] -= phi[i]
