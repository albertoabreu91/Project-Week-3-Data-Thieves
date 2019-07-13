from textblob import TextBlob
from lang_country import *

sting_to_analyze = input("Wich event you want to analyze: ")
string_to_analyze = "Arab spring"
blob = TextBlob(string_to_analyze)
print(blob.translate(to="ca"))

