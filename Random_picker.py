import random

def load_activities(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def generate_activity(activities):
    return random.choice(activities).strip()  

if __name__ == "__main__":
    activities = load_activities("activities.txt")
    print("Random Thing to Do:")
    print(generate_activity(activities))
