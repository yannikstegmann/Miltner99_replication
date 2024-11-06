This is the PsychoPy-Code for the Miltner 1999 Replication Study.
The Study was programmed with PsychoPy version 2024.1.5.
I recommend to download this version (or download a newer version and set the "use version in the settings tab to 2024.1.5").
Anyways make sure the paradigm runs smoothly and all triggers are presented as they should. Let me know if there are any issues.

Setup:

Parallel-Ports:

1. Make sure that the port(s) needed are listed in PsychoPys General Preferences/Hardware. (see point 4 at  https://psychopy.org/hardware/parallelPortInstr.html)
2. Go to the Settings/Basic Tab and enter your physical port adress of your EEG and US parallel port. (Both ports can use the same adress if you send US and EEG triggers over the same port)


Monitor specification:

1. Go to the screen tab and create a "EEGMonitor", which has the exact measure of pixels, screen width, and viewing distance. As the stimulus size is adapted to these values. (see Screenshot Monitor Setup 1)
2. At Settings/Monitor make sure to select the eegMonitor type and to chose the correct monitor. (see Screenshot Monitor Setup 2)

Run the experiment: 

1. Run the pain threshold procedure
	- No need to enter a participant number (nothing will be saved)
 	- You will need the additional pain threshold document for registering the ratings
	- Make sure that the pain intensity starts at 0 ;)
	- Press "Space" once to get to the rating scale and show it to the participant
	- Deliver infinite shocks with pressing "S"
	- Stop with "Escape"

2. Run the main experiment
	- Enter a participant number (First three letters of your lab and two digits for the number, e.g. Wue_01)
	- For each participant you then need to enter the CS assignmet at Order. 
		1: Square = CS+, Diamond= CS-
		2: Diamond = CS+, Square = CS-
	- Participants can read the instructions with pressing "Space"
	- Participants can control the rating scale with the arrow keys and the "Enter" key
	- When participants have to report to the experimenter, you have to press "g" to continue the study (To prevent that participants skip everything or start the trials earlier than recording). 
	- The rest is automatic
