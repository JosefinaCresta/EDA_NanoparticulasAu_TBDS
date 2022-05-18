import scipy.stats as ss
import statsmodels.api as sm
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
from matplotlib import style
import seaborn as sns
import pandas as pd
import numpy as np
import random 


def Test_Normalidad(data, col):
    '''
    Objetivo: Test de normalidad a la variable col del dataframe data.
    
    args.
    -----
    data: Dataframe
    col: String. Nombre de la columna a analizar
    -----
    ------
    ----
    '''
    serie=data[col]
    # Test de D'Agostino's K2
    # ==============================================================================
    k2, p_value = ss.normaltest(serie)
    print("D'Agostino's K2 test:")
    print(f"\t Estadístico = {k2}, p-value = {p_value}")
    
    alpha=0.05
    if p_value <= alpha:
        print(f"P_Valor < 0.05 -> Se rechaza H0 \n\t  No es posible asegurar que {col} sigue una distribución normal.")
    else:
        print(f"P_Valor > 0.05 -> Se acepta H0 \n\t   Es posible asegurar que {col} sigue una distribución normal.")
    print("*"*80)   

    # Histograma + curva normal teórica
    # ==============================================================================
    # Valores de la media (mu) y desviación típica (sigma) de los datos
    mu, sigma = ss.norm.fit(serie)

    # Valores teóricos de la normal en el rango observado
    x = np.linspace(min(serie), max(serie), num=100)
    y = ss.norm.pdf(x, mu, sigma)

    # Gráfico
    fig, ax = plt.subplots(figsize=(7,4))
    ax.plot(x, y, linewidth=2, color="red", label='normal teórica')
    ax.hist(x=serie, density=True, bins=80, color="#3182bd", alpha=0.5)
    ax.set_title(f'Distribución de {col}')
    ax.set_xlabel(f'{col}')
    ax.set_ylabel('Densidad de probabilidad')
    ax.legend()
    # Gráfico Q-Q
    # ==============================================================================
    fig, ax = plt.subplots(figsize=(7,4))
    sm.qqplot(serie, fit = True, line="s", color="blue", alpha = 0.4, lw = 2, ax= ax)
    ax.set_title(f'Gráfico Q-Q de {col}', fontsize = 10, fontweight = "bold")
    ax.tick_params(labelsize = 7)

# ============================================================ # ============================================================

def Detectar_Outliers(data, col):
    '''
    Objetivo: Detección de valores atipicos, y creación de dataframe sin los mismos. 
    
    args.
    -----
    data: Dataframe
    col: String. Nombre de la columna a analizar
    -----
    ---------
    ----
    '''
    # accept a dataframe, remove outliers, return cleaned data in a new dataframe

    # Cálculo de IQR
    # ============================================================
    serie=data[col]
    q1 = serie.quantile(0.25)
    q3 = serie.quantile(0.75)
    iqr = q3-q1

    # Cálculo de los limites
    # ============================================================
    #lim_inf  = serie.mean() - 3*serie.std()
    #lim_sup = serie.mean() + 3*serie.std()
    lim_inf  = q1-1.5*iqr
    lim_sup = q3+1.5*iqr


    # Creación data set de outliers
    # ============================================================
    print("*"*80)   
    df_out = data.loc[(serie < lim_inf) | (serie > lim_sup)]
    len=df_out.shape[0]
    print(f"Se encontraron {len} outliers de {col}")
    print("*"*80)   

    # Creación nuevo data set sin outliers
    # ============================================================
    df=data.copy()
    df[col]=serie
    df = data.loc[(serie > lim_inf) & (serie < lim_sup)]

    #Comparación graficos de caja antes y despues de eliminar Outliers
    # ============================================================
    plt.figure(figsize=(16,8))
    plt.subplot(2,2,1)
    sns.distplot(data[col])
    plt.subplot(2,2,2)
    sns.boxplot(data[col])
    plt.subplot(2,2,3)
    sns.distplot(df[col])
    plt.subplot(2,2,4)
    sns.boxplot(df[col])
    plt.show()
    
    return df

