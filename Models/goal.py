class RunningGoal:

    def __init__(self, distance_goal=None, time_goal=None):
        self.distance_goal = distance_goal
        self.time_goal = time_goal
        self.progress = 0

    def check_distance_goal(self, total_distance):
        """Check and return the status of the distance goal."""
        if self.distance_goal:
            if total_distance >= self.distance_goal:
                return f"Distance goal of {self.distance_goal:.2f} km achieved! Progress: {total_distance:.2f} km"
            return f"Distance goal: {self.distance_goal:.2f} km, Progress: {total_distance:.2f} km"
        return "No distance goal set."

    def check_time_goal(self, best_pace):
        """Check and return the status of the time goal (pace)."""
        if self.time_goal:
            status = "Achieved" if best_pace <= self.time_goal else "Not achieved"
            return f"Time goal (Pace): {self.time_goal:.2f} min/km, Status: {status}"
        return "No time goal set."
