# Diseccion de un campo profundo multi-longitud de onda

Campo centrado en **RA = 135.5 grados**, **Dec = 0.5 grados**, con radio de **0.5 grados**.

<details>
<summary><strong>Estudiante A: El Cartografo Galactico (VizieR)</strong></summary>

### Consulta y procesamiento

El pipeline consulta directamente el servicio TAP de VizieR mediante ADQL. Gaia DR3 se conserva como catalogo principal y se cruza con AllWISE usando un `LEFT JOIN` y un radio de coincidencia de 2 segundos de arco.

Una paralaje positiva por si sola puede aparecer por ruido. Para seleccionar estrellas de la Via Lactea se conservaron fuentes con paralaje positiva y con una relacion `Plx/e_Plx >= 3`. Para el diagrama tambien se eliminaron las filas sin `Gmag` o sin `W1mag`.

El indice de color se calcula como:

```text
G - W1 = Gmag - W1mag
```

La magnitud `Gmag` se representa en el eje vertical invertido, porque en la escala de magnitudes los objetos mas brillantes tienen valores menores.

### Archivos

- `consulta_vizier.sh`: consulta ADQL escrita y enviada con `wget`.
- `analisis_vizier.py`: limpieza con pandas y grafica con matplotlib.
- `proyecto_estudiante_a.ipynb`: cuaderno para ejecutar el trabajo en Google Colab.
- `resultados/diagrama_color_magnitud.png`: diagrama color-magnitud obtenido.
- `resultados/gaia_allwise_limpio.csv`: muestra final usada para la grafica.

### Ejecucion

```bash
bash consulta_vizier.sh
python3 analisis_vizier.py
```

En Google Colab se debe abrir `proyecto_estudiante_a.ipynb` y ejecutar las celdas en orden.

</details>

<details>
<summary><strong>Estudiante B: El Cosmologo (SDSS y MAST)</strong></summary>

TODO: agregar la consulta a SDSS, el analisis de galaxias y cuasares, y la exploracion de observaciones en MAST.

</details>

<details>
<summary><strong>Analisis de resultados</strong></summary>

![Diagrama color-magnitud optico-infrarrojo](resultados/diagrama_color_magnitud.png)

El cruce optico-infrarrojo permite comparar la emision registrada por Gaia con la emision a mayor longitud de onda registrada por AllWISE. Los distintos valores de `G-W1` reflejan diferencias de temperatura y tambien pueden mostrar el efecto del polvo, que atenúa con mayor intensidad la luz optica que la infrarroja.

En la ejecucion realizada se obtuvieron **1.884 estrellas galacticas con fotometria completa**. En el diagrama se observa una secuencia estelar inclinada: las fuentes de menor magnitud G, es decir las mas brillantes, tienden a presentar colores `G-W1` menores; la poblacion mas tenue se concentra aproximadamente entre `G-W1 = 3` y `G-W1 = 4`. Los puntos mas alejados de la secuencia pueden corresponder a fuentes con propiedades fisicas distintas o a objetos afectados por polvo.

</details>
