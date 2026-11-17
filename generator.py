import secrets
import string

def generate_secure_password(length=16):
    """Generate a cryptographically secure random password containing a mix of character types."""
    if length < 8:
        length = 8  # Enforcea safe minimum length

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure at least one character from each category
    password_chars = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill the rest of the length with a combined pool
    all_pool = lowercase + uppercase + digits + symbols
    for _ in range(length - 4):
        password_chars.append(secrets.choice(all_pool))

    # Shuffle the characters securely so predictable patterns don't form
    secrets.SystemRandom().shuffle(password_chars)

    return "".join(password_chars)

def generate_passphrase(num_words=4):
    """Generate an entropic passphrase using a small wordlist."""
    wordlist = [
        "apple", "brave", "delta", "eagle", "frost", "ghost", "helix",
        "iron", "jungle", "karma", "lunar", "matrix", "nova", "orbit", "prism",
        "quantum", "radar", "signal", "titan", "umbra", "vortex", "warp", "xenon"
    ]

    chosen_words = [secrets.choice(wordlist) for _ in range(num_words)]
    # Join with a secure random seperator symbol or dash
    seperator = secrets.choice(["-", "_", ".", "@"])
    return seperator.join(chosen_words)