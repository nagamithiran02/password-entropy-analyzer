# Password Strength & Breach-Pattern Analyzer

A robust command-line security utility built in Python designed to evaluate password entropy, detect weak structural patterns, check against common breach dictionaries, and generate cryptographically secure credentials.

---

## 🚀 Features

- **Mathematical Entropy Calculation**: Computes exact bits of entropy ($E = L \times \log_2(R)$) based on character pool diversity and length.
- **Heuristic Pattern Detection**: Flags common human-predictable habits such as keyboard walks (e.g., `qwerty`), sequential numbers (e.g., `12345`), and excessive repeating characters.
- **Dictionary & Breach Check**: Cross-references passwords against a customizable local list of common weak and breached passwords (`common_passwords.txt`).
- **Crack-Time Estimation**: Estimates offline brute-force attack durations across various threat models.
- **Secure Credential Generator**: Generates cryptographically secure random passwords and memorable passphrases using Python's native `secrets` module.

---

## 📂 Project Architecture

```text
password-entropy-analyzer/
├── README.md              # Project documentation and usage guide
├── main.py                # Command-line interface and user interaction loop
├── analyzer.py            # Core logic: entropy math, pattern checks & crack estimation
├── generator.py           # Secure password & passphrase generator utility
└── common_passwords.txt   # Dictionary blacklist of common weak passwords
