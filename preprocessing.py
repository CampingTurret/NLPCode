import re
import string
import contractions
import typing 

# Case folding
def case_folding(text):
    return text.lower()

# Removing links
def remove_links(text):
    # Define a regular expression pattern for matching URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')

    # Use the sub function to replace matched URLs with an empty string
    text_without_links = url_pattern.sub('', text)

    return text_without_links

# Removing punctuation
def remove_punctuation(text):
    translator = str.maketrans("", "", string.punctuation)
    text_without_punctuation = text.translate(translator)
    
    return text_without_punctuation

# Expanding contractions
def expand_contractions(text):
    expanded_text = contractions.fix(text)
    return expanded_text


# Combining all preprocessing functions
def text_cleaning(text, func_list):
    for f in func_list:
        text = f(text)
    
    return text

def dataset_cleaning(text_gen: typing.Generator):
    
    for text in text_gen:

        # Applying preprocessing functions to each text
        func_list = [case_folding, remove_links, remove_punctuation, expand_contractions]
        clean_text = text
        for op in func_list:
            clean_text = op(clean_text)
        yield clean_text

if __name__ == '__main__':
    test_dataset = ['Hello!!!', '[deleted]', '[removed]', 'I cant wait', "I wouldn't", ' check this link: www.tudelft.n']
    print(list(dataset_cleaning(test_dataset)))
