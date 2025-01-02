def main():
    # Path to the book file
    book_path = "books/frankenstein.txt"

    # Read the text from the book file
    text = get_book_text(book_path)
    
    # Count the number of words in the text
    num_words = get_num_words(text)

    # Count the number of characters in the text
    chars_dict = get_char_count(text)
    
    # Print a report of characters and respective counts in text
    chars_sorted_list = chars_dict_to_sorted_list(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    # Iterate over the sorted list of character counts
    for item in chars_sorted_list:
        # Skip non-alphabetic characters
        if not item["char"].isalpha():
            continue
        # Print the character and its count
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def sort_on(d):
    """
    Helper function to return the count of characters for sorting.
    
    Args:
    d (dict): A dictionary with 'char' and 'num' keys.
    
    Returns:
    int: The count of the character.
    """
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    """
    Converts a dictionary of character counts to a sorted list of dictionaries.
    
    Args:
    num_chars_dict (dict): A dictionary with characters as keys and their counts as values.
    
    Returns:
    list: A sorted list of dictionaries where each dictionary contains a character and its count.
    """
    sorted_list = []
    # Convert the dictionary to a list of dictionaries
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    # Sort the list in descending order based on the count of characters
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_book_text(path):
    """
    Reads the text from a file at the given path.
    
    Args:
    path (str): The path to the file.
    
    Returns:
    str: The text content of the file.
    """
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    """
    Counts the number of words in the given text.
    
    Args:
    text (str): The text to count words in.
    
    Returns:
    int: The number of words in the text.
    """
    words = text.split()
    return len(words)

def get_char_count(text):
    """
    Counts the number of times each character appears in the given text.
    
    Args:
    text (str): The text to count characters in.
    
    Returns:
    dict: A dictionary with characters as keys and their counts as values.
    """
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# Call the main function to execute the program
main()