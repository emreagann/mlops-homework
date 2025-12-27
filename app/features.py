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
    # Return modulo num_buckets to get an index
    return int(hash_obj.hexdigest(), 16) % num_buckets
