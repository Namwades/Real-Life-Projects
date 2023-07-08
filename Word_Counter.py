import string

def word_counter(file_path):
    word_count = {}

    with open(file_path, 'r') as file:
        for line in file:
            # Remove punctuation and convert to lowercase
            line = line.translate(str.maketrans('', '', string.punctuation)).lower()

            # Split line into words
            words = line.split()

            # Update word count
            for word in words:
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    # Sort words by count in descending order
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    # Display word count
    for word, count in sorted_words:
        print(f'{word}: {count}')

def word_counter_main():
    print("Welcome to Word Counter!")

    file_path = input("Enter the path to the text file: ")

    try:
        word_counter(file_path)
    except FileNotFoundError:
        print("File not found.")

if __name__ == '__main__':
    word_counter_main()