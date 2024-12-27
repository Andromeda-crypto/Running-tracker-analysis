class Run:
    def __init__(self, date, distance_km, time_minutes, temperature_celsius, weight_kg):
        self.date = date
        self.distance_km = distance_km
        self.time_minutes = time_minutes
        self.temperature_celsius = temperature_celsius
        self.weight_kg = weight_kg
    
    def pace(self):
        """Calculate the pace per km."""
        return self.time_minutes / self.distance_km
    
    def conditions(self):
        """Analyze weather conditions."""
        if self.temperature_celsius <= 0:
            return "Cold"
        elif self.temperature_celsius >= 25:
            return "Hot"
        else:
            return "Moderate"
        
    def run_info(self):
        """Return formatted information about the run."""
        pace = self.pace()
        conditions = self.conditions()
        return f"Date: {self.date}, Distance: {self.distance_km} km, Time: {self.time_minutes} minutes, Pace: {pace:.2f} min/km, Conditions: {conditions}, Calories burned: {self.calories_burned()}"

    def calories_burned(self):
        """Calculate the calories burned during the run."""
        return 1.036 * self.weight_kg * self.distance_km
