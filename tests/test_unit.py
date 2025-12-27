from app.features import hash_feature

def test_hash_feature_consistency():
    # Unit test: Fast, no external deps
    input_val = "user_12345"
    result = hash_feature(input_val)
    assert isinstance(result, int)
    # Ensure same input always gives same output
    assert hash_feature(input_val) == result
