import pytest
from app.features import hash_feature

def test_hash_feature_consistency():
    """
    Part 1 Requirement: Fast, isolated unit test.
    Checks if the same input always yields the same output.
    """
    input_val = "mlops_user_123"
    result1 = hash_feature(input_val)
    result2 = hash_feature(input_val)
    
    assert isinstance(result1, int)
    assert result1 == result2

def test_hash_feature_range():
    """
    Checks if output is within bucket definition.
    """
    input_val = "test_item"
    buckets = 100
    result = hash_feature(input_val, num_buckets=buckets)
    assert 0 <= result < buckets

def test_invalid_input():
    """
    Checks error handling for non-string inputs.
    """
    with pytest.raises(ValueError):
        hash_feature(12345)
