def most_frequent(string):
    # Create an empty dictionary to store the letter frequencies
    freq_dict = {}

    # Iterate through each character in the string
    for char in string:
        # Increment the count of the current character in the dictionary
        freq_dict[char] = freq_dict.get(char, 0) + 1

    # Sort the dictionary by values in descending order
    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    # Print the letters and their frequencies in decreasing order
    for item in sorted_dict:
        print(f"{item[0]} = {item[1]:02}")

# Test the function
input_string = input("Please enter a string: ")
most_frequent(input_string)
