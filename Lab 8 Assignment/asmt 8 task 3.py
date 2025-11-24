def is_sentence_palindrome(sentence):
    # Remove spaces, punctuation, and convert to lowercase
    cleaned = ''.join(ch.lower() for ch in sentence if ch.isalnum())
    
    # Check palindrome condition
    return cleaned == cleaned[::-1]


# --- User Input ---
sentence = input("Enter a sentence: ")

if is_sentence_palindrome(sentence):
    print("✅ It's a palindrome!")
else:
    print("❌ Not a palindrome.")