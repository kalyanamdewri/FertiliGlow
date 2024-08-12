import datetime
from random import randint

# FertiliGlow App Initialization
class FertiliGlowApp:
    def __init__(self):
        self.user = None
        self.cycle_data = []
        self.fertility_window = None
        self.device = None  # Placeholder for the bedside device integration
        self.points = 0

    def start(self):
        print("Welcome to FertiliGlow!")
        self.user = self.get_user_info()
        self.device = BedsideDevice()
        self.initialize_cycle_data()
        self.calculate_fertility_window()
        self.display_dashboard()
        self.gamification_intro()

    def get_user_info(self):
        print("Please enter your details to get started.")
        name = input("Enter your name: ")
        cycle_length = int(input("Enter your average cycle length (days): "))
        last_period = input("Enter the start date of your last period (YYYY-MM-DD): ")
        return User(name, cycle_length, last_period)

    def initialize_cycle_data(self):
        print("Initializing cycle data...")
        # Placeholder for real data initialization
        self.cycle_data = [randint(0, 1) for _ in range(30)]  # Dummy data

    def calculate_fertility_window(self):
        print("Calculating fertility window...")
        # A simple placeholder calculation for the fertility window
        ovulation_day = self.user.cycle_length // 2
        self.fertility_window = range(ovulation_day - 3, ovulation_day + 2)

    def display_dashboard(self):
        print(f"Hello {self.user.name}, here is your fertility tracking dashboard.")
        print("Your estimated fertility window is from day "
              f"{self.fertility_window.start} to {self.fertility_window.stop - 1} of your cycle.")
        self.update_glow()

    def update_glow(self):
        today = (datetime.datetime.now() - datetime.datetime.strptime(self.user.last_period, "%Y-%m-%d")).days
        if today in self.fertility_window:
            print("🌟 Glow: It's time! Your fertility is at its peak.")
            self.device.set_glow('green')  # Indicate peak fertility
        else:
            print("Glow: Fertility is low today.")
            self.device.set_glow('blue')  # Indicate low fertility

    def log_daily_data(self):
        print("Logging daily data...")
        mood = input("Enter your mood today: ")
        temperature = float(input("Enter your temperature today (°C): "))
        notes = input("Any additional notes for today? ")
        self.user.log_daily_data(mood, temperature, notes)
        self.gamification_rewards()

    def gamification_rewards(self):
        print("🎮 Gamification: You've earned points for logging today's data!")
        self.points += 10  # Assign points for daily logging
        print(f"Total Points: {self.points}")
        self.check_achievements()

    def check_achievements(self):
        if self.points >= 50:
            print("🎉 Congratulations! You've earned the 'Consistent Tracker' badge!")
        # Add more achievement levels as needed

    def gamification_intro(self):
        print("Welcome to the FertiliGlow Gamification Center!")
        print("Track your progress, earn points, and unlock badges as you go.")
        print("Remember, consistency is key to unlocking new levels and rewards!")

# Bedside Device Class (Placeholder for actual hardware integration)
class BedsideDevice:
    def __init__(self):
        self.color = 'off'

    def set_glow(self, color):
        self.color = color
        print(f"Bedside device is now glowing {self.color}.")

    def sync_with_app(self):
        print("Syncing with the FertiliGlow app...")
        # Placeholder for sync logic
        print("Device synced successfully!")

# User Class
class User:
    def __init__(self, name, cycle_length, last_period):
        self.name = name
        self.cycle_length = cycle_length
        self.last_period = last_period
        self.progress = {}

    def log_daily_data(self, mood, temperature, notes=""):
        day = (datetime.datetime.now() - datetime.datetime.strptime(self.last_period, "%Y-%m-%d")).days
        self.progress[day] = {
            "mood": mood,
            "temperature": temperature,
            "notes": notes
        }
        print(f"Day {day} logged successfully.")

    def display_progress(self):
        print("Here is your progress so far:")
        for day, data in self.progress.items():
            print(f"Day {day}: Mood: {data['mood']}, Temp: {data['temperature']}°C, Notes: {data['notes']}")

# Starting the FertiliGlow app
if __name__ == "__main__":
    app = FertiliGlowApp()
    app.start()

    # Simulate daily usage
    while True:
        app.log_daily_data()
        user_choice = input("Do you want to log data for another day? (yes/no): ")
        if user_choice.lower() != 'yes':
            break
