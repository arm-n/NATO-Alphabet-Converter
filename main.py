import pandas

data = pandas.read_csv("NATO.csv")

nato_dict = data.to_dict()
nato_df = pandas.DataFrame(nato_dict)
print(nato_df)

letter_code = {row.letter:row.code for (index,row) in nato_df.iterrows()}
print(letter_code)
name = input('Enter a word: ').upper()
name_list = [letter_code[letter] for letter in name if letter in letter_code]
print(name_list)
