def ejercicio9_1():
    import matplotlib.pyplot as plt

    fig = plt.figure(figsize=(8,6))
    plt.subplot(2, 1, 1) # define la figura de arriba
    plt.plot([0,1,2],[0,1,0]) # dibuja la curva
    plt.xticks([]), plt.yticks([]) # saca las marcas

    plt.subplot(2, 3, 4) # define la primera de abajo, que sería la cuarta si fuera una grilla regular de 2x3
    plt.plot([0,1],[0,1])
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 6) # define la tercera de abajo, que sería la sexta figura si fuera una grilla regular de 2x3
    plt.plot([0,1],[1,0])
    plt.xticks([]), plt.yticks([])

    plt.subplot(2, 3, 5) # define la segunda de abajo, que sería la quinta si fuera una grilla regular de 2x3
    plt.plot([0,1],[0.5,0.5])
    plt.xticks([]), plt.yticks([])

    plt.show()

ejercicio9_1()