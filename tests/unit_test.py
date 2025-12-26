import pytest
from src.features import hash_feature

def test_hash_feature_deterministic():
    """
    Same input should always return the same bucket.
    """
    bucket1 = hash_feature("user_123", num_buckets=50)
    bucket2 = hash_feature("user_123", num_buckets=50)

    assert bucket1 == bucket2


def test_hash_feature_bucket_range():
    """
    Output bucket must be within valid range.
    """
    bucket = hash_feature("product_999", num_buckets=100)

    assert 0 <= bucket < 100


def test_hash_feature_known_value():
    """
    Known input should map to expected bucket.
    """
    bucket = hash_feature("mlops", num_buckets=10)

    # Deterministic expected value
    assert bucket == 3


def test_hash_feature_invalid_input():
    """
    Non-string input should raise ValueError.
    """
    with pytest.raises(ValueError):
        hash_feature(12345)
return hash_int / num_buckets