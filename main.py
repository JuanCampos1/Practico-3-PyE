from distribucion_binomial import DistribucionBinomial
from distribucion_geometrica import DistribucionGeometrica
from distribucion_poisson import DistribucionPoisson
from analisis_distribucion import AnalisisDistribucion

# Parámetros de la distribución binomial
n = 100
p_binom = 0.35
tamaños = [100, 1000, 10000, 100000]

# Crear una instancia de DistribucionBinomial y generar muestras
dist_binom = DistribucionBinomial(n, p_binom)
muestras_binom = {tamaño: dist_binom.generar_muestras(tamaño) for tamaño in tamaños}

# Crear una instancia de AnalisisDistribucion y realizar análisis
analisis_binom = AnalisisDistribucion(muestras_binom, "Distribución Binomial")

# Análisis para Distribución Binomial
analisis_binom.diagrama_cajas()
analisis_binom.histogramas()
esperanza_teorica_binom = n * p_binom
varianza_teorica_binom = n * p_binom * (1 - p_binom)
analisis_binom.comparar_con_teorico(esperanza_teorica_binom, varianza_teorica_binom)

# Parámetros de la distribución geométrica
p_geom = 0.08

# Crear una instancia de DistribucionGeometrica y generar muestras
dist_geom = DistribucionGeometrica(p_geom)
muestras_geom = {tamaño: dist_geom.generar_muestras(tamaño) for tamaño in tamaños}

# Crear una instancia de AnalisisDistribucion y realizar análisis
analisis_geom = AnalisisDistribucion(muestras_geom, "Distribución Geométrica")

# Análisis para Distribución Geométrica
analisis_geom.diagrama_cajas()
analisis_geom.histogramas()
esperanza_teorica_geom = 1 / p_geom
varianza_teorica_geom = (1 - p_geom) / (p_geom**2)
analisis_geom.comparar_con_teorico(esperanza_teorica_geom, varianza_teorica_geom)

# Parámetros de la distribución de Poisson
lam_poisson = 30

# Crear una instancia de DistribucionPoisson y generar muestras
dist_poisson = DistribucionPoisson(lam_poisson)
muestras_poisson = {tamaño: dist_poisson.generar_muestras(tamaño) for tamaño in tamaños}

# Crear una instancia de AnalisisDistribucion y realizar análisis
analisis_poisson = AnalisisDistribucion(muestras_poisson, "Distribución de Poisson")

# Análisis para Distribución de Poisson
analisis_poisson.diagrama_cajas()
analisis_poisson.histogramas()
esperanza_teorica_poisson = lam_poisson
varianza_teorica_poisson = lam_poisson
analisis_poisson.comparar_con_teorico(esperanza_teorica_poisson, varianza_teorica_poisson)
