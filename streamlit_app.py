# ---------------------------------------
# Metode Bisection
# SPNL (Satu Persamaan Non Linear)
# Nama   : Kelvin
# ---------------------------------------



    c = a

    print("\nIterasi |   a    |   b    |   c    |  f(c)")
    print("--------------------------------------------")

    while abs(f(c)) > tol:
        c = (a + b) / 2
        iterasi += 1

        print(f"{iterasi:7} | {a:.4f} | {b:.4f} | {c:.4f} | {f(c):.6f}")

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nAkar persamaan ditemukan!")
    print("Akar =", c)
    print("Jumlah iterasi =", iterasi)
