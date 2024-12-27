from Models.run import Run
from Models.tracker import RunningTracker

    
<<<<<<< HEAD
run1 = Run("2024-06-02", 11.56, 66, -5, 70)  

if __name__ == "__main__":
    tracker = RunningTracker()
    tracker.add_run(run1)
    tracker.visualize_run_data()
=======
run1 = Run("2024-06-02", 11.56, 66, -5)
if __name__ == "__main__":
    tracker = RunningTracker()
    tracker.add_run(run1)
>>>>>>> origin/main
     
    '''Loading the runs ''' 
    tracker.load_from_csv("runs.csv")

    while True:
        print("\nMAIN MENU")
        print("1. Add a run")
        print("2. View all runs")
        print("3. Save and exit")
        choice = input('Enter your choice : ')

        if choice == 1:
            date = input("Enter the Date (YYYY_MM-DD) : ")
            distance = input('Enter the distance (in KM) : ')
            time = input('Enter the total time of the run (in minutes) :')
            temperature = input('Enter the weather conditons( in degree celsius) : ')

            tracker.add_run(Run(date,distance,time,temperature))


        elif choice == 2:
            tracker.analyze_runs()

        elif choice == 3:
            tracker.save_to_csv("runs.csv")
            print('Data Saved.\nGoodbye!')
            break
        else:
            print('Invalid choice. Please try again.')


<<<<<<< HEAD

=======
>>>>>>> origin/main
    












    
    
