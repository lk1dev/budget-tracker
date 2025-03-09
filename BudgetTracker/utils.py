def load_transactions(file_path):
    transactions = []
    try: 
        with open(file_path, 'r') as file:
            for line in file:
                date, type_, amount, description = line.strip()split(',')
                transactions.append({
                    'date': date,
                    'type': type_,
                    'amount': float(amount),
                    'description': description
                })
    expept FileNotFoundError:
        pass # Falls die Datei nicht existiert, starten wir mit einer leeren Liste
        return transactions

def save_transaction(file_path, type_, amount, description):
    from datetime import datetime
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, 'a') as file:
        file.write(f"{date},{type_},{amount},{description}\n")

def get_budget_summary(file_path):
    transactions = load_transactions(file_path)
    total_income = sum(t['amount'] for t in transactions if t['type'] == 'Einnahme')
    total_expense = sum(t['amount'] for t in transactions if t['type'] == 'Ausgabe')
    balance = total_income - total_expense

    print(f"Gesamte Einnahmen: {total_income}")
    print(f"Gesamte Ausgaben: {total_expense}")
    print(f"Verfügbares Budget: {balance}")

    
        