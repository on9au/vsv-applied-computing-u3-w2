import area_rectangle
import perimeter_rectangle

def test_area_rectangle():
    # Test 1
    assert area_rectangle.area_rectangle(4, 3) == 12
    # Test 2
    assert area_rectangle.area_rectangle(6, 3) == 18
    # Test 3
    assert area_rectangle.area_rectangle(6, 6) == 36
    
def test_perimeter_rectangle():
    # Test 1
    assert perimeter_rectangle.perimeter_rectangle(4, 3) == 14
    # Test 2
    assert perimeter_rectangle.perimeter_rectangle(6, 3) == 18
    # Test 3
    assert perimeter_rectangle.perimeter_rectangle(6, 6) == 24
    
if __name__ == "__main__":
    test_area_rectangle()
    test_perimeter_rectangle()
    print("All tests passed!")