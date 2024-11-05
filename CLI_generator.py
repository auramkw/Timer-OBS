# Timer-OBS Generator (CLI)
import os

def get_minutes() -> str:
    minutes = int(input("How many minutes would you like your timer to be? Enter a number 0-999999:"))
    if minutes < 0:
        minutes = 0
    if minutes > 999999:
        minutes = 999999
    return minutes

def get_seconds() -> str:
    seconds = int(input("How many minutes would you like your timer to be? Enter a number 0-59:"))
    if seconds > 59:
        seconds = 59
    if seconds < 0:
        seconds = 0
    return seconds

def get_dir() -> str:
    dir_check = input("Would you like to change the folder your timer is in? If you select \"No\" your timer will be in the same folder as this file. ").casefold()
    if dir_check == "y" or dir_check == "yes" or dir_check == "ok" or dir_check == "okay":
        directory = input("Enter the directory you would like the program to output to: ")
        return directory
    else:
        directory = os.path.dirname(os.path.realpath(__file__))
        directory = directory + "\\"
        return directory
    return None

def get_filename() -> str:
    filename = input("What would you like to name your file? The file extension will be added automatically: ")
    filename = filename + ".html"
    return filename

def combine_dir_and_filename(directory: str, filename: str) -> str:
    fullname = directory + filename
    return fullname

def check_if_ok_with_user(minutes: int, seconds: int, fullpath: str) -> bool:
    print(f"Your timer will last {minutes} : {seconds} and the file will go into the file path {fullpath}")
    ok = input("Is this okay? Y/N: ").casefold()
    if ok == "y" or ok == "yes" or ok == "ok" or ok == "okay":
        print("Continuing with creation of file")
        return True
    elif ok == "n" or ok == "no":
        print("Restarting setup...")
        return False
    else:
        print("I didn't understand. Please try again.")
        return check_if_ok_with_user(minutes, seconds, path)

def write_to_file(minutes: int, seconds: int, fullname: str) -> None:
    with open(fullname, "w") as output:
        output.write("""
<!DOCTYPE html>
<head>
<title> Timer for OBS Browser Source by AuraMKW </title>
</head>
<body>
	<div id="timer"
	style="
	padding: 10px;
	display: inline-block;
	font-family: verdana, arial, sans-serif;
	text-align: center;
	color: white;
	background-color: rgba(255,255,255,255)
	border-radius: 5%;
	font-size: 50px;
	-webkit-text-stroke: 2px black;
	">
	
	</div>
	<script>
	async function countdown() {
""")
        output.write(f"             var start_mins = {minutes}; // change THE NUMBER to change the number of minutes and DO NOT remove the semi-colon after.\n")
        output.write(f"	            var start_secs = {seconds}; // change THE NUMBER to change the number of seconds and DO NOT remove the semi-colon after.\n")
        output.write("""	        var timer_element = document.getElementById("timer");
		while (start_mins > 0 || start_secs > 0) {
			await wait(1000)
			if (start_secs > 0) {
				start_secs--;
				
			}
			else if (start_secs <= 0 && start_mins > 0){
				start_mins--
				start_secs = 59
				
			}
			if (start_secs >= 10){
				timer_element.innerHTML = start_mins + " : " + start_secs
			}
			else if (start_secs <= 9) {
				timer_element.innerHTML = start_mins + " : 0" + start_secs
			}
			if (start_secs <= 0 && start_mins <= 0){
				timer_element.innerHTML = "soon" // if you want to change this message DO NOT REMOVE THE QUOTES. 
			}
			
		}
		
	}
	// The credit for this wait function goes to an answer found here: https://stackoverflow.com/questions/19389200/javascript-sleep-delay-wait-function
	function wait(time) {
		return new Promise(resolve => {
        setTimeout(resolve, time);
		});
	}
	countdown()
	
	</script>

</body>""")
    print(f"Completed writing to {fullname}")


    
def main():
    mins = get_minutes()
    secs = get_seconds()
    directory = get_dir()
    filename = get_filename()
    fullname = combine_dir_and_filename(directory, filename)
    
    ok_to_continue = check_if_ok_with_user(mins, secs, fullname)
    if not ok_to_continue:
        main()
    elif ok_to_continue:
        write_to_file(mins, secs, fullname)

main()
