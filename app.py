import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Perceptrón Interactivo")

st.title("🧠 Perceptrón Interactivo")
st.write("Ajusta los pesos manualmente y observa cómo aprende")

# Sliders
st.sidebar.header("⚙️ Pesos")

w1 = st.sidebar.slider("Peso w1", -5.0, 5.0, 0.0)
w2 = st.sidebar.slider("Peso w2", -5.0, 5.0, 0.0)
b = st.sidebar.slider("Bias", -5.0, 5.0, 0.0)

# Entradas
st.subheader("🎯 Configuración")

inputs = [(0,0), (0,1), (1,0), (1,1)]
labels = []

for i, (x1, x2) in enumerate(inputs):
    label = st.selectbox(
        f"Salida deseada para ({x1},{x2})",
        [-1, 1],
        key=i
    )
    labels.append(label)

# Función perceptrón
def perceptron(x1, x2):
    suma = w1*x1 + w2*x2 + b
    salida = 1 if suma >= 0 else -1
    return salida, suma

correctos = 0

st.subheader("📊 Resultados")

for i, (x1, x2) in enumerate(inputs):
    salida, suma = perceptron(x1, x2)
    esperado = labels[i]

    if salida == esperado:
        correctos += 1

    st.write(f"Entrada: ({x1},{x2}) → Suma: {round(suma,2)} → Salida: {salida}")

st.success(f"✔ Correctos: {correctos}/4")

# Gráfica
st.subheader("📈 Frontera de decisión")

fig, ax = plt.subplots()

for i, (x1, x2) in enumerate(inputs):
    color = "green" if labels[i] == 1 else "red"
    ax.scatter(x1, x2, c=color, s=100)

x_vals = np.linspace(-1, 2, 100)

if w2 != 0:
    y_vals = -(w1*x_vals + b) / w2
    ax.plot(x_vals, y_vals)

ax.set_xlim(-1,2)
ax.set_ylim(-1,2)
ax.set_xlabel("x1")
ax.set_ylabel("x2")

st.pyplot(fig)