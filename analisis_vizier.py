import pandas as pd
import matplotlib.pyplot as plt


# Lectura del resultado entregado directamente por VizieR.
datos = pd.read_csv("datos/gaia_allwise_crudo.csv")

print("Filas descargadas:", len(datos))
print("Fuentes Gaia diferentes:", datos["Source"].nunique())

# Las columnas necesarias se convierten a numeros. Si aparece un valor no valido,
# pandas lo convierte en NaN para poder eliminarlo durante la limpieza.
columnas_numericas = ["Plx", "e_Plx", "pmRA", "pmDE", "Gmag", "W1mag"]
for columna in columnas_numericas:
    datos[columna] = pd.to_numeric(datos[columna], errors="coerce")

# Una paralaje detectada con al menos tres veces su error permite separar fuentes
# con una medicion estelar confiable de objetos extragalacticos muy lejanos.
estrellas = datos.dropna(subset=["Plx", "e_Plx", "Gmag", "W1mag"]).copy()
estrellas = estrellas[(estrellas["Plx"] > 0) &
                      (estrellas["e_Plx"] > 0) &
                      (estrellas["Plx"] / estrellas["e_Plx"] >= 3)].copy()

# Si una fuente de Gaia tiene mas de una coincidencia AllWISE dentro de 2 segundos
# de arco, se conserva una sola fila para no repetirla en la grafica.
estrellas = estrellas.drop_duplicates(subset="Source")
estrellas["G-W1"] = estrellas["Gmag"] - estrellas["W1mag"]

print("Estrellas galacticas con fotometria completa:", len(estrellas))
print(estrellas[["Plx", "pmRA", "pmDE", "Gmag", "W1mag", "G-W1"]].describe())

estrellas.to_csv("resultados/gaia_allwise_limpio.csv", index=False)

plt.figure(figsize=(8, 6))
plt.scatter(estrellas["G-W1"], estrellas["Gmag"], s=12,
            color="darkorange", alpha=0.65)
plt.gca().invert_yaxis()
plt.xlabel("Indice de color G - W1 (mag)")
plt.ylabel("Magnitud G de Gaia (mag)")
plt.title("Diagrama color-magnitud: estrellas del campo profundo")
plt.grid(alpha=0.25)
plt.tight_layout()
plt.savefig("resultados/diagrama_color_magnitud.png", dpi=150)
plt.show()
