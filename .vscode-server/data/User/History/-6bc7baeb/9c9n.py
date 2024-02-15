def main():
    book_path = "/home/llama/workspace/github.com/LLAMA/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    letter_dict = letter_count(text)
    print(letter_dict)
    
def word_count(text):
    words = text.split()
    return len(words)    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def letter_count(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] -= 1
    return chars

    

main()