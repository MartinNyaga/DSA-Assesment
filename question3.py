'''
Dictionaries: 

Question 3: Implement a function word_frequency(sentence) that takes 
a sentence and returns a dictionary containing the frequency of each 
word in the sentence. 

Ignore punctuation and consider words in a case-insensitive manner. 

sample input = 

sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
'''

def word_frequency(sentence):
    content = sentence.split()
    result = [word.strip("?,!.") for word in content]
    return {word: result.count(word) for word in result}
    
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)
    
    