import math
import string
import os

def _determine_character_space(credential: str) -> int:
    """
    Computes the total active character pool size (R) based on 
    comprehensive charset inclusion criteria for Shannon entropy analysis.
    """
    has_lowercase = any(char in string.ascii_lowercase for char in credential)
    has_uppercase = any(char in string.ascii_uppercase for char in credential)
    has_digits    = any(char in string.digits for char in credential)
    has_symbols   = any(char in string.punctuation for char in credential)
    
    radix = 0
    if has_lowercase: radix += 26
    if has_uppercase: radix += 26
    if has_digits:    radix += 10
    if has_symbols:   radix += len(string.punctuation)
        
    return radix

def evaluate_shannon_entropy(credential: str) -> float:
    """
    Calculates the Shannon entropy (in bits) of a given credential string.
    Formula: H = L * log2(R)
    where L is length and R is the character space cardinality.
    """
    if not credential:
        return 0.0
    
    length = len(credential)
    radix = _determine_character_space(credential)
    
    if radix == 0:
        return 0.0
    
    entropy_bits = length * math.log2(radix)
    return round(entropy_bits, 2)

def inspect_structural_vulnerabilities(credential: str) -> list[str]:
    """
    Performs heuristic pattern matching to detect common structural weaknesses,
    repetitive sequences, and predictable keyboard walks.
    """
    vulnerabilities = []
    
    # Evaluate sequential character repetition (e.g., 'aaa', '111')
    for idx in range(len(credential) - 2):
        if credential[idx] == credential[idx+1] == credential[idx+2]:
            vulnerabilities.append("Identified excessive character repetition sequence")
            break
            
    # Check against common structural keyboard walks
    known_walks = ["12345", "123456", "qwerty", "asdfgh", "zxcvbn", "password", "admin", "abcde"]
    lowered_cred = credential.lower()
    for walk in known_walks:
        if walk in lowered_cred:
            vulnerabilities.append(f"Contains predictable keyboard walk or common token ('{walk}')")
            break
            
    return vulnerabilities

def cross_reference_breach_corpus(credential: str, corpus_filepath: str = "common_passwords.txt") -> bool:
    """
    Performs O(1) average-time set lookup against a local corpus 
    of compromised or high-frequency weak passwords.
    """
    if not os.path.exists(corpus_filepath):
        return False
        
    try:
        with open(corpus_filepath, "r", encoding="utf-8") as file_corpus:
            compromised_set = {line.strip().lower() for line in file_corpus if line.strip()}
            return credential.lower() in compromised_set
    except Exception:
        # Fail safe if I/O exceptions occur
        return False