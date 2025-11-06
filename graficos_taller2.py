# graficos_taller2.py
# Genera gráficos a partir de los resultados medidos en el Taller 2 (Complejidad Algorítmica)

import pandas as pd
import matplotlib.pyplot as plt
import math

# === 1. Cargar datos ===
archivo_csv = "resultados_taller2.csv"
df = pd.read_csv(archivo_csv, encoding="latin1")

print("Datos cargados correctamente:")
print(df.head())

# === 2. Gráfico: Tiempo promedio vs tamaño (escala lineal) ===
plt.figure(figsize=(8,5))
for algoritmo in df["Algoritmo"].unique():
    sub = df[df["Algoritmo"] == algoritmo]
    plt.plot(sub["Tamaño_n"], sub["Tiempo_promedio_s"], marker="o", label=algoritmo)

plt.title("Comparación de tiempo de ejecución (escala lineal)")
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Tiempo promedio (s)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("grafico_tiempo_lineal.png", dpi=300)
plt.show()

# === 3. Gráfico: Tiempo vs tamaño (escala log-log) ===
plt.figure(figsize=(8,5))
for algoritmo in df["Algoritmo"].unique():
    sub = df[df["Algoritmo"] == algoritmo]
    plt.plot(sub["Tamaño_n"], sub["Tiempo_promedio_s"], marker="o", label=algoritmo)

plt.xscale("log")
plt.yscale("log")
plt.title("Crecimiento asintótico (escala log-log)")
plt.xlabel("log(n)")
plt.ylabel("log(Tiempo)")
plt.legend()
plt.grid(True, which="both", linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("grafico_tiempo_loglog.png", dpi=300)
plt.show()

# === 4. Gráfico: Memoria promedio vs tamaño ===
plt.figure(figsize=(8,5))
for algoritmo in df["Algoritmo"].unique():
    sub = df[df["Algoritmo"] == algoritmo]
    plt.plot(sub["Tamaño_n"], sub["Memoria_KB"], marker="s", label=algoritmo)

plt.title("Consumo de memoria promedio")
plt.xlabel("Tamaño de entrada (n)")
plt.ylabel("Memoria (KB)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("grafico_memoria.png", dpi=300)
plt.show()

print("\nGráficos generados y guardados como:")
print(" - grafico_tiempo_lineal.png")
print(" - grafico_tiempo_loglog.png")
print(" - grafico_memoria.png")