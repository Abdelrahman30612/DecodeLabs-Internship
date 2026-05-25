def initialize_ledger():
    return 0.0

def process_expense(current_total, expense_input):
    cleaned_input = expense_input.strip().lower()
    
    if cleaned_input == "quit":
        return current_total, True
        
    try:
        expense_value = float(cleaned_input)
        if expense_value < 0:
            return current_total, False
        new_total = current_total + expense_value
        return new_total, False
    except ValueError:
        return current_total, None