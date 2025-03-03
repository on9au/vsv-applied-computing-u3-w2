"""VSV Applied Computing U3W2 Task 1b - Area of a Rectangle
@Author: Dylan Jong
"""

def area_rectangle(length: float, width: float) -> float:
    """Calculate the area of a rectangle given the length and width.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    return length * width

if __name__ == "__main__":
    # Tested with:
    # - length = 4, width = 3
    # - length = 6, width = 3
    # - length = 6, width = 6
    area_result = area_rectangle(4, 3)

    print(area_result)