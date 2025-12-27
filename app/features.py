import hashlib

def hash_feature(input_string, num_buckets=1000):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    # MD5 hash for deterministic results
    hash_obj = hashlib.md5(input_string.encode())
    # SABOTAGE (Part 3): Syntax Error
    return (int(hash_obj.hexdigest(), 16) % num_buckets + 1  # Missing closing parenthesis! Syntax Error!
