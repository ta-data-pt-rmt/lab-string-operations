import re


blacklist = ['and', 'as', 'an', 'a', 'the', 'in', 'it']

poem = """I was angry with my friend; 
I told my wrath, my wrath did end.
I was angry with my foe: 
I told it not, my wrath did grow. 

And I waterd it in fears,
Night & morning with my tears: 
And I sunned it with smiles,
And with soft deceitful wiles. 

And it grew both day and night. 
Till it bore an apple bright. 
And my foe beheld it shine,
And he knew that it was mine. 

And into my garden stole, 
When the night had veild the pole; 
In the morning glad I see; 
My foe outstretched beneath the tree."""

# Your code here:


poem_clean = poem.lower()
poem_split = poem_clean.split()
poem_split_and_clean = [word.strip(".,:;\n").lower() for word in poem_split]

def comparison_word(text_1,text_2):
    compared_words = [word for word in text_1 if word not in text_2]
    return compared_words

compared_words= comparison_word(poem_split_and_clean,blacklist)

print(compared_words)