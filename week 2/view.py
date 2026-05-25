def display_welcome_menu():
    print("\n" + "="*30)
    print("    DECODELABS EXPENSE ENGINE   ")
    print("="*30)
    print("Enter your expense amounts continuously.")
    print("Type 'quit' to halt and print final audit.")
    print("="*30)

def prompt_for_expense():
    return input("\nEnter expense amount (or 'quit'): ")

def display_success(updated_total):
    print(f"✔ Transaction processed. Current Total: ${updated_total:.2f}")

def display_error(error_type):
    if error_type == "invalid_data":
        print("❌ Invalid Data: Input must be a valid numerical value.")
    elif error_type == "negative_value":
        print("❌ Invalid Data: Expense cannot be a negative value.")

def display_final_audit(final_total):
    print("\n" + "="*30)
    print("          FINAL AUDIT           ")
    print("="*30)
    print(f"TOTAL SPENT: ${final_total:.2f}")
    print("Execution halted via sentinel switch.")
    print("="*30)