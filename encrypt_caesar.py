from convert_to_caesar import convert_to_Caesar
import re

# needed values will be the alphabets and the shift value
# the alphabets has to be converted to uppercase without any unique character and numbers
# take two inputs: shift number and the text
# if one of the value is empty then give an error message such as  "Cannot be emptied"
# if two of the values are available
# check the value of shift number - only number can be inserted
# if it is not a number - give an error message such as  "only number can be inserted"
# if the number is more than 26 or lesser than -26 -give an error
# message such as "The limit is 26 or -26"
# if the number is not integer than prompt - only able to receives an integer number
# or number can be rounded to floor number
# other unexpected error should be prompt a message "Unexpected input - please input                 integer number"
# check the value of the text with conver to caesar function
# if the fucntion gives an error message - display the error message given by the function
# create a list of uppercased alphabets
# create a list of uppercased alphabets that shifted based on the shift number
# duplicate list and remove the elements as many as the shift number from the     very last
# duplicate another and keep the elements as many as the shift number from        the very last
# concate both of duplications to be shifted list
# iterate every letter of the converted string from convert to caesar function
# while iterating the converted text iterate through shifted list
# get the position of the letter based on the alphabets list
# concate the empty string with the letter from the ordered alphabets list        that based on shiftedList letter position
# display the result

# shift value
# use alphabets or unique characters
# input float number
# input number with double dot
# input more than the limit
# input empty value
# Number has to be converted to characters

# alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# def encrypt_caesar(shiftNumber, text):
#   if shiftNumber == 0:
#     return "Unable to receive 0"
#   elif isinstance(shiftNumber, int) != True:
#     return "Only number can be received"
#   elif shiftNumber < -26 or shiftNumber > 26:
#     return "The limit shift is -26 or 26"

#   result = ""
#   convertedText = convert_to_Caesar(text)
#   shiftedList = alphabets[-shiftNumber:] + alphabets[:-shiftNumber]
#   for letter in convertedText:
#     for position, shiftedLetter in enumerate(shiftedList):
#       if letter == shiftedLetter:
#         result+= alphabets[position]

#   return result



def encrypt_caesar(shiftNumber, text):
  """
   Encrypt text based on caesar cypher algorithm

   Key arguments:
   
   shiftNumber -- a positive or negative integer between 1 to 26 -- Integer
   
   text -- A text without unique characters and number -- String

   Return value : encrypted text (String)
  """
  def getIndex(a_list, value):
      try:
          return a_list.index(value)
      except ValueError:
          return None
        
  alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
  ]

  numberWords = [
    "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT",
    "NINE"
  ]

  if shiftNumber == 0:
    return "Unable to receive 0"
  elif isinstance(shiftNumber, int) != True:
    return "Only number can be received"
  elif shiftNumber < -26 or shiftNumber > 26:
    return "The limit shift is -26 or 26"

  result = ""
  convertedText = text
  shiftedList = alphabets[-shiftNumber:] + alphabets[:-shiftNumber]

  if shiftNumber < 0:
    convertedText = convertedText.replace("XYX", ".")
    convertedText = [x for x in re.split("(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|ZERO)", convertedText) if x]
    
  
  for index, letter in enumerate(convertedText):
    if shiftNumber < 0:
      if(letter == "."):
        result+="."
      elif(getIndex(numberWords, letter) != None):
        result+=letter
      else:
        for indexDecrypt, letterDecrypt in enumerate(letter):
          if letterDecrypt == ".":
            result+="."
          for position, shiftedLetter in enumerate(shiftedList):
            if letterDecrypt == shiftedLetter:
              result += alphabets[position]
    else:
      if ord(letter) >= 48 and ord(letter) <= 57:
        result+=(numberWords[int(letter)])
              
      if  letter == ".":
        result+="XYX"
        
      for position, shiftedLetter in enumerate(shiftedList):
        if letter == shiftedLetter:
          result += alphabets[position]

  print(result)
  return [result]
