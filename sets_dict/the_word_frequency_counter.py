review="clean fast clean reliable fast clean "
words=review.split()
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
print(word_count)
