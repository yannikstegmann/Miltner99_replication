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
active_buttons = 2;
button_codes = 1,2; #we need "Space" and "S". Space to continue, S to stop.

##################################################
# SDL-structure
begin;


###################
###### Pain rating scale _________________________________________________________________________________________________________________________________________________
###################

picture {
	text { caption = "Please indicate how painful you perceived the electrical stimulus? (verbally):"; font_size = 24; font_color = 255,255,255; }; x = 0; y = 160;
	
	text { caption = "0 ------ 1 ------ 2 ------ 3 ------ 4 ------ 5 ------ 6 ------ 7 ------ 8 ------ 9 ------ 10"; 
			 font_size = 24; font_color = 255,255,255; }; 
	x = 0; y = 0;

	text { caption = "not painful\nat all"; 
			 font_size = 24; font_color = 255,255,255; }; 
	x = -520; y = -80;

	text { caption = "unbearably\npainful"; 
			 font_size = 24; font_color = 255,255,255; }; 
	x = 520; y = -80;
	
} rating_set;

# Trial definition: Pain rating
trial {
	trial_duration = forever;
	trial_type = specific_response;
   terminator_button =  2;

	stimulus_event {
		picture rating_set;
		time = 0;	
		code = "pain_rating";
	} rating;
} rating_trial;

# Trial definition: Red Fixcross for US
trial {
	trial_duration = 300;
	trial_type = fixed;
	
	stimulus_event {
		picture {text{caption = "+"; font_size = 24; font_color= 255,0,0;}fixkr;
		x=0; y=0;}us_text;
		time = 0;	
		
	} us_text_event;
} us_text_trial;

###################
###### Instruction presentation _________________________________________________________________________________________________________________________________________________
###################

trial {
	trial_duration = forever;
	trial_type = specific_response;
	terminator_button = 1;

	picture {
		text { caption = "Welcome, and thank you for participating in this experiment. 
We will now calibrate the intensity of the electrical stimuli."; font_size = 24; font_color = 255,255,255;}; x = 0; y = 140;
		text { caption = "You will experience a series of stimuli. For each sensation, 
please indicate how painful you perceive it using the following scale:"; font_size = 24; font_color = 255,255,255;}; x = 0; y = 0;
	} ;
} instruction_trial;

###################
###### US presentation _________________________________________________________________________________________________________________________________________________
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
###### PCL _______________________________________________________________________________________________________________________________________________________
###################

begin_pcl;

###################
###### Ports ____________________________________________________________________________________________________________________________________________________
###################

output_port port = output_port_manager.get_port( 1 ); # Digitimer/Shock Port

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
###### Shock Workup Procedure ____________________________________________________________________________________________________________________________________________________
###################

string code = logfile.subject(); # Subject code

instruction_trial.present(); 
term.print( "Press Space to start\n");

# Display rating stimuli until user stops
bool stop = false;  # Stop scenario (e.g. after calibration finished)

loop until
   stop == true
begin
	rating_trial.present(); 													# Present rating scale
	
	term.print("Wait for rating - continue with S\n");
	response_data last = response_manager.last_response_data(); 	# Check response

	
	shock();																			# Present US
	us_text_trial.present(); 													# 300ms break to slow things down
	
end;

