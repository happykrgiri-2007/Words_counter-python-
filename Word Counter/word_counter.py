


# Word Counter Using Python

import re

def word_counter():

    print("\n====================================")
    print("          WORD COUNTER")
    print("====================================")

    # Taking file name from user
    file_name = input("\nEnter text file name: ")

    try:
        # Opening and reading the file
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read()

        # Splitting content into words
        words = re.findall(r"\b[\w']+\b", content)

        # Counting total words
        total_words = len(words)

        # Displaying results
        print("\n========== RESULT ==========")

        print("File Name:", file_name)
        print("Total Words:", total_words)
        print("Total Characters:", len(content))
        print("Total Lines:", len(content.splitlines()))

        print("============================")

    except FileNotFoundError:
        print("\nError: File not found!")
        print("Please check the file name and try again.")

    except PermissionError:
        print("\nError: Permission denied!")

    except UnicodeDecodeError:
        print("\nError: Unable to read the file encoding.")

    except Exception as error:
        print("\nAn unexpected error occurred:", error)


# Main program
if __name__ == "__main__":
    word_counter()