# ============================================================ # ============================================================
 
def Media_Muestral(data, col, tamaño_muestral, cant_muestras):
    '''
    Objetivo: Selección de muestras aleatorias, calculo de media muestral y su error estandar
    
    args.
    -----
    data: Dataframe
    col: String. Nombre de la columna a analizar
    tamaño_muestral : int
    cant_muestras : int
    -----
    ---------
    ----
    '''
    medias = np.array([np.mean(data[data[col]<len(data[col])].sample(tamaño_muestral)[col].values)for i in range(cant_muestras)])
    print("*"*80)  
    media_de_medias_muestrales = medias.mean()
    print(f"Media Muestral de {col}: ", media_de_medias_muestrales)
    error_estandar = data[col].std()/np.sqrt(tamaño_muestral)
    print("Error Estandar: ", error_estandar)
    print("*"*80)  

    sns.distplot(medias)
    plt.title(f"Distribución de las Medias Muestrales de {col}")
    plt.xlabel(f"Medias de muestras de {col}", labelpad=14)
    plt.ylabel("Frecuencia", labelpad=14);

# ============================================================ # ============================================================
 
def hipotesisCorrelación(data, col1, col2):
    '''
    Objetivo: Analisis de correlación entre dos variables
    
    args.
    -----
    data: Dataframe
    col1, col2: String. Nombre de las columnas a analizar
    -----
    ---------
    ----
    '''
    print("Hipótesis")
    print(f"\t Nula (H0): No exite relación entre {col1} y {col2}")
    print(f"\t Alternativa (HA): Sí exite relación entre {col1} y {col2}")
    print("_"*40)
    print("Nota: \n\tSe utiliza un nivel de confianza del 95%")
    print("\tEs decir que si se obtiene  p_valor < 0.05:")
    print("\tSe rechaza la H0 y existe una correlación significativa.")
    print("\tEn caso contrario no es posible afirmar que la correlación difiera significativamente de 0.")
    print("_"*40)

    # Cálculo de correlación y significancia con Scipy
    # ==============================================================================
    print("Coeficientes correlación y P_values")
    r, p = ss.spearmanr(data[col1], data[col2])
    print(f"\tDe Spearman: r={r}, p-value={p}")
    
     # Gráfico distribución variables
    # ==============================================================================
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20,5))

    axs[0].hist(x=data[col1], bins=20, color="#3182bd", alpha=0.5)
    axs[0].set_title(f'Distribución de {col1}')
    axs[0].set_xlabel(col1)
    axs[0].set_ylabel('Densidad de probabilidad')

    axs[2].hist(x=data[col2], bins=20, color="#3182bd", alpha=0.5)
    axs[2].set_title(f'Distribución de {col2}')
    axs[2].set_xlabel(col2)
    axs[2].set_ylabel('Densidad de probabilidad')

    axs[1].scatter(x=data[col1], y=data[col2], alpha= 0.8)
    title=f'{col1} vs {col2}'
    axs[1].set_title(title)
    axs[1].set_xlabel(col1)
    axs[1].set_ylabel(col2)

    #Conclusión test de Hipotesis
    # ==============================================================================
    print("*"*80)
    alpha=0.05
    if p <= alpha:
        print(f"Se rechaza H0 \n\t Exite correlación significativa entre {col1} y {col2}")
    else:
        print(f"Se acepta H0 \n\t No es posible afirmar correlación significativa entre {col1} y {col2}")
    print("*"*80)   

    # beta=0.05
    # if r <= alpha:
    #     print(f"Se rechaza H0 \n\t Exite correlación significativa entre {col1} y {col2}")
    # else:
    #     print(f"Se acepta H0 \n\t No es posible afirmar correlación significativa entre {col1} y {col2}")
    # print("*"*80)  
        