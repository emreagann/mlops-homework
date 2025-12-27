import hashlib

def hash_feature(input_string, num_buckets=1000):
    """
    Hashes a string into a fixed number of buckets.
    Part 1 requirement: Logic for feature engineering.
    """
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    # MD5 hash for deterministic results
    hash_obj = hashlib.md5(input_string.encode())
    # SABOTAGE (Part 3): Intentionally introduced bug
    # Correct logic: return int(hash_obj.hexdigest(), 16) % num_buckets
    # Buggy logic: Adding +1 to force test failure
    return (int(hash_obj.hexdigest(), 16) % num_buckets) + 1
