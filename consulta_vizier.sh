#!/bin/bash

echo "Consultando Gaia DR3 y AllWISE en VizieR..."

ADQL="SELECT g.Source, g.RA_ICRS, g.DE_ICRS, g.Plx, g.e_Plx, g.pmRA, g.pmDE, g.Gmag, w.AllWISE, w.W1mag FROM \"I/355/gaiadr3\" AS g LEFT JOIN \"II/328/allwise\" AS w ON 1=CONTAINS(POINT('ICRS', w.RAJ2000, w.DEJ2000), CIRCLE('ICRS', g.RA_ICRS, g.DE_ICRS, 2./3600.)) WHERE 1=CONTAINS(POINT('ICRS', g.RA_ICRS, g.DE_ICRS), CIRCLE('ICRS', 135.5, 0.5, 0.5))"

# Se reemplazan los espacios para poder enviar la consulta dentro de la URL.
URL_ADQL=$(echo "$ADQL" | sed 's/ /+/g')
TAP_URL="https://tapvizier.cds.unistra.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="
TAP_RESPALDO="https://tapvizier.u-strasbg.fr/TAPVizieR/tap/sync?request=doQuery&lang=ADQL&format=csv&query="

mkdir -p datos resultados
wget -q -O datos/gaia_allwise_crudo.csv "$TAP_URL$URL_ADQL"

# Si el servidor principal no responde, se intenta el espejo oficial.
if [ ! -s datos/gaia_allwise_crudo.csv ]; then
    echo "Servidor principal no disponible. Intentando el espejo de VizieR..."
    wget -q -O datos/gaia_allwise_crudo.csv "$TAP_RESPALDO$URL_ADQL"
fi

if [ ! -s datos/gaia_allwise_crudo.csv ]; then
    echo "No fue posible descargar los datos de VizieR."
    exit 1
fi

echo "Consulta terminada: datos/gaia_allwise_crudo.csv"
