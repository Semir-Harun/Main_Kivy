"""
Utility functions for form validation.

This module provides reusable validation functions that can be tested independently.
"""


def validate_name(name):
    """
    Validate a name field.
    
    Args:
        name (str): The name to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not name or not name.strip():
        return False, "Name is required"
    
    name = name.strip()
    if len(name) < 2:
        return False, "Name must be at least 2 characters long"
    
    if not name.replace(" ", "").replace("-", "").replace("'", "").isalpha():
        return False, "Name can only contain letters, spaces, hyphens, and apostrophes"
    
    return True, ""


def validate_email(email):
    """
    Validate an email address.
    
    Args:
        email (str): The email to validate
        
    Returns:
        tuple: (is_valid, error_message)
    """
    if not email or not email.strip():
        return False, "Email is required"
    
    email = email.strip()
    
    # Basic email validation
    if "@" not in email:
        return False, "Email must contain @ symbol"
    
    if email.count("@") != 1:
        return False, "Email must contain exactly one @ symbol"
    
    local, domain = email.split("@")
    
    if not local:
        return False, "Email must have content before @ symbol"
    
    if not domain:
        return False, "Email must have content after @ symbol"
    
    if "." not in domain:
        return False, "Email domain must contain a dot"
    
    if domain.startswith(".") or domain.endswith("."):
        return False, "Email domain cannot start or end with a dot"
    
    return True, ""


def validate_form_data(first_name, last_name, email):
    """
    Validate all form data.
    
    Args:
        first_name (str): First name input
        last_name (str): Last name input  
        email (str): Email input
        
    Returns:
        tuple: (is_valid, list_of_errors)
    """
    errors = []
    
    # Validate first name
    is_valid, error = validate_name(first_name)
    if not is_valid:
        errors.append(f"First name: {error}")
    
    # Validate last name
    is_valid, error = validate_name(last_name)
    if not is_valid:
        errors.append(f"Last name: {error}")
    
    # Validate email
    is_valid, error = validate_email(email)
    if not is_valid:
        errors.append(f"Email: {error}")
    
    return len(errors) == 0, errors