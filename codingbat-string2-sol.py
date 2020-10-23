## Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
## count_code('aaacodebbb') → 1
>>>>>>> 9b0479d04dd9a6aa1616ec85c519344d6f211644
def count_code(str):
  code_cnt=0
  for i in range(len(str)-3):
    if str[i:i+4].startswith("co") and str[i:i+4].endswith("e"):
      code_cnt+=1
  return code_cnt


#Given a string, return a string where for every char in the original, there are two chars.
#double_char('The') → 'TThhee'
def double_char(str):
  str1=''
  for char in str:
    str1+=char*2
  return str1

#Return the number of times that the string "hi" appears anywhere in the given string.
#count_hi('abc hi ho') → 1
#count_hi('ABChi hi') → 2

def count_hi(str):
  hi_cnt=0
  for i in range(len(str)-1):
    if str[i:i+2]=='hi':
      hi_cnt+=1
  return hi_cnt

##Return True if the string "cat" and "dog" appear the same number of times in the given string.
##cat_dog('catdog') → True
##cat_dog('catcat') → False

def cat_dog(str):
  cat_cnt=0
  dog_cnt=0
  for i in range(len(str)-2):
    if str[i:i+3]=='cat':
      cat_cnt+=1
    if str[i:i+3]=='dog':
      dog_cnt+=1
  return (cat_cnt==dog_cnt)

#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
##count_code('aaacodebbb') → 1
##count_code('codexxcode') → 2

def count_code(str):
  code_cnt=0
  for i in range(len(str)-3):
    if str[i:i+4].startswith('co') and str[i:i+4].endswith('e'):
      code_cnt+=1
  return code_cnt

##Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
#end_other('Hiabc', 'abc') → True
#end_other('AbC', 'HiaBc') → True

def end_other(a, b):
  a=a.lower()
  b=b.lower()
  
  return (a.endswith(b) or b.endswith(a))


# Return True if the given string contains an appearance of "xyz" where the 
# xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" 
# does not.

#xyz_there('abcxyz') → True
#xyz_there('abc.xyz') → False
def xyz_there(str):
    if str[:3] == "xyz":
        return True
                    
    for i in range(1, len(str) - 2):
        if str[i-1] != "." and str[i:i+3] == "xyz":
            return True
                                      
    return False


