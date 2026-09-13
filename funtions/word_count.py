# Count the number of words in the text file we need to find the frequency of the words and letters in the file 

# step 1 : open the file in the program with the file path
# step 2 : seperate the words form the sentece
# step 3 : count the words in the sentence
# step 4 : seperate the letters form the sentences
# step 5 : count the repeated letters in the file 
# step 6 : display it on the terminal


def word_counter(file_path):
    word_count = {}
    with open(file_path,'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                cleaned = word.lower().strip(",./\'''{}")
                if cleaned in word_count:
                    word_count[cleaned]+= 1
                else:
                    word_count[cleaned] = 1
                    
    return word_count

def letter_counter(file_path):
    letter_count = {}
    each_letter = []

    with open(file_path) as file:
        for words in file:
            word = words.split()
            for letter in word:
                check = letter.lower().strip("',.\'' '''{}")
                for each in check:
                    each_letter.append(each)
                for ler in each_letter:
                    num = ler.strip("',.\'{}")
                    if num in letter_count:
                        letter_count[num]+=1
                    else:
                        letter_count[num]=1
    return letter_count

word_Count = word_counter("./sample.txt")
letter_Count = letter_counter("./sample.txt")

print(word_Count)

print(" ")

print(letter_Count)
