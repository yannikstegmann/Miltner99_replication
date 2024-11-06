The files were programmed with Presentation 21.1 - I could not test it with other versions.

Setup:
1. Set up the pain threshold procedure
	
	- Adjust monitors, response keys (we need Space and S) and ports (we need the US stimulator port) as needed
	- See screenshots in /Settings for the parameters I used. 


2. Set up the main experiment (/experiment code)

	- In Settings: Adjust monitors, response keys (we need Space, Arrow right, Arrow right (up), Arrow left, Arrow left (up) and G) and ports (we need EEG and stimulator port - can also be the same) as needed
	- See screenshots in /Settings for the parameters I used. 
	- In the Experiment Code: Enter your monitor information (see Screenshot "Monitor Settings (Main)") and check that the right ports are connected (see Screenshot Port Settings 2 (Main)")
	
Run the experiment: 
1. Run the pain threshold procedure
	- Click on the .exp file 
	- No need to enter a participant number (nothing will be saved)
 	- You will need the additional pain threshold document for registering the ratings
	- Make sure that the pain intensity starts at 0 ;)
	- Press "Space" once to get to the rating scale and show it to the participant
	- Deliver infinite shocks with pressing "S"
	- Stop with "Escape"
2. Run the main experiment
	- Click on the Miltner1999.exp file 
	- Enter a participant number (First three letters of your lab and two digits for the number, e.g. Wue_01)
	- For each participant you then need to enter the CS assignmet. 
		1: Square = CS+, Diamond= CS-
		2: Diamond = CS+, Square = CS-
	- Participants can read the instructions with pressing "Space"
	- When participants have to report to the experimenter, you have to press "g" to continue the study (To prevent that participants skip everything or start the trials earlier than recording). 
	- The rest is automatic
	- The CS order will be saved in the log file AND in an additional trigger file
	- The ratings will be saved in "logs/Ratings.csv"