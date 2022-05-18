def Test_Normalidad(data, col):
    serie=data[col]
    # D'Agostino's K-squared test
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
    x_hat = np.linspace(min(serie), max(serie), num=100)
    y_hat = ss.norm.pdf(x_hat, mu, sigma)

    # Gráfico
    fig, ax = plt.subplots(figsize=(7,4))
    ax.plot(x_hat, y_hat, linewidth=2, color="red", label='normal teórica')
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