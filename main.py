#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

caesar_form = """
<!DOCTYPE html>
<html>
<head>
    <title> Caesar Encryption</title>
</head>
<body>

    <h1 style="text-align: center"> Caesar Encryption </h1>


<form> Enter a message here: <br>

    <input name="text"> </br>

    <br>
    Encrypt your text by...numeral:
    </br>
    <input name="rot"> <br>

    <input type=submit> </br>

</form>

</body>
</html>
"""






class Caesar_Form(webapp2.RequestHandler):
    """Writes the caesar_form above"""

    def get(self):
        self.response.write(caesar_form)

class Caesar_Message(webapp2.RequestHandler):
    """Receives user input and passes into the caesar encryption functions"""

    def get(self):

        self.response.get(text, rot)
        return text, rot


    ####### Start of three functions that implements Caesar Encryption #######

    def alphabet_position(letter):

        '''Returns 0 - 26 for a character in the alphabet.'''
        for i in letter:    # for loop to minus alpha to correct arbitrary return value

            if ord(i) >= 97 and ord(i) <= 122:

                i = ord(i) - 97

                return i

            else:

                i = ord(i) - 65

                return i


    def rotate_character(letter, rot):

        '''Returns message as garbled. Uses rotation input.
        Case sensitive. Leaves punctuation as is.'''


        rot = int(rot)

        encryptedMessage = ""

        for x in letter:


            if ord(x) >= 97 and ord(x) <= 122:

                newChar = chr((alphabet_position(x) + rot) % 26 + 97)
                encryptedMessage = encryptedMessage + newChar


            elif ord(x) >= 65 and ord(x) <= 90:

                newChar = chr((alphabet_position(x) + rot) % 26 + 65)
                encryptedMessage = encryptedMessage + newChar


            else:

                newChar = x
                encryptedMessage = encryptedMessage + newChar

        return encryptedMessage


    def encrypt(text, rot):

        '''Returns message as garbled. Uses rotation input.
        Case sensitive. Leaves punctuation as is.'''

        rot = int(rot)

        encryptedMessage = ""

        for x in text:


            if ord(x) >= 97 and ord(x) <= 122:

                newChar = chr((alphabet_position(x) + rot) % 26 + 97)
                encryptedMessage = encryptedMessage + newChar


            elif ord(x) >= 65 and ord(x) <= 90:

                newChar = chr((alphabet_position(x) + rot) % 26 + 65)
                encryptedMessage = encryptedMessage + newChar


            else:

                newChar = x
                encryptedMessage = encryptedMessage + newChar

        return encryptedMessage

    response = ""<p>encryptedMessage</p>""

    Caesar_Output = self.write.response(/Caesar_Message)


app = webapp2.WSGIApplication([
    ('/', Caesar_Form),
    ('/', Caesar_Message)

], debug=True)
