import datetime
from random import randint

# FertiliGlow App Initialization
class FertiliGlowApp:
    def __init__(self):
        self.user = None
        self.cycle_data = []
        self.fertility_window = None

    def start(self):
        print("Welcome to FertiliGlow!")
        self.user = self.get_user_info()
        self.initialize_cycle_data()
        self.calculate_fertility_window()
        self.display_dashboard()

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

    def update_glow(self):
        today = (datetime.datetime.now() - datetime.datetime.strptime(self.user.last_period, "%Y-%m-%d")).days
        if today in self.fertility_window:
            print("🌟 Glow: It's time! Your fertility is at its peak.")
        else:
            print("Glow: Fertility is low today.")


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
