import pandas as pd

#  Below code gives us phonetic words for a given input word
data = pd.read_csv("nato_phonetic_alphabet.csv")
word_list = {}
for i in range(len(data)):
    word_list[data.letter[i]] = data.code[i]

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


def generate_phonetic():
    output = input("Enter a word: ").upper()
    try:
        final_output1 = [word_list[item] for item in output]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(final_output1)


generate_phonetic()

# Below code is an alternate method for printing Phonetic Words
# ----------------------------------------------------------------------------------
final_output = []
output1 = input("Enter a word: ").upper()
for i in output1:
    x = word_list[i]
    final_output.append(x)
print(final_output)


# ----------------------------------------------------------------------------------
#  Below section of code is an example on how to iterate through dictionary

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
for (key, value) in student_dict.items():
    print(key)
    print(value)

# Creating a DataFrame from Dictionary
student_data = pd.DataFrame(student_dict)
print(student_data)

# Loop through data frame
for (key, value) in student_data.items():
    print(value)

# Loop through rows of a data frame
for (index, row) in student_data.iterrows():
    print(row.score)
    print(row)
# ------------------------------------------------------------------------------------

