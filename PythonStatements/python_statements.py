st = 'Print only the words that start with s in this sentence'

#for word in st.split():
#    if word[0].lower() == 's':
#        print(word)

for word in st.split():
    if len(word) % 2 == 0:
        print(word + " is even!")