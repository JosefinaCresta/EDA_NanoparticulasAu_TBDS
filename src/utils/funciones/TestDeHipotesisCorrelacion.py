def hipotesisCorrelación(data, col1, col2):
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
    r, p = stats.spearmanr(data[col1], data[col2])
    print(f"\tDe Spearman: r={r}, p-value={p}")
    
     # Gráfico distribución variables
    # ==============================================================================
    fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(20,5))

    axs[0].hist(x=data[col1], bins=20, color="#3182bd", alpha=0.5)
    axs[0].set_title(f'Distribución de {col1}')
    axs[0].set_xlabel(col1)
    axs[0].set_ylabel('counts')

    axs[2].hist(x=data[col2], bins=20, color="#3182bd", alpha=0.5)
    axs[2].set_title(f'Distribución de {col2}')
    axs[2].set_xlabel(col2)
    axs[2].set_ylabel('counts')

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
    