# define a function called convert_to_Caesar
#   The function has one argument called input
#   input only accept string
#   iterate each letter from the input
#   check the ascii value
#       if the ascii value is bigger or equal to 065 and lesser or equal to 090 
#     do nothing
# if the ascii value is bigger or equal to 097 and lesser or equal to 122
#   convert to uppercase
# if the letter is dot (.)
#   convert it to X
# other than that
#   dont concate the character

# return the string


# TEST

# 1. full number - 876623982382378248 - nothing
# 2. other data type - 123838138 - prompt the error message
# 3. Full unique charachter - !@#$%^&*()_?<":}{ - nothing"
# 4. full small character - "aku suka banget kamu yang cantikkkk"
# 5. full uppercase - "AKU SUKA BANGET KAMU YANG CANTIKKKKK"
# 6. mixed of small, upperr and unique - "4kU SuK4 B4nG3T s4M4 K4mU!@#$%^&*()_+{{}|." - kusukbngtsmkmux
# 7. mixed of number and unique - 1234567890!@#$%^&*()_+{{}|:"M<>?/`"}
# 8. mixed of small and upper - AkUSuKaKaMU

# def convert_to_Caesar(input):
#   result = ""
#   if isinstance(input, str) != True:
#       return "Bro, string only ;-;"
#   for letter in input:
#     if ord(letter) >= 65 and ord(letter) <= 90:
#       result += letter
#     elif ord(letter) >= 97 and ord(letter) <= 122:
#       result += letter.upper()
#     elif letter == ".":
#       result+="X"
#   return result

def convert_to_Caesar(input):
  """
    Convert text that suitable for caesar encryption

    Keyword arguments:
    
    input -- a text -- String

    Return value : converted text (String)
  """
  
  result = ""
  
  if isinstance(input, str) != True:
    return "Bro, string only ;-;"
  if input == "":
    return "Please insert some text"

  for index, letter in enumerate(input):
    if letter == ".":
      result+=letter
    elif ord(letter) >= 48 and ord(letter) <=57:
      result+=letter
    elif ord(letter) >= 65 and ord(letter) <= 90:
      result+=letter
    elif ord(letter) >= 97 and ord(letter) <= 122:
      result+=letter.upper()
  return result

  
# print(convert_to_Caesar("876623982382378248"))
# print(convert_to_Caesar(87662398238237824))
# print(convert_to_Caesar("!@#$%^&*()_?<\":}{"))
# print(convert_to_Caesar("aku suka banget kamu yang cantikkkk"))
# print(convert_to_Caesar("AKU SUKA BANGET KAMU YANG CANTIKKKKK"))
# print(convert_to_Caesar("4kU SuK4 B4nG3T s4M4 K4mU!@#$%^&*()_+{{}|."))
# print(convert_to_Caesar("1234567890!@#$%^&*()_+{{}|:\"M<>?/`\"}"))
# print(convert_to_Caesar("AkUSuKaKaMU"))


    








