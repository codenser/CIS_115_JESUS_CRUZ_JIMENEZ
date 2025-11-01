#this program counts the frequency of a word using a user-defined function and a dictionary to dertermine its frequency


#I am stating and creating the funtion that will be used
def word_frequency(sentence):
    words = sentence.split()
    print(words)

    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency
#the function will then be called along with the printed result
print(word_frequency("this is night, this is day"))
