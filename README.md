# Renault Radio Codes Calculator
Python script to calculate the renault radio code from the precode
If your radio lost power (e.g. after a battery failure) the radio locks itself up and needs a code to be used again. Thia is meant to make the life of radio thiefs harder. 
One can unlock the radio by going to a Renault dealership and paying a fee to get the radio unlocked. Since (at least for me) the fee was higher than to buy a new radio I spent some time to write this little script which calculates the codes

## How to get the pre-code
Some radios allow to get the code by simultaniouslly pressing and holding the buttons 1&6 or 1&5 for 5 seconds.

If that doesn't work you obtain the pre-code by unmounting the radio:
1. Insert something into the four holes around the radio (e.g screw drivers, shashlik scewers) to unlock the radio
2. Pull out the radio
3. Locate the sticker with the serial number (most likely on the side of the radio)
4. The pre-code is the last four characters of the serial nummber it should start with a capital letter followed by 3 numbers (e.g. A123) 

## Hoe to run the script
Simple:
```
$ python renault.py
```
Enter the pre-code and it will give you the code
