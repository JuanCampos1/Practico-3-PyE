from scipy.stats import poisson

class DistribucionPoisson:
    def __init__(self, lam):
        self.lam = lam

    def generar_muestras(self, tamaño):
        return poisson.rvs(self.lam, size=tamaño)