from model import initialize_ledger, process_expense
from view import (
    display_welcome_menu, 
    prompt_for_expense, 
    display_success, 
    display_error, 
    display_final_audit
)

def main():
    total_spent = initialize_ledger()
    display_welcome_menu()
    
    while True:
        user_input = prompt_for_expense()
        new_total, status = process_expense(total_spent, user_input)
        
        if status is True:
            total_spent = new_total
            display_final_audit(total_spent)
            break
        elif status is None:
            display_error("invalid_data")
        elif status is False and new_total == total_spent:
            display_error("negative_value")
        else:
            total_spent = new_total
            display_success(total_spent)

if __name__ == "__main__":
    main()