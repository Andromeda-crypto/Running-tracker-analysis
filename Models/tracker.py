
import csv
from Models.run import Run

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
        for run in self.runs:
            print(run.run_info())  # Make sure this method exists in the Run class

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
