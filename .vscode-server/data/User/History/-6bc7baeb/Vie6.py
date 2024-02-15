def main():
    book_path = "/home/llama/workspace/github.com/LLAMA/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")
    
def word_count(text):
    words = text.split()
    return len(words)    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    


main()