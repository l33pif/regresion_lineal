import numpy as np
import matplotlib.pyplot as plt

def main():
    #dataset
    x = np.array([1,2,3,4,5])
    y = np.array([2,3,5,6,5])

    #Obtenemos b1 y b2
    b = estimated_b0_b1(x, y)
    print(f'Los valores de a = {b[0]}, b = {b[1]}')
    
    #graficamos linea de regresion
    plot_regression(x, y, b)

def estimated_b0_b1(x, y):
    #n = np.size(x)
    
    #obtener promedios de x y y
    me_x, me_y = np.mean(x), np.mean(y)

    #calcular sumatoria de xy y sumatoria se xx
    sumatoria_xy = np.sum((x-me_x)*(y-me_y))
    sumatoria_xx = np.sum((x-me_x)**2)

    #coeficientes de regresion
    b = sumatoria_xy / sumatoria_xx
    a = me_y - b * me_x

    return (a, b)

def plot_regression(x, y, b):
    plt.scatter(x, y, color = 'green', marker = 'o', s=30)

    y_prediction = b[0] + b[1]*x
    plt.plot(x, y_prediction, color = 'blue')

    #etiquetado
    plt.xlabel('x-Independiente')
    plt.ylabel('y-Dependiente')

    plt.show()


if __name__ == '__main__':
    main()
    