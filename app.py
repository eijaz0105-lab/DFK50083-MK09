import streamlit as st



st.title("Kalkulator BMI Klinik")



berat_input = st.text_input("Masukkan berat (kg):")
tinggi_input = st.text_input("Masukkan tinggi (meter):")



if st.button("Kira BMI"):

    try:
       
        berat = float(berat_input)
        tinggi = float(tinggi_input)

        # Pengiraan BMI
        bmi = berat / (tinggi * tinggi)

    except ValueError:
        st.error("Sila masukkan nombor yang sah untuk berat dan tinggi.")

    except ZeroDivisionError:
        st.error("Tinggi tidak boleh bernilai 0.")

    except Exception as e:
        st.error("Ralat yang tidak dijangka telah berlaku.")

    else:
        st.success(f"BMI pesakit ialah: {bmi:.2f}")

    finally:
        st.info("Sistem selesai memproses permintaan anda.")


# Bahagian rekod pesakit
st.subheader("Rekod Pesakit")


if st.button("Papar Rekod Lama"):

    try:
        with open("rekod_pesakit.txt", "r") as fail:
            rekod = fail.read()

        st.text(rekod)

    except FileNotFoundError:
        st.warning("Fail rekod belum diwujudkan")