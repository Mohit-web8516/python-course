import os

def create_file():
    filename = input("Enter filename to create: ")
    with open(filename, "w") as f:
        f.write("This is a new file.\n")
    print(f"File '{filename}' created successfully.")

def write_file():
    filename = input("Enter filename to write: ")
    text = input("Enter text to write: ")
    with open(filename, "w") as f:
        f.write(text + "\n")
    print(f"Text written to '{filename}'.")

def read_file():
    filename = input("Enter filename to read: ")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            print("File content:\n", f.read())
    else:
        print("File does not exist.")

def append_file():
    filename = input("Enter filename to append: ")
    text = input("Enter text to append: ")
    with open(filename, "a") as f:
        f.write(text + "\n")
    print(f"Text appended to '{filename}'.")

def delete_file():
    filename = input("Enter filename to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    else:
        print("File does not exist.")

def rename_file():
    old_name = input("Enter current filename: ")
    new_name = input("Enter new filename: ")
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
        print(f"File renamed from '{old_name}' to '{new_name}'.")
    else:
        print("File does not exist.")

def check_file():
    filename = input("Enter filename to check: ")
    if os.path.exists(filename):
        print(f"File '{filename}' exists.")
    else:
        print(f"File '{filename}' does not exist.")

def main():
    while True:
        print("\n--- File Handling Menu ---")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Append to File")
        print("5. Delete File")
        print("6. Rename File")
        print("7. Check File Existence")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            append_file()
        elif choice == "5":
            delete_file()
        elif choice == "6":
            rename_file()
        elif choice == "7":
            check_file()
        elif choice == "8":
            print("Exiting... File handling revision complete!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
