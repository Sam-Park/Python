sentence = "Hey fellow warriors"
newSentence = []
def spin_words(sentence):
    # Your code goes here
    print(' '.join([len(w) < 5 and w or w[::-1] for w in sentence.split() ]))
            
    
spin_words(sentence)