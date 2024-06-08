import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import mode

class AnalisisDistribucion:
    def __init__(self, muestras, nombre_distribucion):
        self.muestras = muestras
        self.nombre_distribucion = nombre_distribucion
    
    def diagrama_cajas(self):
        plt.figure(figsize=(12, 8))
        sns.boxplot(data=[self.muestras[tamaño] for tamaño in self.muestras])
        plt.xticks(ticks=np.arange(len(self.muestras)), labels=[str(tamaño) for tamaño in self.muestras])
        plt.xlabel('Tamaño de la muestra')
        plt.ylabel('Valores de la muestra')
        plt.title(f'Diagramas de Cajas para {self.nombre_distribucion}')
        plt.show()
        
    def histogramas(self):
        num_muestras = len(self.muestras)
        fig, axes = plt.subplots(num_muestras, 1, figsize=(12, 3 * num_muestras))
        
        if num_muestras == 1:
            axes = [axes]  # Ensure axes is iterable
        
        for ax, (tamaño, muestra) in zip(axes, self.muestras.items()):
            unique_values = np.unique(muestra)
            bins = np.arange(min(unique_values) - 0.5, max(unique_values) + 1.5)
            sns.histplot(muestra, bins=bins, kde=False, ax=ax)  # Set kde=False to remove the blue line
            ax.set_title(f'Histograma para {self.nombre_distribucion} con tamaño {tamaño}')
            ax.set_xlabel('Valores de la muestra')
            ax.set_ylabel('Frecuencia')
        
        plt.tight_layout()
        plt.show()
    
    def calcular_estadisticas(self):
        estadisticas = {}
        for tamaño in self.muestras:
            muestra = self.muestras[tamaño]
            mediana = np.median(muestra)
            moda_result = mode(muestra, keepdims=False)
            moda = moda_result.mode[0] if isinstance(moda_result.mode, np.ndarray) else moda_result.mode
            media = np.mean(muestra)
            varianza = np.var(muestra, ddof=1)  # Usamos ddof=1 para obtener la varianza muestral
            estadisticas[tamaño] = {
                'mediana': mediana,
                'moda': moda,
                'media': media,
                'varianza': varianza
            }
        return estadisticas
    
    def comparar_con_teorico(self, media_teorica, varianza_teorica):
        estadisticas = self.calcular_estadisticas()
        print(f'\nAnálisis para {self.nombre_distribucion}:')
        for tamaño in estadisticas:
            print(f'Tamaño de muestra {tamaño}:')
            print(f'  Media empírica = {estadisticas[tamaño]["media"]}, Esperanza teórica = {media_teorica}')
            print(f'  Varianza empírica = {estadisticas[tamaño]["varianza"]}, Varianza teórica = {varianza_teorica}')
            print(f'  Mediana: {estadisticas[tamaño]["mediana"]}')
            print(f'  Moda: {estadisticas[tamaño]["moda"]}')
