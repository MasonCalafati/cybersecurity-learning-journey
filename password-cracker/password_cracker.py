import hashlib
import time

def hash_password(password):
    """Hash a password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_crack(target_hash, max_length=4):
    """Try to crack password using brute force (numbers only)"""
    print(f"\n[*] Starting brute force attack...")
    print(f"[*] Trying all combinations up to {max_length} digits...")
    
    start_time = time.time()
    attempts = 0
    
    for length in range(1, max_length + 1):
        for num in range(10 ** (length - 1), 10 ** length):
            attempts += 1
            password = str(num)
            
            if hash_password(password) == target_hash:
                elapsed = time.time() - start_time
                print(f"\n[+] PASSWORD CRACKED!")
                print(f"[+] Password: {password}")
                print(f"[+] Attempts: {attempts}")
                print(f"[+] Time: {elapsed:.2f} seconds")
                return password
    
    print(f"\n[-] Password not found")
    print(f"[-] Attempts: {attempts}")
    return None

def dictionary_crack(target_hash, wordlist):
    """Try to crack password using dictionary attack"""
    print(f"\n[*] Starting dictionary attack...")
    print(f"[*] Testing {len(wordlist)} common passwords...")
    
    start_time = time.time()
    
    for i, password in enumerate(wordlist, 1):
        if hash_password(password) == target_hash:
            elapsed = time.time() - start_time
            print(f"\n[+] PASSWORD CRACKED!")
            print(f"[+] Password: {password}")
            print(f"[+] Attempts: {i}")
            print(f"[+] Time: {elapsed:.2f} seconds")
            return password
    
    print(f"\n[-] Password not found in dictionary")
    return None

COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty", "abc123",
    "monkey", "1234567", "letmein", "trustno1", "dragon",
    "baseball", "iloveyou", "master", "sunshine", "ashley",
    "bailey", "shadow", "123123", "654321", "superman"
]

print("=" * 50)
print("    PASSWORD CRACKER DEMONSTRATION")
print("=" * 50)
print("\nWARNING: For educational purposes only!")
print("This demonstrates why strong passwords are important.\n")

demo_password = input("Enter a password to test (or press Enter for demo): ")

if not demo_password:
    demo_password = "1234"
    print(f"\n[*] Using demo password: {demo_password}")

target_hash = hash_password(demo_password)
print(f"[*] Password hash: {target_hash}")

print("\n--- Method 1: Dictionary Attack ---")
result = dictionary_crack(target_hash, COMMON_PASSWORDS)

if not result and demo_password.isdigit() and len(demo_password) <= 4:
    print("\n--- Method 2: Brute Force Attack ---")
    result = brute_force_crack(target_hash, max_length=4)

if result:
    print(f"\n[!] CONCLUSION: Password '{result}' is WEAK and easily cracked!")
    print("[!] Use longer passwords with letters, numbers, and symbols.")
else:
    print(f"\n[+] This password appears strong!")
    print("[+] Not found in common passwords or simple brute force.")

print("\n" + "=" * 50)
