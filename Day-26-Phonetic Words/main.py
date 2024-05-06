import pandas as pd

# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# student_data = pd.DataFrame(student_dict)
# print(student_data)

# Loop through data frame
# for (key, value) in student_data.items():
#     print(value)

# Loop through rows of a data frame
# for (index, row) in student_data.iterrows():
#     print(row.score)
#     print(row)


data = pd.read_csv("nato_phonetic_alphabet.csv")
word_list = {}
for i in range(len(data)):
    word_list[data.letter[i]] = data.code[i]

# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)


# final_output = []
# for i in output:
#     x = word_list[i]
#     final_output.append(x)
# print(final_output)

def generate_phonetic():
    output = input("Enter a word: ").upper()
    try:
        final_output = [word_list[item] for item in output]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(final_output)


generate_phonetic()
