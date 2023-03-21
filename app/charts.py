import matplotlib.pyplot as plt 


def generate_bar_chart(name, labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values) #el .bar quiere decer que es grafica de barras y se le da los valores del eje x y del eje y
    plt.savefig(f'./images/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()


if __name__=='__main__':
    labels = ['a','b','c']
    values = [100, 30, 50]
   
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)