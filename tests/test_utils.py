import unittest
import sys
import os

# Add the parent directory to the path so we can import from utils.py
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import validate_name, validate_email, validate_form_data


class TestNameValidation(unittest.TestCase):
    """Test cases for name validation."""
    
    def test_valid_names(self):
        """Test valid name inputs."""
        valid_names = [
            "John",
            "Mary-Jane", 
            "O'Connor",
            "Jean Pierre",
            "Al"
        ]
        
        for name in valid_names:
            with self.subTest(name=name):
                is_valid, error = validate_name(name)
                self.assertTrue(is_valid, f"Name '{name}' should be valid")
                self.assertEqual(error, "")
    
    def test_invalid_names(self):
        """Test invalid name inputs."""
        invalid_names = [
            "",           # Empty string
            "   ",        # Only spaces
            "A",          # Too short
            "John123",    # Contains numbers
            "John@",      # Contains invalid characters
        ]
        
        for name in invalid_names:
            with self.subTest(name=name):
                is_valid, error = validate_name(name)
                self.assertFalse(is_valid, f"Name '{name}' should be invalid")
                self.assertNotEqual(error, "")


class TestEmailValidation(unittest.TestCase):
    """Test cases for email validation."""
    
    def test_valid_emails(self):
        """Test valid email inputs."""
        valid_emails = [
            "test@example.com",
            "user.name@domain.org",
            "first.last@subdomain.example.co.uk",
            "user+tag@example.com"
        ]
        
        for email in valid_emails:
            with self.subTest(email=email):
                is_valid, error = validate_email(email)
                self.assertTrue(is_valid, f"Email '{email}' should be valid")
                self.assertEqual(error, "")
    
    def test_invalid_emails(self):
        """Test invalid email inputs."""
        invalid_emails = [
            "",                    # Empty string
            "   ",                 # Only spaces  
            "plainaddress",        # No @ symbol
            "@missinglocal.com",   # Missing local part
            "missing.domain@",     # Missing domain
            "double@@domain.com",  # Double @ symbol
            "user@.domain.com",    # Domain starts with dot
            "user@domain.com.",    # Domain ends with dot
            "user@nodot",          # Domain has no dot
        ]
        
        for email in invalid_emails:
            with self.subTest(email=email):
                is_valid, error = validate_email(email)
                self.assertFalse(is_valid, f"Email '{email}' should be invalid")
                self.assertNotEqual(error, "")


class TestFormValidation(unittest.TestCase):
    """Test cases for complete form validation."""
    
    def test_valid_form_data(self):
        """Test valid form data."""
        is_valid, errors = validate_form_data("John", "Doe", "john.doe@example.com")
        self.assertTrue(is_valid)
        self.assertEqual(len(errors), 0)
    
    def test_invalid_form_data(self):
        """Test invalid form data."""
        is_valid, errors = validate_form_data("", "", "invalid-email")
        self.assertFalse(is_valid)
        self.assertEqual(len(errors), 3)  # All fields should have errors
    
    def test_mixed_form_data(self):
        """Test form data with some valid and some invalid fields."""
        is_valid, errors = validate_form_data("John", "", "john@example.com")
        self.assertFalse(is_valid)
        self.assertEqual(len(errors), 1)  # Only last name should have error
        self.assertIn("Last name:", errors[0])


if __name__ == '__main__':
    unittest.main()