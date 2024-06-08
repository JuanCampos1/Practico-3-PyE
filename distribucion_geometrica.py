from scipy.stats import geom

class DistribucionGeometrica:
    def __init__(self, p):
        self.p = p

    def generar_muestras(self, tamaño):
        return geom.rvs(self.p, size=tamaño)