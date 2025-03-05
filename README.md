# NATO-Alphabet-Converter
This project is a simple NATO Phonetic Alphabet Converter built using Python and the pandas library. It converts any word entered by the user into its corresponding phonetic code using the NATO alphabet.

Features

✅ Converts words to NATO phonetic alphabet.
✅ Handles case-insensitive input.
✅ Ignores characters not in the alphabet (e.g., punctuation).
✅ Uses pandas for efficient CSV handling.

How It Works

Reads NATO.csv, which contains letters and their corresponding NATO phonetic codes.
Takes a user-inputted word.
Converts each letter of the word into its phonetic equivalent.

Example Output

If the user enters:
Enter a word: Armaan
The output will be:
['Alfa', 'Romeo', 'Mike', 'Alfa', 'Alfa', 'November']

Prerequisites,
Ensure you have Python installed (>=3.8) and install the required package:

pip install pandas

How to Run

Clone this repository:

git clone https://github.com/arm-n/nato-alphabet-converter.git
cd nato-alphabet-converter

Ensure NATO.csv exists in the project directory and contains two columns:

letter,code
A,Alfa
B,Bravo
...

Run the script:
python main.py

Contributions,
Feel free to fork and submit a pull request if you'd like to enhance this project!

License
This project is licensed under the MIT License.
