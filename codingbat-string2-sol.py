## Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
  code_cnt=0
  for i in range(len(str)-3):
    if str[i:i+4].startswith("co") and str[i:i+4].endswith("e"):
      code_cnt+=1
  return code_cnt
