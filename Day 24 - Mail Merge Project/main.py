with open("./Input/Names/invited_names.txt") as name_files:
    names = name_files.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    for name in names:
        name = name.strip()
        new_letter = letter_content.replace("[name]", name)
        with open(f"./Output/ReadyToSend/Letter-for-{name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)
