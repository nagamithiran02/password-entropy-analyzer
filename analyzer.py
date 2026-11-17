import math
import string
import os

def calculate_pool_size(password):
    """Determine the character pool size (R) based on character types present."""
    has_lower = any(c in string.ascii_lowercase for c in password)
    has_upper = any(c in string.ascii_uppercase for c in password)
    has_digits = any(c in string.digits for c in password)
    has_symbols = any(c in string.punctuation for c in password)
    
    pool_size = 0
    if has_lower:
        pool_size += 26
    if has_upper:
        pool_size += 26
    if has_digits:
        pool_size += 10
    if has_symbols:
        pool_size += len(string.punctuation)
        
    return pool_size

def calculate_entropy(password):
    """Calculate bits of entropy for a given password string."""
    if not password:
        return 0.0
    
    length = len(password)
    pool_size = calculate_pool_size(password)
    
    if pool_size == 0:
        return 0.0
    
    # E = L * log2(R)
    entropy = length * math.log2(pool_size)
    return round(entropy, 2)

def check_patterns(password):
    """Detect common weak structural patterns in the password."""
    issues = []
    
    # Check for excessive repeating characters (e.g., 'aaaa', '1111')
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            issues.append("Contains repeating character sequences (e.g., 'aaa')")
            break
            
    # Check for common keyboard walks or predictable strings
    common_walks = ["12345", "123456", "qwerty", "asdfgh", "zxcvbn", "password", "admin", "abcde"]
    lower_pwd = password.lower()
    for walk in common_walks:
        if walk in lower_pwd:
            issues.append(f"Contains predictable pattern/walk ('{walk}')")
            break
            
    return issues

def check_dictionary(password, filepath="common_passwords.txt"):
    """Check if password matches any entry in the local common passwords file."""
    if not os.path.exists(filepath):
        return False
        
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            # Build a set of stripped, lowercase common passwords for fast lookup
            common_words = {line.strip().lower() for line in f if line.strip()}
            if password.lower() in common_words:
                return True
    except Exception:
        pass
        
    return False