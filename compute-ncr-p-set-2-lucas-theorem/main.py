def nCrModpLucasV1(n, r, p):
    def nCrModpDP(N, K, P):
        C = [0] * (N + 1)
        C[0] = 1
        for n in range(1, N + 1):
            k = min(n, K)
            while k > 0:
                C[k] = (C[k] + C[k - 1]) % P
                k -= 1
        return C[K]

    def nCrModpLucas(n, r, p):
        if r == 0:
            return 1

        next = nCrModpLucas(n // p, r // p, p)
        cr = nCrModpDP(n % p, r % p, p)
        return (next * cr) % p

    return nCrModpLucas(n, r, p)


# -----------------------

n = 1000
r = 900
p = 13
assert nCrModpLucasV1(n, r, p) == 8
