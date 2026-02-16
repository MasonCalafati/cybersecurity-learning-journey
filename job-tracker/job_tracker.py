import json
import os
from datetime import datetime

DATA_FILE = "applications.json"

def load_applications():
    """Load applications from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_applications(apps):
    """Save applications to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(apps, f, indent=2)

def add_application():
    """Add a new job application"""
    print("\n=== ADD NEW APPLICATION ===")
    company = input("Company name: ")
    position = input("Position: ")
    status = input("Status (applied/pending/interview/rejected/offer): ")
    
    app = {
        "id": len(load_applications()) + 1,
        "company": company,
        "position": position,
        "status": status,
        "date": datetime.now().strftime("%Y-%m-%d"),
    }
    
    apps = load_applications()
    apps.append(app)
    save_applications(apps)
    print(f"\n✓ Added application to {company}")

print("=" * 50)
print("    JOB APPLICATION TRACKER")
print("=" * 50)
def view_applications():
    """View all applications"""
    apps = load_applications()
    
    if not apps:
        print("\nNo applications tracked yet.")
        return
    
    print("\n" + "=" * 80)
    print(f"{'ID':<5} {'Company':<20} {'Position':<25} {'Status':<12} {'Date':<12}")
    print("=" * 80)
    
    for app in apps:
        print(f"{app['id']:<5} {app['company']:<20} {app['position']:<25} {app['status']:<12} {app['date']:<12}")
    
    print("=" * 80)

def show_stats():
    """Show application statistics"""
    apps = load_applications()
    
    if not apps:
        print("\nNo applications to analyze.")
        return
    
    total = len(apps)
    applied = sum(1 for a in apps if a['status'] == 'applied')
    pending = sum(1 for a in apps if a['status'] == 'pending')
    interview = sum(1 for a in apps if a['status'] == 'interview')
    rejected = sum(1 for a in apps if a['status'] == 'rejected')
    offers = sum(1 for a in apps if a['status'] == 'offer')
    
    print("\n" + "=" * 40)
    print("         APPLICATION STATS")
    print("=" * 40)
    print(f"Total Applications: {total}")
    print(f"Applied:           {applied}")
    print(f"Pending:           {pending}")
    print(f"Interviews:        {interview}")
    print(f"Rejected:          {rejected}")
    print(f"Offers:            {offers}")
    print("=" * 40)

def main():
    """Main menu"""
    while True:
        print("\n1. Add application")
        print("2. View all applications")
        print("3. Show stats")
        print("4. Exit")
        
        choice = input("\nChoose option (1-4): ")
        
        if choice == '1':
            add_application()
        elif choice == '2':
            view_applications()
        elif choice == '3':
            show_stats()
        elif choice == '4':
            print("\nGood luck with your job search! 💪")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
