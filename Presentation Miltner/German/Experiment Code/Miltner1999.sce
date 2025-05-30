# Please read:
# This is the experiment code for the Miltner 1999 replication
# Before running the experiment, several things need to be adjusted to the individual lab:
# 
# Parallel ports:
# 1. Make sure that the correct ports are selected at "Settings/Port -> Output Port". Default pulse width should be set to 2 ms. 
#	Please test your ports to check that triggers are sent to the EEG and stimulator. See Screenshot "Port Settings"
# 2. At line 293 and 294 at #Ports: Enter the number of the ports according to how they are set in the settings tab. See Screenshot "Port Settings 2"
#	The US and EEG port can have the same number if the same port is used for sending EEG triggers and triggers to the stimulator.
#
# Monitor specifications:
# 1. In Settings/Video choose the correct monitor.
# 2. At line 41 - 43 enter the distance from participant to monitor at viewing_distance in milimeters, the monitor_width in pixels, and the monitor_size_width in milimeters. See Screenshot "Monitor Settings"
#	Based on these values the stimulus size will be calculated to span exactly 8° of visual angle
# 
# Response buttons:
# The experiment needs 6 Response Buttons to work properly. 
# 1. Go to "Settings/Response" and choose the "Miltner1999.sce" Scenario. Make sure that the following buttons are listed at "Active Buttons" in the correct order:
# 	SPACE, RIGHT, RIGHT (up), LEFT, LEFT (up), G

###################
###### Header __________________________________________________________________________________________________________________________________________________________
###################

scenario_type = trials; 
default_font_size = 18;
default_font = "Arial"; 
default_trial_type = fixed; 
default_background_color =128,128,128;
write_codes = true;
response_port_output = false;
active_buttons = 6;        
button_codes =1,2,3,4,5,6;  #1 = Space, 2 = right, 3 = right (up), 4 = left, 5 = left (up), 6 = g
response_matching = simple_matching;
begin;

###################
###### User Input of CS Size __________________________________________________________________________________________________________________________________________
################

$viewing_distance = 900; #milimeter
$monitor_width = 2560; #pixels
$monitor_size_width = 600; #milimeter

$visual_angle = 0.13962634; #DO NOT CHANGE visual angle of the final stimulus Radians(8°) = 0.13962634. 

$stim_size = 'tan($visual_angle)*$viewing_distance*$monitor_width/$monitor_size_width';

###################
###### User Input of CS Assignment __________________________________________________________________________________________________________________________________________
###################
  

