# Project 4:  Brevet time calculator with Ajax

## ACP controle times

That's "controle" with an 'e', because it's French, although "control"
is also accepted.  Controls are points where   
a rider must obtain proof of passage, and control[e] times are the
minimum and maximum times by which the rider must  
arrive at the location.   

The algorithm for calculating controle times is described at
https://rusa.org/octime_alg.html . 

Speeds are dictated by where precisely the control in question
is placed on the entire brevet. They are divided by thresholds,
which must be *met* to progress to the next one, so long
as the brevet length is shorter than the actual position of the
control. The controls are cumulative - the first 200 km use the
0-200 range, the next 200 the 200-400 range, and so on.

With the exceptions of 200 and 400 km brevets (noted below), closing 
controles - ones that occur at or after the brevet length - are treated
as though the control were only as long as the brevet itself and 
calculated in that way. A 407 km control will be different for 400 km
brevets and 600 km ones.

Brevets include a number of rules that are exceptions
the patterns described above, They are as follows:
  *The closing time of the starting checkpoint for a brevet is
always one hour after it opens.
  *The overall time limit for a 200 km brevet is always 13.5
hours, regardless of the actual position of the final control.
  *The overall time limit for a 400 km brevet is always 27 hours,
regardless of the actual position of the final control.

## AJAX and Flask reimplementation

The current RUSA controle time calculator is a Perl script that takes
an HTML form and emits a text page. The reimplementation fills in
times as the input fields are filled.  Each time a distance is filled
in, the corresponding open and close times should be filled in. This
functionality is a property of the original skeleton code. Please look
to the base project at https://github.com/UO-CIS-322/proj4-brevets for 
more information regarding it.

## Installation and utilization

The code may be forked, cloned, and otherwise employed as any other Github
project. Once cloned, you can change into the directory with the 'cd' 
command and use the commands 'bash ./configure' and 'make run' to run
the debugger version of the site. Gunicorn, if installed, can be used to
make a more long-term version with the command 'make service'. The server
runs on port 5000 by default, using Flask.

## Testing

A suite of nose test cases has been implemented to test the algorithms used
to calculate the open and close times of the controles. The provided suite
tests a brevet of each type, and may be run with the 'nosetests' command.
You must have nosetests installed to run them in that manner ('pip install
nosetests' should work if you do not and wish to run them.)

## Contact Details

If you have questions regarding the code, especially regarding the algorithm
used to calculate brevet times, you can contact me through email.
  *Name: Alexander Dibb
  *Email: adibb@cs.uoregon.edu