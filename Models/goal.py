class RunningGoal:
    def __init__(self, distance_goal=None, time_goal=None, pace_goal=None):
        self.distance_goal = distance_goal
        self.time_goal = time_goal
        self.pace_goal = pace_goal

    def check_distance_goal(self, total_distance):
        """Check and return the status of the distance goal."""
        if self.distance_goal:
            if total_distance >= self.distance_goal:
                return f"Distance goal of {self.distance_goal:.2f} km achieved! Progress: {total_distance:.2f} km"
            return f"Distance goal: {self.distance_goal:.2f} km, Progress: {total_distance:.2f} km"
        return "No distance goal set."

    def check_time_goal(self, total_time):
        """Check and return the status of the time goal."""
        if self.time_goal:
            if total_time >= self.time_goal:
                return f"Time goal of {self.time_goal:.2f} minutes achieved! Progress: {total_time:.2f} minutes"
            return f"Time goal: {self.time_goal:.2f} minutes, Progress: {total_time:.2f} minutes"
        return "No time goal set."

    def check_pace_goal(self, best_pace):
        """Check and return the status of the pace goal."""
        if self.pace_goal:
            status = "Achieved" if best_pace <= self.pace_goal else "Not achieved"
            return f"Pace goal: {self.pace_goal:.2f} min/km, Status: {status}"
        return "No pace goal set."

    def check_all_goals(self, total_distance, total_time, best_pace):
        """Check all goals and return a summary."""
        distance_status = self.check_distance_goal(total_distance)
        time_status = self.check_time_goal(total_time)
        pace_status = self.check_pace_goal(best_pace)

        return f"{distance_status}\n{time_status}\n{pace_status}"

            
