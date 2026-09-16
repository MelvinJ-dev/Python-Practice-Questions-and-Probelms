# Input: "hello world hello"
# Output: {'hello': 2, 'world': 1}

# Input: "the quick brown fox jumps over the lazy dog"
# Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}



sentence = "the quick brown fox jumps over the lazy dog"

def word_counter(sentence):
    

    output = {}
    if sentence=="":
        print({})
    else:
        words = sentence.split(" ")
        for word in words:
            if word in output:
                output[word]+=1
            else:
                output[word]=1
        
        print(output)


word_counter('')