string=input("Enter a string: ")

def word_freq(s):
    words=s.lower().split()
    freq={}
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
    return freq

print(word_freq(string))

