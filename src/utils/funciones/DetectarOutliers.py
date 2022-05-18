def Detectar_Outliers(data, col):
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