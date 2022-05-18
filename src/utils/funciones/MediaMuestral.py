def Media_Muestral(data, col, tamaño_muestral, cant_muestras):
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