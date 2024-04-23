import re
from collections import Counter
import nltk
from nltk.corpus import stopwords
from tabulate import tabulate

nltk.download('stopwords')

def process_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()  # Convert text to lowercase
    
    words = re.findall(r'\b\w+\b', text)
    
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    
    word_freq = Counter(filtered_words)
    
    return word_freq

def print_frequency_table(word_freq):
    table_data = [[word, freq] for word, freq in word_freq.items()]
    
    table_data.sort(key=lambda x: x[1], reverse=True)
    
    print(tabulate(table_data, headers=['Word', 'Frequency'], tablefmt='grid'))

def main():
    file_path = './paragraphs.txt'
    
    word_freq = process_text(file_path)
    
    print_frequency_table(word_freq)

if __name__ == "__main__":
    main()
