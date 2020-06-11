from thirdparty import pyteaser

from exnihilo import data

text = data.read_from_file("../input.txt")

print(pyteaser.Summarize(title="", text=text, sentence_num=3).replace('\n', ''))
