"""Basic tests to test testing system."""
import example_project


def test_import():
    """Package testing stub."""
    assert example_project.TEST_VAR == 1
    
def test_function():
    assert example_project.f1() == 1
