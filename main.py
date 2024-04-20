def main():
    # Define the relative path of the file:
    path = "books/frankenstein.txt"
    with open(path) as frankenstein:
        
        #Read and store book contents in a string
        book_contents = frankenstein.read()
        
        #Calculate the number of words in the book
        num_words = count_words(book_contents)

        #Calculate the frequency of each letter in the book and store it in a dictionary
        #and convert that into a list of dictionaries so that it can get sorted
        letters_in_book = letter_freq(book_contents)
        occur_list = dict_to_list(letters_in_book)

        #Output a report
        print(f"--- Begin report of {path} ---")
        print(f"{num_words} words found in the document")
        
        for item in occur_list:
            print(f"The '{item["letter"]}' character was found {item["num"]}")


#Counts and returns the number of words that are inside a string
def count_words(text):
    words = text.split()
    return len(words)

#Calculates the frequency of each letter in a string
def letter_freq(text):
    occur_dict = {}
    lowercase_text = text.lower()

    for letter in lowercase_text:
        if letter.isalpha():
            if letter not in occur_dict:
                occur_dict[letter] = 1
            else:
                occur_dict[letter] += 1

    return occur_dict

#Transform a dictionary into a list of dictionaries so that it can get sorted
def dict_to_list(dict):
    conv_list = []
    for item in dict:
        conv_list.append({"letter": item, "num": dict[item]})
        conv_list.sort(reverse=True, key = sort_on)
    return conv_list

#The key that we base our sort on
def sort_on(dict):
    return dict["num"]


main()
