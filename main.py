# Job Application Tracker - Dattatray Bhosale
# Strong Project for Recruiters

import json
from datetime import datetime

DATA_FILE = "applications.json"

def load_applications():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_applications(applications):
    with open(DATA_FILE, "w") as f:
        json.dump(applications, f, indent=2)

def add_application():
    company = input("Company Name: ")
    position = input("Position: ")
    status = input("Status (Applied/Interview/Rejected/Offer): ")
    
    application = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "company": company,
        "position": position,
        "status": status,
        "notes": input("Notes: ")
    }
    
    applications = load_applications()
    applications.append(application)
    save_applications(applications)
    print("✅ Application added!")

def view_applications():
    applications = load_applications()
    if not applications:
        print("No applications yet.")
        return
    for app in applications:
        print(f"\n{app['date']} | {app['company']} | {app['position']} | {app['status']}")
        if app['notes']:
            print("Notes:", app['notes'])

def statistics():
    applications = load_applications()
    total = len(applications)
    print(f"\nTotal Applications: {total}")
    # Can add more stats later

def main():
    while True:
        print("\n=== Job Application Tracker ===")
        print("1. Add Application")
        print("2. View Applications")
        print("3. Statistics")
        print("4. Exit")
        choice = input("Choose: ")
        
        if choice == "1":
            add_application()
        elif choice == "2":
            view_applications()
        elif choice == "3":
            statistics()
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
