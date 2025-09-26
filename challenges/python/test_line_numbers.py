from challenges.python.line_numbers import number
import pytest

@pytest.mark.parametrize("list, expected, description", [
	# base cases
	(["a", "b"], ["1: a", "2: b"], "test 1"),
    (["a", "b", "c", "d"], ["1: a", "2: b", "3: c", "4: d"], "test 2"),

	# edge cases
     ([], [], "test 3"),
])

def test_base_cases(list, expected, description):
	assert number(list) == expected, description

# Option 1 for type validation using parametrize
# @pytest.mark.parametrize("invalid_input, expected_error", [
#     (123, "Expected list, got int"),
#     ("hello", "Expected list, got str"),
#     (None, "Expected list, got NoneType"),
#     (["a", 2, 3, True], "All elements must be strings"),
# ], ids=[
#     "integer_input",
#     "string_input", 
#     "none_input",
#     "mixed_types_in_list"
# ])
# def test_type_validation_errors(invalid_input, expected_error):
#     with pytest.raises(TypeError, match=expected_error):
#         number(invalid_input)

# Option 2 for type validation - separate tests for each
def test_valid_list_input():
    # Test normal operation with valid string list
    assert number(["a", "b" ,"c", "d", "e"]) == ["1: a", "2: b", "3: c", "4: d", "5: e"]

def test_non_list_inputs():
    # Test rejection of non-list inputs
    with pytest.raises(TypeError, match="Expected list, got int"):
        number(123)

def test_string_input_rejection():
    # Test rejection of string input
    with pytest.raises(TypeError, match="Expected list, got str"):
        number("hello")

def test_none_input_rejection():
    # Test rejection of None input
    with pytest.raises(TypeError, match="Expected list, got NoneType"):
        number(None)

def test_mixed_type_list_rejection():
    # Test rejection of list with non-string elements
    with pytest.raises(TypeError, match="All elements must be strings"):
        number(["a", 2, 3, True])