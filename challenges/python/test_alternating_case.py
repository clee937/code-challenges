from challenges.python.alternating_case import alternate_case
import pytest

@pytest.mark.parametrize("string, expected, description", [
	# base cases
	("hello world", "HELLO WORLD", "test 1"),
    ("HELLO WORLD", "hello world", "test 2"),
	("hello WORLD", "HELLO world", "test 3"),
    ("HeLLo WoRLD", "hEllO wOrld", "test 4"),
	("String.prototype.toAlternatingCase", "sTRING.PROTOTYPE.TOaLTERNATINGcASE", "test 5"),

	# edge cases
     ("12345", "12345", "numbers should remain unchanged"),
	 ("1a2b3c4d5e", "1A2B3C4D5E", "mixed letters and numbers"),
     ("", "", "empty string")
])

def test_base_cases(string, expected, description):
	assert alternate_case(string) == expected, description

# type validation using parametrize
@pytest.mark.parametrize("invalid_input, expected_error", [
    (123, "Expected str, got int"),
    (["hello"], "Expected str, got list"),
    (None, "Expected str, got NoneType"),
    (True, "Expected str, got bool"),
], ids=[
    "integer_input",
    "list_input", 
    "none_input",
    "boolean_list"
])
def test_type_validation_errors(invalid_input, expected_error):
    with pytest.raises(TypeError, match=expected_error):
        alternate_case(invalid_input)

