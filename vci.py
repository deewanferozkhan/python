ch=str(input())
vowel=('a','e','i','o','u')
if(ch>='a' and ch<'z' or ch>='A' and ch<='Z'):
  if ch in vowel:
    print("vowel")
  else :
    print("consonant")
else:
  print("invalid")
