import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


bet = {row.letter:row.code for (index, row) in data.iterrows()}



word = input("Enter a word:").upper()
output_list = [bet[letter] for letter in word]
print(output_list)