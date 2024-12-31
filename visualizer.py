import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    def __init__(self, running_goal=None):
        self.running_goal = running_goal

    def plot_bar_chart(self, data, labels, title):
        """Plot a bar chart."""
        plt.bar(labels, data)
        plt.title(title)
        plt.xlabel("Categories")
        plt.ylabel("Values")
        plt.show()

    def plot_line_chart(self, x, y, title, xlabel="Date", ylabel="Values"):
        """Plot a line chart."""
        plt.plot(x, y, marker="o")
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_pie_chart(self, data, labels, title):
        """Plot a pie chart."""
        plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)
        plt.title(title)
        plt.show()

    def plot_histogram(self, data, title, bins=10):
        """Plot a histogram."""
        plt.hist(data, bins=bins, edgecolor="black")
        plt.title(title)
        plt.xlabel("Pace (min/km)")
        plt.ylabel("Frequency")
        plt.show()

    def plot_total_distance_by_date(self, runs):
        """Plot cumulative distance over time."""
        if not runs:
            print("No runs found.")
            return

        sorted_runs = sorted(runs, key=lambda x: x.date)
        dates = [run.date for run in sorted_runs]
        distances = [run.distance_km for run in sorted_runs]
        cumulative_distances = np.cumsum(distances)

        plt.figure(figsize=(10, 6))
        plt.plot(dates, cumulative_distances, marker="o", linestyle="--", color="b")
        plt.title("Total Distance Run Over Time")
        plt.xlabel("Date")
        plt.ylabel("Cumulative Distance (km)")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_avg_pace_by_category(self, avg_pace_by_category):
        """Plot average pace by category."""
        categories = list(avg_pace_by_category.keys())
        avg_pace = list(avg_pace_by_category.values())
        plt.bar(categories, avg_pace, color=["blue", "green", "red"])
        plt.title("Average Pace by Category")
        plt.xlabel("Category")
        plt.ylabel("Average Pace (min/km)")
        plt.show()

    def interactive_visualization(self, runs):
        """Display an interactive menu for visualizations."""
        print("\nInteractive Visualization")
        print("1. Line Graph")
        print("2. Bar Chart")
        print("3. Scatter Plot")
        chart_type = input("Enter the chart type (1/2/3): ")
        start_date = input("Enter start date (YYYY-MM-DD) or press Enter to skip: ")
        end_date = input("Enter end date (YYYY-MM-DD) or press Enter to skip: ")

        filtered_runs = self.filter_runs_by_date(runs, start_date, end_date)

        if chart_type == "1":
            self.plot_total_distance_by_date(filtered_runs)
        elif chart_type == "2":
            self.plot_avg_pace_by_category(filtered_runs)
        elif chart_type == "3":
            self.scatter_plot(filtered_runs)
        else:
            print("Invalid choice. Please try again.")

    def filter_runs_by_date(self, runs, start_date, end_date):
        """Filter runs based on date range."""
        if not start_date and not end_date:
            return runs

        filtered = [
            run for run in runs
            if (not start_date or run.date >= start_date) and (not end_date or run.date <= end_date)
        ]
        return filtered

    def plot_goal_progress(self, total_distance, total_time):
        """Visualize goal progress."""
        if self.running_goal and self.running_goal.distance_goal:
            plt.bar(["Goal"], [self.running_goal.distance_goal], color="green", label="Distance Goal")
            plt.bar(["Achieved"], [total_distance], color="blue", label="Distance Achieved")
            plt.legend()
            plt.title("Distance Goal Progress")
            plt.show()
        else:
            print("No distance goal set.")

    def plot_trends(self, runs):
        """Plot pace trends with a moving average."""
        if len(runs) < 2:
            print("Not enough data to analyze trends.")
            return

        dates = [run.date for run in runs]
        paces = [run.pace() for run in runs]

        window = 3
        moving_avg = np.convolve(paces, np.ones(window) / window, mode="valid")

        plt.plot(dates, paces, label="Pace")
        plt.plot(dates[window-1:], moving_avg, label="Moving Average", linestyle="--")
        plt.title("Pace Trend with Moving Average")
        plt.xlabel("Date")
        plt.ylabel("Pace (min/km)")
        plt.legend()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def scatter_plot(self, runs):
        """Plot a scatter plot of distance vs. pace."""
        distances = [run.distance_km for run in runs]
        paces = [run.pace() for run in runs]

        plt.scatter(distances, paces, color="purple")
        plt.title("Distance vs. Pace")
        plt.xlabel("Distance (km)")
        plt.ylabel("Pace (min/km)")
        plt.show()

    def plot_run_data(self,runs):
        if not runs:
            print("No runs to display.")
            return
        dates = [run.date for run in runs]
        distances = [run.distance_km for run in runs]
    
        self.plot_line_chart(dates, distances, "Run Distance Over Time")






    




    
        










    





    
    




