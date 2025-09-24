from challenges.python.spin_words import spin_words
import pytest

@pytest.mark.parametrize("string, expected, description", [
	# base cases
	("Hey fellow warriors", "Hey wollef sroirraw", "test 1"),
	("This is a test", "This is a test", "'This is a test' should equal 'This is a test'"),
	("This is another test", "This is rehtona test", "test 3"),
	# edge cases
	("word", "word", "test 4"),
	("words", "sdrow", "test 5"), 
    ("a", "a", "test 6")
])

def test_base_cases(string, expected, description):
	assert spin_words(string) == expected, description

def test_type_validation():
    # Test valid input
    assert spin_words("hello") == "olleh"
    
    # Test invalid types
    with pytest.raises(TypeError, match="Expected str, got int"):
        spin_words(123)
    
    with pytest.raises(TypeError, match="Expected str, got list"):
        spin_words(["hello", "world"])
    
    with pytest.raises(TypeError, match="Expected str, got NoneType"):
        spin_words(None)	
        												
    with pytest.raises(ValueError, match="Input cannot be None"):
     	spin_words("")
        



