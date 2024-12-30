class RunningGoal:

    def __init__(self,distance_goal = None, time_goal = None):
        self.distance_goal = distance_goal
        self.time_goal = time_goal
        self.progress = 0

    def check_distance_goal(self,total_distance):
        if self.distance_goal:
            return f"Distance goal : {self.distance_goal:.2f} km , Progress : {total_distance:.2f} km "
        return "No distance goal set."
    
    def check_time_goal(self,total_time):
        
        if self.time_goal:
            status = "Achieved" if best_pace <= self.pace_goal else "Not achieved"
            return f"Pace Goal: {self.pace_goal:.2f} min/km, Status: {status}"
        return "No pace goal set."
