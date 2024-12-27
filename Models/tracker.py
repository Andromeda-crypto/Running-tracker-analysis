
import csv
from Models.run import Run
from visualizer import Visualizer 

class RunningTracker:

    def __init__(self):
        self.runs = []

    def add_run(self, run):
        """Add a run to the tracker."""
        self.runs.append(run)

    def total_distance(self):
        """Calculate total distance run."""
        return sum(run.distance_km for run in self.runs)

    def average_pace(self): 
        """Calculate the average pace for all runs."""
        total_pace = sum(run.pace() for run in self.runs)
        return total_pace / len(self.runs) if self.runs else 0
    
    def find_fastest_pace(self):
        if not self.runs:
            return "No runs found."
        
        paces = []
        for run in self.runs:
            pace = run.time_minutes / run.distance_km
            paces.append((pace, run))  # Store tuple (pace, run object)
        
        fastest_pace, fastest_run = min(paces, key=lambda x: x[0])  # Use the pace for comparison
        return fastest_pace, fastest_run
    
    def longest_run(self):
        if not self.runs:
            return 'No runs found.'
        
        maximum_distance = float('-inf')
        longest_run = None
        for run in self.runs:
            if run.distance_km > maximum_distance:
                maximum_distance = run.distance_km
                longest_run = run

        return maximum_distance, longest_run

    def analyze_runs(self):
        """Analyze all runs."""
        if not self.runs:
            print('No runs available to analyze.')
            return
        total_distance = self.total_distance()
        fastest_pace = self.find_fastest_pace()
        longest_run = self.longest_run()
        avg_pacee = self.average_pace()

        if longest_run:
            longest_run_info = f'{longest_run.distance_km} km (on {longest_run.date})'
        else:
            longest_run_info= " No runs found."

        print(f"Total distance = {total_distance:.2f} km")
        print(f"Average pace = {avg_pacee:.2f} min/km")
        print(f"Fastest pace = {fastest_pace[0]:.2f} min/km (on {fastest_pace[1].date})")
        print(f"Longest run = {longest_run_info}")
        print('Average pace by category:')
        for category, avg_pace in self.average_pace_by_category().items():
            print(f"{category}: {avg_pace:.2f} min/km")

        
    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Distance (Km)', 'Time (minutes)', 'Temperature (Celsius)'])  # Fixed this line
            for run in self.runs:
                writer.writerow([run.date, run.distance_km, run.time_minutes, run.temperature_celsius])

    def load_from_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.add_run(Run(row['Date'], float(row['Distance (km)']), float(row['Time (minutes)']), float(row['Temperature (°C)'])))
        except FileNotFoundError:
            print("No existing data found.")

    def total_calories_burned(self):
        """Calculate the total calories burned."""
        return f"The total calories burned are {sum(run.calories_burned() for run in self.runs)}. " 
    
    def group_runs_by_temperature(self):
        groups = {'Cold' :[],
                  'Moderate' : [],
                  'Hot ': []}
        for run in self.runs:
            if self.conditions() == 'Cold':
                groups['Cold'].append(run)
            elif self.conditions() == 'Moderate':
                groups['Moderate'].append(run)
            else:
                groups['Hot'].append(run)

        return groups
    
    def average_pace_by_category(self):
        avg_paces = {'Cold : 0','Moderate: 0 ','Hot : 0'}
        grouped_runs = self.group_runs_by_temperature()
        
        for category, runs in grouped_runs.items():
            if runs:
                total_pace = sum(run.pace()for run in runs)
                avg_paces[category] = total_pace / len(runs)
            else:
                avg_paces[category] = 'No runs in this category'

        return avg_paces
    
    def visualize_run_data(self):
        visualizer = Visualizer(self.runs)
        visualizer.plot_run_data()



        
