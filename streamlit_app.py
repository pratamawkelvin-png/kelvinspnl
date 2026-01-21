import streamlit as st

st.title("Metode Bisection - SPNL")

def f(x):
    return x**2 - 4

a = st.number_input("Masukkan batas bawah (a)")
b = st.number_input("Masukkan batas atas (b)")
tol = st.number_input("Masukkan toleransi error", value=0.0001)

if st.button("Hitung Akar"):
    if f(a) * f(b) > 0:
        st.error("Metode bisection tidak bisa digunakan! f(a) dan f(b) harus berlainan tanda.")
    else:
        iterasi = 0
        st.write("Iterasi | a | b | c | f(c)")

        while (b - a) / 2 > tol:
            c = (a + b) / 2
            iterasi += 1

            st.write(f"{iterasi} | {a:.4f} | {b:.4f} | {c:.4f} | {f(c):.6f}")

            if f(a) * f(c) < 0:
                b = c
            else:
                a = c

        st.success(f"Akar ditemukan: {round(c,6)}")
        st.info(f"Jumlah iterasi: {iterasi}")

