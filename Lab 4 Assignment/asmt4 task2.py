def cm_to_inches(cm):
    """
    Convert centimeters to inches
    
    Args:
        cm (float): Length in centimeters
        
    Returns:
        float: Length in inches
    """
    return cm / 2.54

# Example usage
if __name__ == "__main__":
    # Test the function
    centimeters = 25.4
    inches = cm_to_inches(centimeters)
    print(f"{centimeters} centimeters is equal to {inches} inches")
