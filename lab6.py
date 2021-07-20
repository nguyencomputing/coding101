import string
import scipy.stats as stats

a,z = ord(string.ascii_lowercase[0]), ord(string.ascii_lowercase[-1])
A,Z = ord(string.ascii_uppercase[0]), ord(string.ascii_uppercase[-1])


def caesar_encrypt(plaintext, key):
    asciitxt = list(map(ord, str.lower(plaintext)))
    ciphertext = ''
    for letter in asciitxt:
      if not chr(letter).isalpha():
        ciphertext += chr(letter)
      elif not chr(letter+key).isalpha() and key>0:
        ciphertext += chr(key+letter-26)
      elif not chr(letter+key).isalpha() and key<0:
        ciphertext += chr(key+letter+26)
      else:
        ciphertext += chr(letter+key)
    return ciphertext

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext,-key)

def statistical_attack(ciphertext):
    unigramFreqs = [0.080, 0.015, 0.030, 0.040, 0.130, 0.020, 0.015, 0.060,
            0.065, 0.005, 0.005, 0.035, 0.030, 0.070, 0.080, 0.020, 0.002, 0.065,
            0.060, 0.090, 0.030, 0.010, 0.015, 0.005, 0.020, 0.002] 
    expectedFrequency = {}
    chiSquaredResults = []
    for letter in string.ascii_lowercase:
      expectedFrequency[letter] = unigramFreqs[string.ascii_lowercase.index(letter)]
    expected = list(expectedFrequency.values())
    for testKey in range(26):
      text = caesar_encrypt(ciphertext,testKey)
      observedFrequency = getFrequency(text)
      chiSquaredResults.append(stats.chisquare(f_obs=list(observedFrequency.values()), f_exp=expected).pvalue)
    key = 26 - chiSquaredResults.index(max(chiSquaredResults))
    return key, plaintext

def getFrequency(ciphertext):
  length = 0 
  observedFrequency = {}
  observedFrequencySorted = {}
  for char in ciphertext:
      if char.isalpha():
        length += 1
        if char not in observedFrequency:
          observedFrequency[char] = 1
        else:
          observedFrequency[char] += 1
  for letter in string.ascii_lowercase:
      if not letter in observedFrequency:
        observedFrequency[letter] = 0
  for key, value in sorted(observedFrequency.items()):
      observedFrequencySorted[key] = value/length
  return observedFrequencySorted

if __name__ == "__main__":
    plaintext = open('tufts_fight_song.txt', 'r', encoding="utf-8")
    text = plaintext.read()
    plaintext.close()

    print("Before encryption:")
    print(text)

    cc = caesar_encrypt(text, 2)
    print("\n\nAfter encryption:")
    print(cc)

    pt = caesar_decrypt(cc, 2)
    print("\n\nAfter decryption:")
    print(pt)
    
    key, pt = statistical_attack(cc)
    print("\n\nThe key was {}!!!".format(key))
