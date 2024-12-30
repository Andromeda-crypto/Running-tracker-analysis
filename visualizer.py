import matplotlib as plt
import numpy as np

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

def plot_line_chart(self,runs):
    dates = [run.date for run in runs]
    paces = [run.pace()for run in runs]

    fig ,ax = plt.subplots()
    line, = ax.plot(dates,paces,label='Pace')
    ax.set_title('Pace over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Pace (min/km)')
    plt.legend()

    def on_hover(event):
        for i, point in  enumerate(line.get_data()[0]):
            if event.xdata and abs(event.xdata - i) < 0.5:
                print(f"Run on {dates[i]}: Pace = {paces[i]:.2f} min/km ")

        fig.canvas.mpl_connect('motion_notifu_event',on_hover)
        plt.show()





def scatter_plot(x,y,title):
    plt.scatter(x,y)
    plt.title(title)
    plt.xlabel('Distance (Km)')
    plt.ylabel('Pace (min/km)')
    plt.show()


def interactive_visualization(self,runs):
    print('\n Interactive Visualization')
    print('1. Line Graph')
    print('2. Bar Chart')
    print('3. Scatter Plot')
    chart_type = int(input('Enter the chart type : '))
    start_date = input('Enter start date (YYYY-MM-DD) or press Enter to skip : ')
    end_date = input('Enter end date (YYYY-MM-DD) or press Enter to skip : ')

    filtered_runs = self.filter_runs_by_date(runs,start_date,end_date)

    if chart_type == '1':
        self.plot_line_chart(filtered_runs)
    elif chart_type == '2':
        self.plot_bar_chart(filtered_runs)
    elif chart_type == '3':
        self.plot_scatter_plot(filtered_runs)
    else:
        print('Invalid choice. Please try again.')

def filter_runs_by_date(self,runs,start_date,end_date):
    if not start_date and not end_date:
        return runs
    
    filtered = []
    for run in runs:
        if (not start_date or run.date >= start_date) and (not end_date or run.date <= end_date):
            filtered.append(run)
        return filtered
    
def analyze_runs(self,runs):
    dates = [run.date for run in self.runs]
    distances = [run.distance_km() for run in self.runs]
    paces = [run.pace() for run in self.runs]

    print("\n Trend Analysis")
    if len(runs) < 2:
        print('Not enough data to analyze trends.')
        return
    avg_pace = sum(paces)/len(paces)
    avg_distance = sum(distances)/len(distances)
    print(f"Average Pace : {avg_pace:.2f} min/km")
    print(f"Average Distance : {avg_distance:.2f} km")


# Calculating moving average for smoother visualization

def plot_trends(self,runs):
    dates = [run.date for run in runs]
    paces = [run.pace() for run in runs]

    numerical_dates = np.arange(len(dates))

    window = 3
    moving_avg = np.convolve(paces,np.ones(window)/window,mode='valid')

    fig ,ax = plt.subplots()
    ax.plot(dates,paces,label='Pace')
    ax.plot(dates[window-1:],moving_avg,label='Moving Average')
    ax.set_title("Pace trend with moving average")
    ax.set_xlabel('Date')
    ax.set_ylabbel("Pace (min/km)")
    plt.legend()
    plt.show()

# Comparision between different weather conditions

def compare_conditions(self,runs):
    conditions = {"Cold":[],
                  "Moderate" : [],
                  "Hot" : []
                  }
    for run in runs:
        conditions[run.conditions()].append(run.pace())

    avg_paces = {cond : sum(paces)/len(paces) if paces else 0 for cond, paces in conditions.items()}
    print("Average pace by conditons : ")
    for cond, avg in avg_paces.items():
        print(f"{cond} : {avg:.2f} min/km")


def plot_trend_with_annotation(self,runs):
    dates = [run.date for run in runs]
    paces = [run.pace() for run in runs]

    fig,ax = plt.subplots()
    ax.plot(dates,paces,label="Pace")
    ax.set_title("Pace trend")
    ax.set_xlabel('Date')
    ax.set_ylabel('Pace (min/km)')

    # highlighting the fastest run

    fastest_idx = paces.index(min(paces))
    ax.annotate("Fastest", (dates[fastest_idx],),
                textcoords = "offset points", xytext = (10,-10),
                arrowprops = dict(arrowstyle = '->'))
    
    plt.legend()
    plt.show()


# Adding performance insights 

def summary_of_performance(self,runs):
    total_dist = sum(run.distance_km for run in runs)
    total_time = sum(run.time_minutes for run in runs)
    total_cals = sum(run.calories_burned() for run in runs)

    best_pace = min(run.pace() for run in runs)
    longest_run = max(run.pace() for run in runs)

    print("\n Performance Summary")
    print(f"Total Distance : {total_dist:.2f} km")
    print(f"Total Time : {total_time:.2f} minutes")
    print(f"Calories Burned  : {total_cals:.2f} calories")
    print(f"Fastest Pace : {best_pace:.2f} min/km")
    print(f"Longest Run : {longest_run:.2f} km")


def analyze_patterns(self,runs):
    pace_by_condition = {"Cold": [], "Moderate": [], "Hot": []}
    for run in runs:
        pace_by_condition[run.conditions()].append(run.pace())

    print("\nPerformance Insights:")
    for condition, paces in pace_by_condition.items():
        if paces:
            avg_pace = sum(paces) / len(paces)
            print(f"Average Pace in {condition} Conditions: {avg_pace:.2f} min/km")


def plot_performance_highlights(self,runs):
    dates = [run.date for run in runs]
    distances  = [run.distance_km for run in runs]
    fig, ax = plt.subplots()
    ax.plot(dates, distances, label="Distance")

    # Highlight the longest run
    max_distance = max(distances)
    max_index = distances.index(max_distance)
    ax.annotate(f"Longest Run: {max_distance} km", (dates[max_index], max_distance),
                textcoords="offset points", xytext=(10, 10),
                arrowprops=dict(arrowstyle="->"))

    ax.set_title("Performance Highlights")
    ax.set_xlabel("Date")
    ax.set_ylabel("Distance (km)")
    plt.legend()
    plt.show()



    




    
        










    





    
    




