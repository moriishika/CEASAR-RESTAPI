from convert_to_caesar import convert_to_Caesar
import re

def encrypt_caesar(shiftNumber, text, method):
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
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    numberWords = [
        "ZERO",
        "ONE",
        "TWO",
        "THREE",
        "FOUR",
        "FIVE",
        "SIX",
        "SEVEN",
        "EIGHT",
        "NINE",
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

    if method == "false":
        convertedText = convertedText.replace("XYX", ".")
        convertedText = [
            x
            for x in re.split(
                "(ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|ZERO)", convertedText
            )
            if x
        ]

    for index, letter in enumerate(convertedText):
        if method == "false":
            if letter == ".":
                result += "."
            elif getIndex(numberWords, letter) != None:
                result += letter
            else:
                for indexDecrypt, letterDecrypt in enumerate(letter):
                    if letterDecrypt == ".":
                        result += "."
                    for position, shiftedLetter in enumerate(shiftedList):
                        if letterDecrypt == shiftedLetter:
                            result += alphabets[position]
        elif method == "true":
            if ord(letter) >= 48 and ord(letter) <= 57:
                result += numberWords[int(letter)]

            if letter == ".":
                result += "XYX"

            for position, shiftedLetter in enumerate(shiftedList):
                if letter == shiftedLetter:
                    result += alphabets[position]

    return [result]


