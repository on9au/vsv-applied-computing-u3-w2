"""VSV Applied Computing U3W2 Task 1b Submission File
All the files have been combined into a single file for submission.

@Author: Dylan Jong
"""

# Taken directly from the task pdf
def perimeter_rectangle(length, width):
    perimeter = 2 * (length + width)
    return perimeter
    
def area_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle given the length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

def test_area_rectangle():
    """Test the area_rectangle function."""
    # Test 1
    assert area_rectangle(4, 3) == 12
    # Test 2
    assert area_rectangle(6, 3) == 18
    # Test 3
    assert area_rectangle(6, 6) == 36
    
def test_perimeter_rectangle():
    """Test the perimeter_rectangle function."""
    # Test 1
    assert perimeter_rectangle(4, 3) == 14
    # Test 2
    assert perimeter_rectangle(6, 3) == 18
    # Test 3
    assert perimeter_rectangle(6, 6) == 24

# Test the functions
if __name__ == "__main__":
    test_area_rectangle()
    test_perimeter_rectangle()
    print("All tests passed!")