import hashlib

def hash_feature(value: str, num_buckets: int = 100) -> int:
    """
    Deterministic hashing for categorical features.
    """
    if not isinstance(value, str):
        raise ValueError("Input must be a string")

    hash_object = hashlib.md5(value.encode("utf-8"))
    hash_int = int(hash_object.hexdigest(), 16)
    return hash_int % num_buckets
