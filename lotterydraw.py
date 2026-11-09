
# Personal Journal Program
# Name:
# Class: CIS 105

# Global counter
entry_count = 0


# Function to save a journal entry
def save_entry():
    global entry_count

    entry = input("Write your journal entry: ")

    try:
        with open("/Users/altheaharris/Python Class/november 9th/journal/journal.txt", "a", encoding="utf-8") as journal_file:
            journal_file.write(entry + "\n")

        entry_count += 1

        print("Your journal entry was saved successfully!")
        print("Total entries saved this run:", entry_count)

    except OSError as error:
        print("Sorry, your journal entry could not be saved.")
        print("Error:", error)


# Function to read the journal
def read_journal():

    try:
        journal_file = open("journal.txt", "r", encoding="utf-8")

        print("\n--- YOUR JOURNAL ---")
        print(journal_file.read())

        journal_file.close()

    except FileNotFoundError:
        print("No journal entries found. Write an entry first.")

    except OSError:
        print("Sorry, the journal could not be opened.")


# Main program
while True:

    print("\n===== PERSONAL JOURNAL =====")
    print("1. Write a journal entry")
    print("2. Read journal entries")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        save_entry()

    elif choice == "2":
        read_journal()

    elif choice == "3":
        print("Thank you for using the Personal Journal!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
