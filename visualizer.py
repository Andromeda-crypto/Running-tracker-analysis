import matplotlib as plt

class Visualizer:
    def __init__(self):
        pass

def plot_bar_chart(data, labels,title):
    plt.bar(labels,data)
    plt.title(title)
    plt.xlabel('Categories')
    plt.ylabel('Total distance (km)')
    plt.show()

def plot_line_chart(x,y,title):
    plt.plot(x,y,maker= 'o')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Distyance(Km)')
    plt.xtics(rotation = 45)
    plt.show()


def plot_pie_chart(data, labels ,title):
    plt.pie(data,labels=labels,autopct = '%1.1f%',startangle = 90)
    plt.title(title)
    plt.show()

def plot_histogram(data,title,bins = 10):
    plt.hist(data,bins = bins)
    plt.title(title)
    plt.xlabel('Pace (min/km)')
    plt.ylabel('Frequency')
    plt.show()





