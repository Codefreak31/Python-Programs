#Now we need to open the pycharm terminal and install pywhatkit in it.
install:
  pip install pywhatkit

import pywhatkit
   #Now we need to make the use of pywhatkit and send the message:
   pywhatkit.sendwhatmsg(“phone-number”, “The message”, hours, minutes)

#We need to enter the phone number with the country code or else the compiler will pop error.

#Now the output and full code is:


#Full Code

import pywhatkit

pywhatkit.sendwhatmsg("+xyz", "This is prequelcoding.in", 13, 49)
