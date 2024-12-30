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

def plot_total_distance_by_date(runs):
    if not runs:
        print('No runs found.')
        return
    sorted_runs = sorted(runs, key = lambda x: x.date)
    dates = [run.date for run in sorted_runs]
    distances = [ run.distance_km for run in sorted_runs]
    cumulative_distances = [sum(distances[:i+1]) for i in range (len(distances))]

    # plotting the graph

    plt.figure(figsize=(10,6))
    plt.plot(dates, cumulative_distances, marker = 'o', linestyle = '--', color = 'b')
    plt.title('Total Distance run over time')
    plt.xlabel('Date')
    plt.ylabel('Cumulative distance (km)')
    plt.grid(True)
    plt.xtics(rotation = 45)
    plt.tight_layout()
    plt.show()

def plot_avg_pace_by_category(avg_pace_by_category):
    categories = list(avg_pace_by_category.keys())
    avg_pace = list(avg_pace_by_category.values())
    plt.bar(categories, avg_pace, color = ['blue', 'green', 'red'])
    plt.title('Average pace by category')
    plt.xlabel('category')
    plt.ylabel('Average pace(min/km)')
    plt.show()

def plot_line_chart(x,y,title):
    plt.plot(x,y,marker='o')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Distance (Km)')
    plt.xtics(rotation = 45)
    plt.show()







    





    
    




