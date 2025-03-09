from utils import  load_transactions, save_transaction, get_budget_summary

def main():
    # Lade Transaktionen
    transactions = load_transactions("budget_data.txt")

    # Menü
    while True:
        print("\nTracke dein Budget!")
        print("1. Einnahme hinzufügen")
        print("2. Ausgabe hinzufügen")
        print("3. Budgetübersicht anzeigen")
        print("4. Beenden")

        choice = input("Wähle eine Option (1/2/3/4): ")

        if choice == '1':
            amount = float(input("Gib den Betrag der Einnahme ein: "))
            description = input("Beschreibung der Einnahme: ")
            save_transaction("budget_data.txt", "Einahme", amount, description)
            print(f"Einnahme von {amount} wurde hinzugefügt.")
        elif choice == '2':
            amount = float(input("Gib den Betrag der Ausgabe ein: "))
            description = input("Beschreibung der Ausgabe: ")
            save_transaction("budget_data.txt", "Einahme", amount, description)
            print(f"Ausgabe von {amount} wurde hinzugefügt.")
        elif choice == '3':
            get_budget_summary("budget_data.txt")
        elif choice == '4': 
            print("BudgetTracker beendet!")
            break 
        else:
            print("Ungültige Auswahl!")

if __name__ == "__main__":
    main()