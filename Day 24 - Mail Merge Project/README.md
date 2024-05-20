# Mail Merge Project

This Python script automates the process of creating personalized letters for a mailing list. It reads a list of names from a file, generates individualized letters, and saves them as separate text files ready for sending.

## Features

1.  **Input Files:** The script reads input data from two files:

    -   `invited_names.txt`: Contains a list of names to personalize the letters.
    -   `starting_letter.txt`: Contains the template for the letter, with a placeholder `[name]` to be replaced with the recipient's name.
2.  **Personalization:** For each name in the list, the script replaces the `[name]` placeholder in the letter template with the actual name. This creates a unique letter for each recipient.

3.  **Output Files:** After personalizing the letters, the script saves them as individual text files in a designated output directory (`./Output/ReadyToSend/`). Each file is named based on the recipient's name.

## Usage

1.  **Input Files:** Prepare the following input files:

    -   `invited_names.txt`: List of names, with each name on a separate line.
    -   `starting_letter.txt`: Template of the letter, with `[name]` as a placeholder for the recipient's name.
2.  **Execution:** Run the Python script. It will read the input files, generate personalized letters, and save them in the output directory.
<hr>

https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/eae85b2d-84c5-418f-bdcd-9668baa68c08

