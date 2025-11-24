def convert_date_format(date_str):
    # Split the date into parts
    parts = date_str.split('-')
    
    # Ensure 3 parts: year, month, day
    if len(parts) != 3:
        return "Invalid format ❌"
    
    year, month, day = parts
    
    # Validate numeric parts
    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return "Invalid date ❌"
    
    # Check valid lengths
    if len(year) != 4 or len(month) != 2 or len(day) != 2:
        return "Invalid format ❌"
    
    # Return converted format
    return f"{day}-{month}-{year}"


# --- User Input ---
date_str = input("Enter date in YYYY-MM-DD format: ")
print("Converted Date Format:", convert_date_format(date_str))