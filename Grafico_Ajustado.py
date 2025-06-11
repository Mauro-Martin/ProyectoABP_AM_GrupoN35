import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# DATOS HISTÓRICOS
years = np.array([1970, 1980, 1991, 2001, 2010, 2022])
population = np.array([2086850, 2407754, 2766683, 3066801, 3308876, 3840905])
proj_years = np.array([2032, 2042])

# MODELO LINEAL
linear_coef = np.polyfit(years, population, 1)
linear_model = np.poly1d(linear_coef)
linear_proj = linear_model(proj_years)

# MODELO EXPONENCIAL
def exp_model(x, a, b):
    return a * np.exp(b * x)

exp_params, _ = curve_fit(exp_model, years, population, p0=(1e5, 0.01))
exp_proj = exp_model(proj_years, *exp_params)

# MODELO LOGÍSTICO
def logistic_model(x, L, k, x0):
    return L / (1 + np.exp(-k * (x - x0)))

try:
    logistic_params, _ = curve_fit(logistic_model, years, population, p0=[10000000, 0.03, 2000])
    logistic_proj = logistic_model(proj_years, *logistic_params)
    logistic_ok = True
except:
    logistic_ok = False

# GRAFICAR
plt.figure(figsize=(10, 6))
plt.scatter(years, population, label="Datos censales", color="black")
plt.plot(years, linear_model(years), label="Modelo lineal", color="blue")
plt.plot(years, exp_model(years, *exp_params), label="Modelo exponencial", color="green")
plt.scatter(proj_years, linear_proj, color="blue", marker="x", label="Proy. lineal")
plt.scatter(proj_years, exp_proj, color="green", marker="x", label="Proy. exponencial")
if logistic_ok:
    plt.plot(years, logistic_model(years, *logistic_params), label="Modelo logístico", color="red")
    plt.scatter(proj_years, logistic_proj, color="red", marker="x", label="Proy. logístico")

plt.xlabel("Año")
plt.ylabel("Población")
plt.title("Proyección de la población en Córdoba")
plt.legend()
plt.grid(True)

grafico_path = "grafico_modelos.png"
plt.savefig(grafico_path)
plt.close()

print(f"✅ Gráfico generado y guardado como: {grafico_path}")