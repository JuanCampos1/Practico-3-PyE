from scipy.stats import binom

class DistribucionBinomial:
    def __init__(self, n, p):
        self.n = n
        self.p = p

    def generar_muestras(self, tamaño):
        return binom.rvs(self.n, self.p, size=tamaño)