picture {
   text {
      font_size = 18;
      caption = "Gib die CS Zuordnung ein ('1' oder '2') und bestätige mit <ENTER>.






			Falls ein Fehler auftritt, starte das Programm wieder!";};
   x = 0; y = 0;
   text {
      font_size = 18;
      caption = " ";
   } response_text;
   x = 0; y = 0;
}RF_input;

###################
###### Fixation cross and ITI __________________________________________________________________________________________________________________________________________
###################
  
picture { 
	text {caption = "+";font_size = 18; background_color = 128, 128, 128; transparent_color = 128, 128, 128;}fixk; 
	x = 0; y = 0; 
}fix;   

trial {
   stimulus_event {picture fix;
      }iti_event;
}iti_trial;

###################
###### CS presentation _________________________________________________________________________________________________________________________________________________
###################


plane {color = 0, 0, 0; height = $stim_size; width = $stim_size; description = "CS_p";}cs_pr; #square
   
array{
	bitmap {filename = "cs1.png"; height = 300; width = 300;  alpha=-1;  description = "CS_p";}cs_pr_rating; #square
	bitmap {filename = "cs2.png"; height = 425; width = 425;  alpha=-1;   description = "CS_m";}cs_mg_rating; #diamond
}cs_rating_array_1;     


array{
	bitmap {filename = "cs2.png"; height = 425; width = 425; alpha=-1;  description = "CS_p";}cs_pg_rating; #diamond
	bitmap {filename = "cs1.png"; height = 300; width = 300; alpha=-1; description = "CS_m";}cs_mr_rating; #square
}cs_rating_array_2;     

trial {
	trial_duration = 3000; #3s CS presentations
	trial_type = fixed;
	stimulus_event {
		picture {
			plane cs_pr; x = 0; y = 0; z = 0;
			#text fixk;x = 0; y = 0; 
		} cs_pic;
		#set event_code in PCL
		#set port_code in PCL
	} cs_event;
} cs_trial;

###################
###### US presentation ________________________________________________________________________________________________________________________________________________
###################

trial {
	stimulus_event {
		nothing {};
		time = 0;
	}shock_on;
	stimulus_event {
		nothing {};
		delta_time = 4;#2
		duration = 2;#2
	}shock_off;
}pulse_US;


###################
###### Instruction trials ____________________________________________________________________________________________________________________________________________
###################

trial { # Container for instructions 
   trial_type = specific_response;
   trial_duration = forever;
   terminator_button = 1; #Continue with "space" (1 = Space)
	stimulus_event{  
		picture {
			text { caption = " "; }text1; x = 0; y = 0;    # Fill Text in PCL                  
		}txtpic1; 
   }txtevent1;
} instruction_trial;       

trial { 
   trial_type = specific_response;
   trial_duration = forever;
   terminator_button = 6; #Continue with "g" (6 = g) Needed in case participants should not be able to continue on their own.
	stimulus_event{  
		picture {
			text { caption = " "; }text2; x = 0; y = 0;  # Fill Text in PCL             
		}txtpic2; 
   }txtevent2;
}instruction_trial2;       

###################
###### Rating trials ____________________________________________________________________________________________________________________________________________
###################

text{caption=" ";font_color = 255,255,255; transparent_color = 128,128,128; }empty_text;

text{ caption ="Die Skala reicht von negativ bis positiv.
Beim ersten Extremwert wirken die Stimuli sehr negativ auf Sie, beim anderen sehr positiv.
Wenn die Stimuli keine Wirkung auf Sie haben, also weder positiv noch negativ, 
bewegen Sie den Kreis bitte auf die 0 in der Mitte.

Nutzen Sie die Pfeiltasten, um den roten Kreis auf der entsprechenden Zahl platzieren.
Drücken Sie die Leeraste um ihre Auswahl zu bestätigen und um mit dem Experiment fortzufahren."; font_size = 20; font_color = 255,255,255; transparent_color = 128,128,128; }practice_text;

text { caption ="Wie negativ/positiv wirkt dieser Stimulus auf Sie?"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating1;
text { caption ="-4"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating2;
text { caption ="-3"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating3;
text { caption ="-2"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating4;
text { caption ="-1"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating5;
text { caption ="0"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating6;
text { caption ="+1"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating7;
text { caption ="+2"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating8;
text { caption ="+3"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating9;
text { caption ="+4"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating10;
text { caption ="___"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating11;
text { caption ="sehr negativ"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating12;
text { caption ="neutral"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating13;
text { caption ="sehr positiv"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }tv_rating14;

trial {   
   stimulus_event {
picture { 
    # the circle
    polygon_graphic { sides = 20; line_color = 255,0,0; line_width = 2; radius = 24; join_type = join_circle;}circle1;
    x = 0; y = -380; on_top = true;
    # text
   text tv_rating1; x = 0; y = -300; on_top = true;
	text tv_rating2; x = -400; y = -380; on_top = true;
	text tv_rating3; x = -300; y = -380; on_top = true;
	text tv_rating4; x = -200; y = -380; on_top = true;
	text tv_rating5; x = -100; y = -380; on_top = true;
	text tv_rating6; x = 0; y = -380; on_top = true;
	text tv_rating7; x = 100; y = -380; on_top = true;
	text tv_rating8; x = 200; y = -380; on_top = true;
	text tv_rating9; x = 300; y = -380; on_top = true;
	text tv_rating10; x = 400; y = -380; on_top = true;
	
	text tv_rating11; x = -350; y = -365; on_top = true;
	text tv_rating11; x = -250; y = -365; on_top = true;
	text tv_rating11; x = -150; y = -365; on_top = true;
	text tv_rating11; x = -50; y = -365; on_top = true;
	text tv_rating11; x = 50; y = -365; on_top = true;
	text tv_rating11; x = 150; y = -365; on_top = true;
	text tv_rating11; x = 250; y = -365; on_top = true;
	text tv_rating11; x = 350; y = -365; on_top = true;
	
	text tv_rating12; x = -400; y = -420; on_top = true;
	text tv_rating13; x = 0; y = -420; on_top = true;
	text tv_rating14; x = 400; y = -420; on_top = true;

	bitmap cs_pr_rating; x = 0; y = 0; on_top = false;
} lines;                                   

time = 500;
duration = response;} ratingEvent;
} ratingTrial;

## Pain intensity

text{ caption ="Außerdem sollen Sie die elektrischen Reizebewerten, die Ihnen während des Experiments präsentiert werden. 

Auf der ersten Skala bewerten Sie, wie schmerzhaft/intensiv Sie die elektrischen Reize wahrgenommen haben. 
Die Skala reicht von 'gar nicht schmerzhaft' bis 'unerträglich schmerzhaft'.

Nutzen Sie die Pfeiltasten, um den roten Kreis auf der entsprechenden Zahl platzieren.
Drücken Sie die Leeraste um ihre Auswahl zu bestätigen und um mit dem Experiment fortzufahren."; font_size = 20; font_color = 255,255,255; transparent_color = 128,128,128; }practice_text2;

text { caption ="Wie schmerzhaft/intensiv haben Sie den letzten elektrischen Reiz wahrgenommen?"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating1;
text { caption ="0"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating2;
text { caption ="1"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating3;
text { caption ="2"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating4;
text { caption ="3"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating5;
text { caption ="4"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating6;
text { caption ="5"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating7;
text { caption ="6"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating8;
text { caption ="7"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating9;
text { caption ="8"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating10;
text { caption ="9"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating15;
text { caption ="10"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating16;
text { caption ="___"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating11;
text { caption ="gar nicht schmerzhaft"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating12;
#text { caption ="neutral"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating13;
text { caption ="unerträglich schmerzhaft"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pi_rating14;

trial {   
   stimulus_event {
picture { 
    # the circle
    polygon_graphic circle1;
    x = 0; y = -380; on_top = true;
    # text
   text pi_rating1; x = 0; y = -300; on_top = true;
	text pi_rating2; x = -500; y = -380; on_top = true;
	text pi_rating3; x = -400; y = -380; on_top = true;
	text pi_rating4; x = -300; y = -380; on_top = true;
	text pi_rating5; x = -200; y = -380; on_top = true;
	text pi_rating6; x = -100; y = -380; on_top = true;
	text pi_rating7; x = 0; y = -380; on_top = true;
	text pi_rating8; x = 100; y = -380; on_top = true;
	text pi_rating9; x = 200; y = -380; on_top = true;
	text pi_rating10; x = 300; y = -380; on_top = true;
	text pi_rating15; x = 400; y = -380; on_top = true;
	text pi_rating16; x = 500; y = -380; on_top = true;
	
	text pi_rating11; x = -450; y = -365; on_top = true;
	text pi_rating11; x = -350; y = -365; on_top = true;
	text pi_rating11; x = -250; y = -365; on_top = true;
	text pi_rating11; x = -150; y = -365; on_top = true;
	text pi_rating11; x = -50; y = -365; on_top = true;
	text pi_rating11; x = 50; y = -365; on_top = true;
	text pi_rating11; x = 150; y = -365; on_top = true;
	text pi_rating11; x = 250; y = -365; on_top = true;
	text pi_rating11; x = 350; y = -365; on_top = true;
	text pi_rating11; x = 450; y = -365; on_top = true;
		
	text pi_rating12; x = -500; y = -420; on_top = true;
	#text pi_rating13; x = 0; y = -420; on_top = true;
	text pi_rating14; x = 500; y = -420; on_top = true;

	text empty_text; x = 0; y = 0; on_top = false;
} lines2;                                   

time = 500;
duration = response;} ratingEvent2;
} ratingTrial2;

# Pain unpleasantnes

text{ caption ="Auf der zweiten Skala sollen sie darüberhinaus bewerten wie unangenehm/störend Sie die elektrischen Reize wahrgenommen haben. 
Diese Skala reicht von 'gar nicht unangenehm' bis 'sehr unangenehm'.

Nutzen Sie die Pfeiltasten, um den roten Kreis auf der entsprechenden Zahl platzieren.
Drücken Sie die Leeraste um ihre Auswahl zu bestätigen und um mit dem Experiment fortzufahren."; font_size = 20; font_color = 255,255,255; transparent_color = 128,128,128; }practice_text3;

text { caption ="Wie unangenehm/störend haben Sie den letzten elektrischen Reiz wahrgenommen?"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating1;
text { caption ="0"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating2;
text { caption ="1"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating3;
text { caption ="2"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating4;
text { caption ="3"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating5;
text { caption ="4"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating6;
text { caption ="5"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating7;
text { caption ="6"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating8;
text { caption ="7"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating9;
text { caption ="8"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating10;
text { caption ="9"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating15;
text { caption ="10"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating16;
text { caption ="___"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating11;
text { caption ="gar nicht unangenehm"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating12;
#text { caption ="neutral"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating13;
text { caption ="sehr unangenehm"; font_size = 22; font_color = 255,255,255; transparent_color = 128,128,128; }pu_rating14;

trial {   
   stimulus_event {
picture { 
    # the circle
    polygon_graphic circle1;
    x = 0; y = -380; on_top = true;
    # text
   text pu_rating1; x = -0; y = -300; on_top = true;
	text pu_rating2; x = -500; y = -380; on_top = true;
	text pu_rating3; x = -400; y = -380; on_top = true;
	text pu_rating4; x = -300; y = -380; on_top = true;
	text pu_rating5; x = -200; y = -380; on_top = true;
	text pu_rating6; x = -100; y = -380; on_top = true;
	text pu_rating7; x = 0; y = -380; on_top = true;
	text pu_rating8; x = 100; y = -380; on_top = true;
	text pu_rating9; x = 200; y = -380; on_top = true;
	text pu_rating10; x = 300; y = -380; on_top = true;
	text pu_rating15; x = 400; y = -380; on_top = true;
	text pu_rating16; x = 500; y = -380; on_top = true;
	
	text pu_rating11; x = -450; y = -365; on_top = true;
	text pu_rating11; x = -350; y = -365; on_top = true;
	text pu_rating11; x = -250; y = -365; on_top = true;
	text pu_rating11; x = -150; y = -365; on_top = true;
	text pu_rating11; x = -50; y = -365; on_top = true;
	text pu_rating11; x = 50; y = -365; on_top = true;
	text pu_rating11; x = 150; y = -365; on_top = true;
	text pu_rating11; x = 250; y = -365; on_top = true;
	text pu_rating11; x = 350; y = -365; on_top = true;
	text pu_rating11; x = 450; y = -365; on_top = true;
	
	text pu_rating12; x = -500; y = -420; on_top = true;
	#text pu_rating13; x = 0; y = -420; on_top = true;
	text pu_rating14; x = 500; y = -420; on_top = true;

	text empty_text; x = 0; y = 0; on_top = false;
} lines3;                                   

time = 500;
duration = response;} ratingEvent3;
} ratingTrial3;




###################
###### PCL _______________________________________________________________________________________________________________________________________________________
###################

begin_pcl; 

###################
###### Set CS assignment _____________________________________________________________________________________________________________________________________________
###################

sub
   int get_response
begin
   system_keyboard.set_max_length( 1 );
   string assignment;
	int assignment_int;
   loop until false begin  
      response_text.set_caption( " " + assignment );
      response_text.redraw();
      RF_input.present();
      string letter = system_keyboard.get_input(); 
      if (system_keyboard.last_input_type() == keyboard_delimiter) then
         break
      end;
      assignment = assignment + letter;   
		assignment_int = int(assignment);
   end;
   return assignment_int
end;  

int assignment = get_response();
term.print("CS assignment: "+string(assignment)+"\n");				

int rotation_factor;
array <bitmap> cs_rating_array[2]; 

if (assignment != 1 && assignment != 2) then								# if wrong number, give error and abort
 exit( "Error: Wrong CS assignment, please restart experiment and enter only 1 or 2");
end;		
		
if (assignment == 1) then														# if 1: CS+ = square, CS- = diamond
	rotation_factor = 0;
	cs_rating_array = cs_rating_array_1;
elseif (assignment == 2) then													# if 2: CS- = square, CS+ = diamond
	rotation_factor = 45;
	cs_rating_array = cs_rating_array_2;
end; 

###################
###### Output Files _____________________________________________________________________________________________________________________________________________
###################

output_file outRating = new output_file;
logfile.set_filename(logfile.subject() + ".log"); # Standard presentation log files

string outputFile1=logfile.subject()+"_Trigger.dat"; # Saves a txt file including the order of the CS triggers per participant
output_file trigger1 = new output_file;

###################
###### Ports ____________________________________________________________________________________________________________________________________________________
###################

output_port port = output_port_manager.get_port( 1 ); # Adjust ports as needed. Here Port 1 is used for the digitimer
output_port port2 = output_port_manager.get_port( 2 ); # Port 2 is used for the EEG

###################
###### US ____________________________________________________________________________________________________________________________________________________
###################

sub shock begin
	term.print( "Shock\n" );
	loop int l1 = 1
	until l1 > 3
	begin			
		#shock_on.set_event_code("shock");
		shock_off.set_port_code(port_code_none);
		port.send_code(128);		
		pulse_US.present();				
		l1=l1+1
	end;
end;

###################
###### Write_Output _____________________________________________________________________________________________________________________________________________
###################

sub trigger_output(int marker_output)	begin #to write triggers into the _trigger.dat file
	trigger1.open_append(outputFile1);
   trigger1.print(string(marker_output));
   trigger1.print("\n");
	trigger1.close();
end;

###################
####### ITI _____________________________________________________________________________________________________________________________________________________
###################

sub iti begin
iti_event.set_duration ( random(3000,4000) ) ; #set ITI duration to 3-4s 
iti_trial.present () ;
end;

sub short_iti begin
iti_event.set_duration ( 500 ) ; #set ITI duration to 4s without jitter
iti_trial.present () ;
end;

###################
#######  Instruction trials _____________________________________________________________________________________________________________________________________
###################  

sub instr (string new_txt) # for text the participant can continue with pressing the space bar
 begin
 text1.set_formatted_text( true );
 text1.set_caption (new_txt);
 text1.redraw();
 instruction_trial.present ()
end;

sub instrvl (string new_txt)  # for text the experimentator can continue with pressing "g"
 begin
 text2.set_formatted_text( true );
 text2.set_caption (new_txt);
 text2.redraw();
 instruction_trial2.present ()
end;


###################
#######  Rating trials _____________________________________________________________________________________________________________________________________
###################  

string rating_description; # so we know later when the rating was collected

sub cs_rating begin
	cs_rating_array.shuffle(); # counterbalance square and diamond
	int rating_index = 1;
	loop until rating_index > cs_rating_array.count() begin # loop through both colors
		int valence;
		short_iti();
		loop
			int count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
			int x1 = 0;
			int x_inc = 100;
			int x_change = 0;	
			int confirm = response_manager.total_response_count( 1 );
			int confirm2 = confirm + 1;
			lines.set_part_x( 1, x1 ); 
			lines.set_part(23, cs_rating_array[rating_index]); 		# show the color
			lines.present();														# and the rating scale
		until
			response_manager.total_response_count( 1 ) == confirm2 	# continue when participant presses space
		begin	
			if (response_manager.last_response () == 4) then 
				x_change = -x_inc													# go left if participant presses left arrow
			elseif (response_manager.last_response () == 2) then
				x_change = x_inc;													# go right if participant presses right arrow
			end;
			if (response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 ) > count_up) then
				if (response_manager.last_response () == 3 || response_manager.last_response () == 5) then
					x1 = x1 + x_change;
					if x1 < - 400 then x1 = -400 
					elseif x1 > 400 then x1 = 400 end;
					lines.set_part_x( 1, x1 );
					lines.present(); 												# visually update the rating scale
					count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
				end;
			end;
		valence = x1/100;	      
		end;        
		outRating.open_append("Ratings.csv");								# open the table file for saving the ratings. Make sure it's closed before the experiment starts!
		outRating.print(logfile.subject());									# save subject ID
		outRating.print(";");
		outRating.print(rating_description);								# save when the rating was collectedd
		outRating.print(";");
		outRating.print(cs_rating_array[rating_index].description()); # save CS information
		outRating.print(";");
		outRating.print(valence);												# save valence rating
		outRating.print(";");
		outRating.print("\n");													# new line for each CS and participant
		outRating.close();
		rating_index = rating_index + 1;
	end; #endloop	
end; #endsub

sub us_rating begin
	
	int intensity;
	short_iti();
	loop
		int count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
		int x1 = -500;
		int x_inc = 100;
		int x_change = 0;	
		int confirm = response_manager.total_response_count( 1 );
		int confirm2 = confirm + 1;
			
		lines2.set_part_x( 1, x1 ); 
		lines2.set_part(26, empty_text); 								# show nothing
		lines2.present();														# and the rating scale
		until
			response_manager.total_response_count( 1 ) == confirm2 	# continue when participant presses space
		begin	
			if (response_manager.last_response () == 4) then 
				x_change = -x_inc													# go left if participant presses left arrow
			elseif (response_manager.last_response () == 2) then
				x_change = x_inc;													# go right if participant presses right arrow
			end;
			if (response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 ) > count_up) then
				if (response_manager.last_response () == 3 || response_manager.last_response () == 5) then
					x1 = x1 + x_change;
					if x1 < - 500 then x1 = -500 
					elseif x1 > 500 then x1 = 500 end;
					lines2.set_part_x( 1, x1 );
					lines2.present(); 												# visually update the rating scale
					count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
				end;
			end;
		intensity = (x1/100)+5;	             
	end;

	int unpleasantnes;
	short_iti();
	loop
		 int count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
		 int x1 = -500;
		 int x_inc = 100;
		 int x_change = 0;	
		 int confirm = response_manager.total_response_count( 1 );
		 int confirm2 = confirm + 1;
			
		lines3.set_part_x( 1, x1 ); 
		lines3.set_part(26, empty_text); 								# show nothing
		lines3.present();														# and the rating scale
		until
			response_manager.total_response_count( 1 ) == confirm2 	# continue when participant presses space
		begin	
			if (response_manager.last_response () == 4) then 
				x_change = -x_inc													# go left if participant presses left arrow
			elseif (response_manager.last_response () == 2) then
				x_change = x_inc;													# go right if participant presses right arrow
			end;
			if (response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 ) > count_up) then
				if (response_manager.last_response () == 3 || response_manager.last_response () == 5) then
					x1 = x1 + x_change;
					if x1 < - 500 then x1 = -500 
					elseif x1 > 500 then x1 = 500 end;
					lines3.set_part_x( 1, x1 );
					lines3.present(); 												# visually update the rating scale
					count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
				end;
			end;
		unpleasantnes = (x1/100)+5;	     
	end;

		outRating.open_append("Ratings.csv");								# open the table file for saving the ratings. Make sure it's closed before the experiment starts!
		outRating.print(logfile.subject());									# save subject ID
		outRating.print(";");
		outRating.print(rating_description);								# save when the rating was collectedd
		outRating.print(";");
		outRating.print("US_int"); # save US information
		outRating.print(";");
		outRating.print(intensity);											# save us intensity rating
		outRating.print(";");
		outRating.print("\n");													# new line for each CS and participant
		outRating.print(logfile.subject());									# save subject ID
		outRating.print(";");
		outRating.print(rating_description);								# save when the rating was collectedd
		outRating.print(";");
		outRating.print("US_unpl"); # save US information
		outRating.print(";");
		outRating.print(unpleasantnes);										# save us unpleasantnes rating
		outRating.print(";");
		outRating.print("\n");		
		
		outRating.close();
end; #endsub


###################
#######  Practice rating trials _________________________________________________________________________________________________________________________
###################  

sub practice_rating begin # Does the same as above without showing a color or saving anything


	loop
		 int count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
		 int x1 = 0;
		 int x_inc = 100;
		 int x_change = 0;	
		 int confirm = response_manager.total_response_count( 1 );
		 int confirm2 = confirm + 1;
		lines.set_part_x( 1, x1 ); 
		lines.set_part(23, practice_text);
		lines.present();		
	until
		response_manager.total_response_count( 1 ) == confirm2
	begin	
		if (response_manager.last_response () == 4) then
			x_change = -x_inc
		elseif (response_manager.last_response () == 2) then
			x_change = x_inc;
		end;
		if (response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 ) > count_up) then
			if (response_manager.last_response () == 3 || response_manager.last_response () == 5) then
				x1 = x1 + x_change;
				if x1 < - 400 then x1 = -400 
				elseif x1 > 400 then x1 = 400 end;
				lines.set_part_x( 1, x1 );
				lines.present();
				count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
			end;
		end;
	end;        

	loop
		int count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
		int x1 = -500;
		int x_inc = 100;
		int x_change = 0;	
		int confirm = response_manager.total_response_count( 1 );
		int confirm2 = confirm + 1;
		lines2.set_part_x( 1, x1 ); 
		lines2.set_part(26, practice_text2);
		lines2.present();		
	until
		response_manager.total_response_count( 1 ) == confirm2
	begin	
		if (response_manager.last_response () == 4) then
			x_change = -x_inc
		elseif (response_manager.last_response () == 2) then
			x_change = x_inc;
		end;
		if (response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 ) > count_up) then
			if (response_manager.last_response () == 3 || response_manager.last_response () == 5) then
				x1 = x1 + x_change;
				if x1 < - 500 then x1 = -500 
				elseif x1 > 500 then x1 = 500 end;
				lines2.set_part_x( 1, x1 );
				lines2.present();
				count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
			end;
		end;
	end;        
	
	loop
		int count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
		int x1 = -500;
		int x_inc = 100;
		int x_change = 0;	
		int confirm = response_manager.total_response_count( 1 );
		int confirm2 = confirm + 1;
		lines3.set_part_x( 1, x1 ); 
		lines3.set_part(26, practice_text3);
		lines3.present();		
	until
		response_manager.total_response_count( 1 ) == confirm2
	begin	
		if (response_manager.last_response () == 4) then
			x_change = -x_inc
		elseif (response_manager.last_response () == 2) then
			x_change = x_inc;
		end;
		if (response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 ) > count_up) then
			if (response_manager.last_response () == 3 || response_manager.last_response () == 5) then
				x1 = x1 + x_change;
				if x1 < - 500 then x1 = -500 
				elseif x1 > 500 then x1 = 500 end;
				lines3.set_part_x( 1, x1 );
				lines3.present();
				count_up = response_manager.total_response_count( 3 ) + response_manager.total_response_count( 5 );
			end;
		end;
	end;        
	
end; #endsub





###################
####### CS arrays ______________________________________________________________________________________________________________________________________________
###################

array <int> cue_conditions[120] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
												1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
												1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2}; # 60x 1 = CS+, 60x 2 = CS-

array <int> ext_conditions[80] = {1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,
												1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2}; # 40x 1 = CS+, 40x 2 = CS-

###################
####### Main trials: Cue acquisition_____________________________________________________________________________________________________________________________
###################

int cue_index = 1; 																	# indexes trials
int csp_count = 1; 																	# counts CS+
int csm_count = 1; 																	# counts CS-
int iti_cue_count = 1; 																# counts ITIs

sub acquisition_phase begin 
	loop cue_index=1; until cue_index > cue_conditions.count() begin 	# run through all 120 elements in cue_conditions array
		iti_event.set_event_code("iti_" + string(iti_cue_count));		# write ITI count to log file
		iti();																			# present ITI
		iti_cue_count = iti_cue_count + 1;										# increment ITI count
		
		if (cue_conditions[cue_index] ==1) then 								# CS+ trials:
			port2.send_code (1); 													# EEG marker (1 = CS+ in Acq)
			trigger_output(1); 														# write to _trigger.dat file
			cs_event.set_event_code ("csp_"+string(csp_count)); 			# write CS+ count to log file
			term.print( "Acq: CS+ "+string(csp_count)+"\n");				# print CS+ count in console
			csp_count= csp_count+1;													# increment CS+ count	
			cs_pic.set_3dpart_rot(1,0,0,rotation_factor);					# set CS+ 
			cs_trial.present();														# present CS+
			shock ();																	# present US

		elseif (cue_conditions[cue_index] == 2) then 						# CS- trials:
			port2.send_code (2); 													# EEG marker (2 = CS- in Acq)
			trigger_output(2); 														# write to _trigger.dat file		
			cs_event.set_event_code ("csm_"+string(csm_count)); 			# write CS- count to log file
			term.print( "Acq: CS- "+string(csm_count)+"\n");				# print CS- count in console
			csm_count= csm_count+1;													# increment CS- count		
			cs_pic.set_3dpart_rot(1,0,0,rotation_factor-45);				# set CS- 
			cs_trial.present();														# present CS-
		end;	#end_conditions_if			
		
		if (cue_index == 60) then													# After 60 and 120 trials: 
			rating_description = "Acq_1";									
			cs_rating();																# Get Valence Ratings of CS+ and CS- 
			us_rating();
		elseif (cue_index == 120) then
			rating_description = "Acq_2";
			cs_rating();
			us_rating();
		end;
		cue_index = cue_index+1;													# increment cue_index
	end;	#endbigloop
end;	#endsub

###################
####### Main trials: Extinction phase___________________________________________________________________________________________________________________________
###################

sub extinction_phase begin 
	csp_count = 1;																		# counts CS+ in extinction
	csm_count = 1;																		# counts CS- in extinction
	loop cue_index=1; until cue_index > ext_conditions.count() begin  # run through all 80 elements in ext_conditions array 
		iti_event.set_event_code("iti_" + string(iti_cue_count));		# write ITI count to log file
		iti();																			# present ITI
		iti_cue_count = iti_cue_count + 1;										# increment ITI count
	
		if (ext_conditions[cue_index] ==1) then 								# CS+ trials:
			port2.send_code (3); 													# EEG marker (3 = CS+ in Ext)
			trigger_output(3); 														# write to _trigger.dat file
			cs_event.set_event_code ("csp_"+string(csp_count)); 			# write CS+ count to log file
			term.print( "Ext: CS+ "+string(csp_count)+"\n");				# print CS+ count in console
			csp_count= csp_count+1;													# increment CS+ count
			cs_pic.set_3dpart_rot(1,0,0,rotation_factor);					# set CS+ 
			cs_trial.present();														# present CS+ without US

		elseif (ext_conditions[cue_index] == 2) then 						# CS- trials:
			port2.send_code (4); 													# EEG marker (4 = CS- in Acq)
			trigger_output(4); 														# write to _trigger.dat file
			cs_event.set_event_code ("csm_"+string(csm_count)); 			# write CS- count to log file
			term.print( "Ext: CS- "+string(csm_count)+"\n");				# print CS- count in console
			csm_count= csm_count+1;													# increment CS- count
			cs_pic.set_3dpart_rot(1,0,0,rotation_factor-45);				# set CS- 
			cs_trial.present();														# present CS-
		end;	#end_conditions_if	
		
		if (cue_index == 40) then													# After 40 and 80 Trials of Extinction
			rating_description = "Ext_1";
			cs_rating();																# Get Valence Ratings of CS+ and CS- 
		elseif (cue_index == 80) then
			rating_description = "Ext_2";
			cs_rating();
		end;		
		cue_index = cue_index+1;													# increment cue_index
	end;	#endbigloop
end;	#endsub

###################
####### Main experiment ___________________________________________________________________________________________________________________________
###################

# Intro and instructions:
	instr("Herzlich willkommen und vielen Dank für die Teilnahme an diesem Experiment.\n\n\n\n---  Drücken Sie die Leertaste um fortzufahren  ---");
	instr("In den nächsten 30 Minuten werden Sie verschiedene Symbole betrachten.\nIhre Aufgabe ist es dabei, sich auf das Kreuz in der Bildschirmmitte zu konzentrieren.\n\n---  Drücken Sie die Leertaste um fortzufahren  ---");
	instr("Zwischendurch sollen Sie regelmäßig angeben, welche Emotionen diese Stimuli in Ihnen auslösen.\nEs gibt dabei keine „richtigen“ oder „falschen“ Antworten,\nantworten Sie deshalb bitte so ehrlich wie möglich!\n\n\n---  Drücken Sie die Leeraste um fortzufahren  ---");

	practice_rating(); 			#practice rating slider
	
# Cue acquisition:
	instrvl("Ihre Versuchsleitung wird jetzt die Aufzeichnung starten.\nHaben Sie noch Fragen?\n\nBitte geben Sie jetzt Ihrer Versuchsleitung Bescheid.");
	cue_conditions.shuffle(); 	#shuffle CS+ and CS- presentations
	acquisition_phase();			#start acquisition trials


# Extinction training:
	ext_conditions.shuffle();	#shuffle CS+ and CS- presentations for Extinction
	extinction_phase();			#start extinction trials

# End:
	term.print("End of experiment\n");
	instr("Ende des Experiments.\n\nBitte warten Sie auf die Versuchsleitung!");  
