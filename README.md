```markdown
# Password Strength & Breach-Pattern Analyzer

A robust, modular Python security tool designed to evaluate password strength using cryptographic entropy calculations, structural heuristic warnings, and local blacklist breach detection.

## 🚀 Features

- **Shannon Entropy Calculation ($E = L \times \log_2(R)$):** Objectively measures password unpredictability and bits of security based on character set variety.
- **Structural Pattern Heuristics:** Automatically scans for vulnerable human habits, such as excessive character repetition (`aaa`) and keyboard walks (`qwerty`, `12345`).
- **Local Breach-Pattern Blacklist:** Fast $O(1)$ set lookup against a curated list of common or leaked credentials (`common_passwords.txt`).
- **Secure Credential Generator:** Generates cryptographically secure random passwords and memorable passphrases using Python's `secrets` module.
- **Modular Architecture:** Clean separation of concerns across logic, generation, and CLI interface components.

---

## 🛠️ Project Structure

```text
password-entropy-analyzer/
│
├── main.py              # CLI interface and user interaction loops
├── analyzer.py          # Entropy formulas, pattern checks, and dictionary lookups
├── generator.py         # Secure random password and passphrase generators
└── common_passwords.txt # Local blacklist of common/weak passwords

```

---

## 📦 Requirements & Installation

* **Python 3.x** installed on your system.
* No external third-party pip packages required (uses Python standard libraries: `math`, `string`, `os`, `secrets`).

1. Open your project folder in your terminal:
```bash
cd password-entropy-analyzer

```


2. Run the application:
```bash
python main.py

```



---

## 💡 How It Works (Under the Hood)

1. **Entropy ($\mathbf{E}$):** Calculated by multiplying the password length ($L$) by the base-2 logarithm of the character pool size ($R$). Each bit added exponentially increases the time required for brute-force attacks.
2. **Security:** Built using Python's `secrets` module instead of the standard `random` module to ensure pseudo-random number generation is cryptographically strong.

```

```