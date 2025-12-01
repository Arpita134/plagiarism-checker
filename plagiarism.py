# from difflib import SequenceMatcher
# with open('demo1.txt') as one_file,open('demo2.txt') as two_file:
#     data_file1=one_file.read()
#     data_file2=two_file.read()
#     matches=SequenceMatcher(None,data_file1,data_file2).ratio()
#     print(f"the plagiarised content {matches*100}%")
from difflib import SequenceMatcher
import string

def clean_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Normalize whitespace (remove extra spaces and newlines)
    text = ' '.join(text.split())
    return text

# Read file contents
with open('demo1.txt', 'r') as file1, open('demo2.txt', 'r') as file2:
    data_file1 = file1.read()
    data_file2 = file2.read()

# Clean both texts
cleaned_file1 = clean_text(data_file1)
cleaned_file2 = clean_text(data_file2)

# Calculate similarity ratio
similarity_ratio = SequenceMatcher(None, cleaned_file1, cleaned_file2).ratio()

# Print a clean report
print("Plagiarism Detection Report")
print(f"Similarity Score: {similarity_ratio * 100:.2f}%")
if similarity_ratio > 0.8:
    print(" High similarity detected. Possible plagiarism.")
elif similarity_ratio > 0.5:
    print(" Moderate similarity found.")
else:
    print(" Low similarity; likely no plagiarism.")
