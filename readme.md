OTP - a one time pad generator and message en-/decrypter

IDEA:
this program was inspired by the use of numberstations and one time pads by intelligence-sevices.
one time pads (key) provide a safe way of sending encrypted messages. the transmitted message
is a string of numbers (or frequencies or anything you can imagine) that only the owner of the key 
is able to decrypt. the use of one time pads provide an unhackable way of one-directional 
transmitting of encrypted messages as long as the key is only known by the receiver and 
the sender, since every key is only used once (one time).

i tried to recreate this procedure with a program.

STRUCTURE
the program is devided into two sections: encryting and decrypting.

otp
	|-otp_encrypter_ui.py
		|-otp_encrypter.py
			|-filegen.py
	|-otp_decrypter_ui.py
		|-otp_decrypter.py

SYSTEM-REQUIREMENTS:
the code is written in the python programming language. to run this program from an IDE or from console 
an interpreter for python 3.x is needed. the program was written using python 3.11 and not tested against
older versions. given the simplicity of the program there should be no issues with older python 3.x-versions.

	PyQt5 needs to be installed to display the program

	pip install pyqt5

if you use linux, you can copy 'otp_encoder_and_decoder' from the 'build'-directory and
run the executable

from a hardwareperspective: the rotten potato you forgot in your kitchen drawer should be enough

RUN THE PROGRAM:
the following instructions are true wether you start the program from an IDE or the executable

you can access the encrypter and decrypter by clicking on the tab or switch between the tabs using
ctrl+tab

to generate a key and an encrypted message use 'encrypter"
- type your message in the lineedit and press return or click on the 'encode'-button
- a message will apear on the screen, telling you where on your system the key is saved
	- the key will be overwritten, when a new message is encrypted
- the encrypted message will be shown below
- copy the encrypted message by clicking on the 'copy to clipboard'-button
	
# WARNING #
the message will only be available to the clipboard while 'otp_encoder_and_decoder' is running
at this point i'm not shure if this is a bug or a feature

to decrypt an encrypted message use 'decrypter'
- find the key in your system and drag&drop it to the designated area
- paste the message to the lineedit and press return or click the 'decode'-button
- if key and message match, the decoded message will be shown below

# WARNING #
don't send key and message at the same time! although this program is meant to be a prove of concept,
as long as the key stays a secret between you and the receiver or vice versa it provides a safe
way of transmitting information. advanced security-features for transmitting key and message might
be added later but for now it is not recommended to send both at the same time.

OLDER VERSIONS
older versions with the same functionality can be found in the branches
OLD_V1
OLD_V2