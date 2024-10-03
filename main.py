def main():
    book_path = "books/frankenstein.txt"
    text = get_words(book_path)
    num_words = count_words(text)
    char_dict = count_characters(text)
    cd_list = [{"char": char, "num": count} for char, count in char_dict.items()]
    cd_list.sort(reverse=True, key=sort_on)
   #The Following line will print the entire book if uncommented 
    #print(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char in cd_list:
        if char['char'].isalpha():
            print(f"The character '{char['char']}' appears {char['num']} times.")
    print("--- End report ---")

def get_words(path):
     with open(path) as f:
        return f.read()
        
def count_words(text):
    count = text.split()
    return len(count)

def count_characters(text):
    character_dict = {}
    lowered = text.lower()
    for character in lowered:
        if character in character_dict:
            character_dict[character] += 1
        else:
            character_dict[character] = 1
    return character_dict

def sort_on(dict):
        return dict["num"]

main()