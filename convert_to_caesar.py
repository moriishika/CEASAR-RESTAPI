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


    








