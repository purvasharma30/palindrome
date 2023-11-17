def is_palindrome(input_str):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    cleaned_str = "".join(char.lower() for char in input_str if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

if __name__ == "__main__":
    user_input = input("Enter a word or phrase: ")
    
    if is_palindrome(user_input):
        print(f"{user_input} is a palindrome!")
    else:
        print(f"{user_input} is not a palindrome.")
