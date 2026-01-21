# ---------------------------------------
# Metode Bisection
# SPNL (Satu Persamaan Non Linear)
# Nama   : Kelvin
# ---------------------------------------



# Cek syarat metode bisection
if f(a) * f(b) > 0:
    print("Metode bisection tidak bisa digunakan!")
    print("f(a) dan f(b) harus berlainan tanda.")

        print(f"{iterasi:7} | {a:.4f} | {b:.4f} | {c:.4f} | {f(c):.6f}")

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("\nAkar persamaan ditemukan!")
    print("Akar =", c)
    print("Jumlah iterasi =", iterasi)
