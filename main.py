import streamlit as st
st.write("""
# Menghitung Indeks Massa Tubuh
Ini adalah aplikasi untuk menghitung Indeks Massa Tubuh menggunakan Streamlit 
Indeks Massa Tubuh adalah metrik standar yang digunakan untuk menentukan siapa saja yang masuk dalam golongan berat badan sehat dan tidak sehat.
BMI = (weight in kilograms / height in meters^2  )
""")
weight = st.number_input("Masukkan weight", 0)
height = st.number_input("Masukkan height", 0)
hitung = st.button("Hitung BMI")

if hitung:
	BMI = weight / ((height/100)**2)
	st.write("Hitungan BMInya adalah ", BMI)
	st.write("BMI < 18,5", Berat Badan Kurang)
	st.write("BMI >= 18,5 <= 22,9", Berat Badan Normal)
	st.write("BMI >= 23 <= 29,9", Berat Badan Berlebih (Obesitas))
	st.write("BMI > 30", Obesitas)