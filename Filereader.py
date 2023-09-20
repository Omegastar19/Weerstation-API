import os


def list_text_files(sub_directory):
    # List all .txt files in the specified sub-directory
    txt_files = [f for f in os.listdir(sub_directory) if f.endswith('.txt')]
    return txt_files


def lees_text_document(sub_directory, filename):
    # Check if the file exists
    file_path = os.path.join(sub_directory, filename)
    if not os.path.isfile(file_path):
        print(f"The file '{file_path}' does not exist.")
        return

    # Open and read the .txt file
    with open(file_path, 'r') as txt_file:
        content = txt_file.read()
        print(content)


def main():
    sub_directory = 'weerberichten'  # Specify the sub-directory

    while True:
        # List all .txt files in the sub-directory
        txt_files = list_text_files(sub_directory)

        if not txt_files:
            print("No .txt files found in the sub-directory.")
            break

        print("List of .txt files in the sub-directory:")
        for i, filename in enumerate(txt_files, 1):
            print(f"{i}. {filename}")

        selection = input("Enter the number of the .txt file to read (or '0' to exit): ")

        if selection == '0':
            break

        try:
            index = int(selection)
            if 1 <= index <= len(txt_files):
                selected_file = txt_files[index - 1]
                lees_text_document(sub_directory, selected_file)
            else:
                print("Invalid selection. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number or '0' to exit.")


if __name__ == "__main__":
    main()