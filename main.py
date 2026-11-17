import os
from analyzer import calculate_entropy, check_patterns, check_dictionary
from generator import generate_secure_password, generate_passphrase

def print_banner():
    print("=" * 60)
    print("      PASSWORD STRENGTH & BREACH-PATTERN ANALYZER")
    print("=" * 60)

def evaluate_flow():
    print("\n--- Password Strength Evaluation ---")
    password = input("Enter a password to analyze: ")
    
    if not password:
        print("[!] Password cannot be empty.")
        return

    # Run analysis functions from analyzer.py
    entropy = calculate_entropy(password)
    patterns = check_patterns(password)
    is_breached = check_dictionary(password)

    print("\n[+] Analysis Results:")
    print(f"    - Length: {len(password)} characters")
    print(f"    - Entropy: {entropy} bits")
    
    # Strength rating based on entropy bits
    if entropy < 28:
        rating = "VERY WEAK (Vulnerable to instant brute-force)"
    elif entropy < 36:
        rating = "WEAK (Easily cracked by modern hardware)"
    elif entropy < 60:
        rating = "STRONG (Good for standard use)"
    else:
        rating = "VERY STRONG (Highly resilient against attacks)"
    print(f"    - Strength Rating: {rating}")

    # Display pattern warnings if any found
    if patterns:
        print("    - Structural Warnings:")
        for pattern in patterns:
            print(f"      * {pattern}")
    else:
        print("    - Structural Warnings: None detected.")

    # Display local dictionary blacklist check
    if is_breached:
        print("    - [!] ALERT: This password matches a known entry in common_passwords.txt!")
    else:
        print("    - [✓] Not found in the local common passwords blacklist.")

def generate_flow():
    print("\n--- Secure Credential Generator ---")
    print("1. Random Complex Password")
    print("2. Memorable Passphrase")
    choice = input("Select generation type (1 or 2): ").strip()

    if choice == "1":
        try:
            length_input = input("Enter desired length (default 16, min 8): ").strip()
            length = int(length_input) if length_input else 16
        except ValueError:
            length = 16
        pwd = generate_secure_password(length)
        print(f"\n[+] Generated Password: {pwd}")
    elif choice == "2":
        try:
            words_input = input("Enter number of words (default 4): ").strip()
            words = int(words_input) if words_input else 4
        except ValueError:
            words = 4
        phrase = generate_passphrase(words)
        print(f"\n[+] Generated Passphrase: {phrase}")
    else:
        print("[!] Invalid selection.")

def main():
    while True:
        print_banner()
        print("1. Evaluate a Password")
        print("2. Generate a Secure Password / Passphrase")
        print("3. Exit")
        
        choice = input("\nSelect an option (1-3): ").strip()
        
        if choice == "1":
            evaluate_flow()
        elif choice == "2":
            generate_flow()
        elif choice == "3":
            print("\nExiting tool. Stay secure!")
            break
        else:
            print("\n[!] Invalid option. Please select 1, 2, or 3.")
        
        input("\nPress Enter to continue...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()