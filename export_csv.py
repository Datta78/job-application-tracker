# Export Applications to CSV - Dattatray Bhosale

import json
import csv
from datetime import datetime

def export_to_csv():
    try:
        with open("applications.json", "r") as f:
            applications = json.load(f)
        
        with open("applications.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Company", "Position", "Status", "Notes"])
            
            for app in applications:
                writer.writerow([
                    app["date"],
                    app["company"],
                    app["position"],
                    app["status"],
                    app.get("notes", "")
                ])
        
        print("✅ Applications exported to applications.csv successfully!")
    except FileNotFoundError:
        print("No applications found to export.")

if __name__ == "__main__":
    export_to_csv()
