import re
def extract_digits(text):
    # Find all digits in the text
    return ''.join(re.findall(r'\d+', text))