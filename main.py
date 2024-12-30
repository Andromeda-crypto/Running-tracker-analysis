from Models.run import Run
from Models.tracker import RunningTracker
from visualizer import Visualizer

if __name__ == "__main__":
    tracker = RunningTracker()
    
    # Example run to test
    run1 = Run("2024-06-02", 11.56, 66, -5, 67)
    tracker.add_run(run1)
    
    # Visualize and analyze the runs
    tracker.visualize_run_data()
    tracker.analyze_runs()
    tracker.visualize_total_distance_by_date()

    # Load runs from CSV
    tracker.load_from_csv("runs.csv")

    # Main menu loop
    while True:
        print("\nMAIN MENU")
        print("1. Add a run")
        print("2. View all runs")
        print("3. Save and exit")
        choice = input('Enter your choice: ')

        if choice == "1":
            date = input("Enter the Date (YYYY-MM-DD): ")
            distance = float(input('Enter the distance (in KM): '))
            time = float(input('Enter the total time of the run (in minutes): '))
            temperature = float(input('Enter the weather conditions (in degrees Celsius): '))
            weight = float(input('Enter your weight (in kg): '))

            tracker.add_run(Run(date, distance, time, temperature, weight))

        elif choice == "2":
            tracker.analyze_runs()

        elif choice == "3":
            tracker.save_to_csv("runs.csv")
            print('Data Saved.\nGoodbye!')

            break
        elif choice == "4":
            tracker.visualizer.interactive_visualization(tracker.runs)

        elif choice == '5':
            tracker.visualizer.analyze_trends(tracker.runs)
            tracker.visualizer.plot_trends(tracker.runs)
            tracker.visualizer.compare_weather_conditions(tracker.runs)

        elif choice == '6':
            tracker.visualizer.summary_of_performance(tracker.runs)

        elif choice == '7':
            tracker.visualizer.analyze_patterns(tracker.runs)
        elif choice == "8":
            distance_goal = float(input("Set a distance goal (in km): "))
            pace_goal = float(input("Set a pace goal (in min/km): "))
            tracker.goal = RunningGoal(distance_goal, pace_goal)
            print("Goals set successfully!")
        else:
            print('Invalid choice. Please try again.')




    












    
    
