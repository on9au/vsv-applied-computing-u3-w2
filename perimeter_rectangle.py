# Taken from the task pdf

def perimeter_rectangle(length, width):
    perimeter = 2 * (length + width)
    return perimeter

if __name__ == "__main__":
    # Tested with:
    # - length = 4, width = 3
    # - length = 6, width = 3
    # - length = 6, width = 6
    perimeter_result = perimeter_rectangle(4, 3)

    print(perimeter_result)