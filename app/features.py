import hashlib

def hash_feature(input_string, num_buckets=1000):
    """Hashes a high-cardinality string into a fixed number of buckets."""
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    hash_obj = hashlib.md5(input_string.encode())
    return int(hash_obj.hexdigest(), 16) % num_buckets
