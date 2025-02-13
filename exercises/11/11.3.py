# 11-3. Word Count

def word_count(sentence):
  words = sentence.split(' ')
  return len(words)

sentence = "I'm so cool."

print(word_count(sentence))