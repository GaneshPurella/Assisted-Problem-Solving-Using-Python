def is_valid_email(email):
    # Must contain @ and .
    if '@' not in email or '.' not in email:
        return False
    
    # Should not allow multiple @
    if email.count('@') > 1:
        return False
    
    # Should not start or end with special characters
    if not email[0].isalnum() or not email[-1].isalnum():
        return False
    
    return True


# --- User Input ---
email = input("Enter your email: ")

# --- Output ---
if is_valid_email(email):
    print("Valid Email ✅")
else:
    print("Invalid Email ❌")