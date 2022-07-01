with open('words.txt') as words: 
  words = words.read()
  words = words.split(', ')
words = set(words)

with open('tweets.txt') as tweets:
  tweets = tweets.read()
  tweets = tweets.split('\n')

def ctoccur(stt):
  ct = 0
  for w in words:
    w = ' '+w+' '
    if w in stt:
      ct += 1
  return ct

def lnStr(stt):
  ct = 0
  for c in stt:
    if c == ' ':
      ct += 1
  return ct

for tweet in tweets:
  text = tweet.split()
  l = 0
  for i in range(len(text)):
    if text[i][0] != '@' and text[i][0:2] != '"@':
      text[l] = text[i]
      l+=1
  text = ' '.join(text[:l])
  ct = ctoccur(text)
  ln = lnStr(text)
  degree_of_profanity = ct/ln if ln != 0 else 0
  if degree_of_profanity>0:
    print(degree_of_profanity, ': ', tweet)
  # print(degree_of_profanity, ': ', tweet)