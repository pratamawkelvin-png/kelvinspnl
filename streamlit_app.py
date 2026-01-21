import streamlit as st

# ---------------------------------------
# Metode Bisection
# SPNL (Satu Persamaan Non Linear)
# Nama : Kelvin
# ---------------------------------------

st.title("Metode Bisection - SPNL")

# Definisi fungsi
def f(x):
    return x**2 - 4   # Ubah fungsi di sini jika perlu

# Input
a = st.number_input("Masukkan batas bawah (a)", value=0.0)
b = st.number_input("Masukkan batas atas (b)", value=5.0)
tol = st.number_input("Masukkan toleransi error", value=0.0001, format="%.6f")

# Tombol proses
if st.button("Hitung Akar"):
    if f(a) * f(b) > 0:
        st.error("Metode bisection tidak bisa digunakan karena f(a) dan f(b) bertanda sama.")
    else:
        iterasi = 0
        st.write("Iterasi | a | b | c | f(c)")

        while (b - a) / 2 > tol:
            c = (a + b) / 2
            iterasi += 1

            st.write(
                f"{iterasi} | {a:.4f} | {b:.4f} | {c:.4f} | {f(c):.6f}"
            )

            if f(a) * f(c) < 0:
                b = c
            else:
                a = c

        st.success(f"Akar persamaan ≈ {round(c, 6)}")
        st.info(f"Jumlah iterasi = {iterasi}")


