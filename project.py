# ITP 125 Final Project - Program
# December 8th, 2016
################################################################################

# importing necessary libraries
import urllib, sys, os, getopt
from collections import OrderedDict
from subprocess import call
from sys import platform as _platform

########################### GLOBAL VARIABLES ###################################
# These global variables are used throughout all functions.

# blank strings which will later hold the gender, phone number, reason numbers,
# ending numbers, and the filename
gender, number, reasons, endings, filename = "", "", "", "", ""

# array of possible male reasons
malereasons = ["[1] '... building an orphanage for children... '",
"[2] '... cracking walnuts with their man mind.'",
"[3] '... polishing their monocle smile.'",
"[4] '... ripping out mass loads of weights.'"]

# array of possible male endings
maleendings = ["[1] 'I'm on a horse.'", "[2] *jingle*",
"[3] 'I'm on a phone.'", "[4] 'Swan dive!'",
"[5] 'This voicemail is now diamonds.'"]

# array of possible female reasons
femalereasons = ["[1] '... ingesting my delicious old spice man smell.'",
"[2] '... listening to me read romantic poetry... '",
"[3] '... enjoying a delicious lobster dinner... '",
"[4] '... being serenaded on the moon with a view of the Earth... '",
"[5] '... riding a horse backwards with me.'"]

# array of possible female endings
femaleendings = ["[1] '... but she'll get back to you as soon as she can.'",
"[2] 'Thanks for calling.'"]

# URL used for all file downloads
globalurl = "http://www-bcf.usc.edu/~chiso/itp125/project_version_1/"

# blank dictionaries which will hold relationships of numbers (either from
# phone numbers or array indices) and its corresponding mp3 filename
numToMP3dict, reasonsToMP3dict, endingsToMP3dict = {}, {}, {}

# set that will hold what will be recorded to output file
fileset = []

# logic to determine which platform the program is being run on
OSX = False
if _platform == "linux" or _platform == "linux2" or _platform == "win32":
    # Linux or Windows
    OSX = False
elif _platform == "darwin":
    #OSX
    OSX = True

################################# FUNCTIONS ####################################
# function to download appropriate mp3 files based on the phone number given
def numberDownload():
    global number, numToMP3dict, globalurl
    numberslist = list(set(number)) # only one of each needed is downloaded
    for x in range(len(numberslist)):
        num = numberslist.pop()
        mp3 = num + ".mp3"
        url = globalurl + mp3
        urllib.urlretrieve(url, mp3) # retrieves file
        numToMP3dict[num] = mp3 # records number to corresponding filename

# function to download male mp3 files based on reasons and endings given
def maleDownload():
    global reasons, endings, reasonsToMP3dict, endingsToMP3dict, globalurl

    # these files are necessary for all male voicemails
    urllib.urlretrieve (globalurl + "m-b1-hello.mp3",
                                    "m-b1-hello.mp3")
    urllib.urlretrieve (globalurl + "m-b2-have_dialed.mp3",
                                    "m-b2-have_dialed.mp3")
    urllib.urlretrieve (globalurl + "m-r0-cannot_come_to_phone.mp3",
                                    "m-r0-cannot_come_to_phone.mp3")
    urllib.urlretrieve (globalurl + "m-leave_a_message.mp3",
                                    "m-leave_a_message.mp3")

    # downloads appropriate files based on reasons selected and records
    # reason number with its corresponding filename in the dictionary
    reasonslist = list(set(reasons)) # only one of each is needed
    if '1' in reasonslist:
        urllib.urlretrieve (globalurl + "m-r1-building.mp3",
                                        "m-r1-building.mp3")
        reasonsToMP3dict['1'] = "m-r1-building.mp3"
    if '2' in reasonslist:
        urllib.urlretrieve (globalurl + "m-r2-cracking_walnuts.mp3",
                                        "m-r2-cracking_walnuts.mp3")
        reasonsToMP3dict['2'] = "m-r2-cracking_walnuts.mp3"
    if '3' in reasonslist:
        urllib.urlretrieve (globalurl + "m-r3-polishing_monocole.mp3",
                                        "m-r3-polishing_monocole.mp3")
        reasonsToMP3dict['3'] = "m-r3-polishing_monocole.mp3"
    if '4' in reasonslist:
        urllib.urlretrieve (globalurl + "m-r4-ripping_weights.mp3",
                                        "m-r4-ripping_weights.mp3")
        reasonsToMP3dict['4'] = "m-r4-ripping_weights.mp3"

    # downloads appropriate files based on endings selected and records
    # ending number with its corresponding filename in the dictionary
    endingslist = list(set(endings)) # only one of each is needed
    if '1' in endingslist:
        urllib.urlretrieve (globalurl + "m-e1-horse.mp3",
                                        "m-e1-horse.mp3")
        endingsToMP3dict['1'] = "m-e1-horse.mp3"
    if '2' in endingslist:
        urllib.urlretrieve (globalurl + "m-e2-jingle.mp3",
                                        "m-e2-jingle.mp3")
        endingsToMP3dict['2'] = "m-e2-jingle.mp3"
    if '3' in endingslist:
        urllib.urlretrieve (globalurl + "m-e3-on_phone.mp3",
                                        "m-e3-on_phone.mp3")
        endingsToMP3dict['3'] = "m-e3-on_phone.mp3"
    if '4' in endingslist:
        urllib.urlretrieve (globalurl + "m-e4-swan_dive.mp3",
                                        "m-e4-swan_dive.mp3")
        endingsToMP3dict['4'] = "m-e4-swan_dive.mp3"
    if '5' in endingslist:
        urllib.urlretrieve (globalurl + "m-e5-voicemail.mp3",
                                        "m-e5-voicemail.mp3")
        endingsToMP3dict['5'] = "m-e5-voicemail.mp3"

# function to download female mp3 files based on reasons and endings given
def femaleDownload():
    global reasons, endings, reasonsToMP3dict, endingsToMP3dict, globalurl

    # these files are necessary for all female voicemails
    urllib.urlretrieve (globalurl + "f-b1-hello_caller.mp3",
                                    "f-b1-hello_caller.mp3")
    urllib.urlretrieve (globalurl + "f-b2-lady_at.mp3",
                                    "f-b2-lady_at.mp3")
    urllib.urlretrieve (globalurl + "f-r0.1-unable_to_take_call.mp3",
                                    "f-r0.1-unable_to_take_call.mp3")
    urllib.urlretrieve (globalurl + "f-r0.2-she_is_busy.mp3",
                                    "f-r0.2-she_is_busy.mp3")

    # downloads appropriate files based on reasons selected and records
    # reason number with its corresponding filename in the dictionary
    reasonslist = list(set(reasons)) # only one of each is needed
    if '1' in reasonslist:
        urllib.urlretrieve (globalurl + "f-r1-ingesting_old_spice.mp3",
                                        "f-r1-ingesting_old_spice.mp3")
        reasonsToMP3dict['1'] = "f-r1-ingesting_old_spice.mp3"
    if '2' in reasonslist:
        urllib.urlretrieve (globalurl + "f-r2-listening_to_reading.mp3",
                                        "f-r2-listening_to_reading.mp3")
        reasonsToMP3dict['2'] = "f-r2-listening_to_reading.mp3"
    if '3' in reasonslist:
        urllib.urlretrieve (globalurl + "f-r3-lobster_dinner.mp3",
                                        "f-r3-lobster_dinner.mp3")
        reasonsToMP3dict['3'] = "f-r3-lobster_dinner.mp3"
    if '4' in reasonslist:
        urllib.urlretrieve (globalurl + "f-r4-moon_kiss.mp3",
                                        "f-r4-moon_kiss.mp3")
        reasonsToMP3dict['4'] = "f-r4-moon_kiss.mp3"
    if '5' in reasonslist:
        urllib.urlretrieve (globalurl + "f-r5-riding_a_horse.mp3",
                                        "f-r5-riding_a_horse.mp3")
        reasonsToMP3dict['5'] = "f-r5-riding_a_horse.mp3"

    # downloads appropriate files based on endings selected and records
    # ending number with its corresponding filename in the dictionary
    endingslist = list(set(endings)) # only one of each is needed
    if '1' in endingslist:
        urllib.urlretrieve (globalurl + "f-e1-she_will_get_back_to_you.mp3",
                                        "f-e1-she_will_get_back_to_you.mp3")
        endingsToMP3dict['1'] = "f-e1-she_will_get_back_to_you.mp3"
    if '2' in endingslist:
        urllib.urlretrieve (globalurl + "f-e2-thanks_for_calling.mp3",
                                        "f-e2-thanks_for_calling.mp3")
        endingsToMP3dict['2'] = "f-e2-thanks_for_calling.mp3"

# function to generate the command line prompt needed to combine male mp3s
def concatenateMale():
    global number, reasons, endings, filename, fileset, OSX

    # will show in ouput file that the voicemail is male
    fileset.append("male")

    # determines which concatenation format is needed depending on platform
    if(OSX):
        final = "cat m-b1-hello.mp3 m-b2-have_dialed.mp3 "
    else:
        final = "copy /b m-b1-helo.mp3 + m-b2-have_dialed.mp3 + "
    # appends to output file set
    fileset.append("m-b1-hello.mp3")
    fileset.append("m-b2-have_dialed.mp3")

    # appends number mp3s to command line prompt using dictionary to return
    # appropriate filename
    for x in number:
        final += numToMP3dict[x] + " "
        if(OSX == False):
            final += "+ "
        fileset.append(numToMP3dict[x]) # dictionary used here

    final += "m-r0-cannot_come_to_phone.mp3 "
    if(OSX == False):
        final += "+ "
    fileset.append("m-r0-cannot_come_to_phone.mp3")

    # appends reason mp3s to command line prompt using dictionary
    for y in reasons:
        final += reasonsToMP3dict[y] + " "
        if (OSX == False):
            final += "+ "
        fileset.append(reasonsToMP3dict[y])

    final += "m-leave_a_message.mp3 "
    fileset.append("m-leave_a_message.mp3")

    # appends endings mp3s to command line prompt using dictionary
    for z in endings:
        if(OSX == False):
            final += "+ "
        final += endingsToMP3dict[z] + " "
        fileset.append(endingsToMP3dict[z])

    # checks platform to ensure concatenation format
    if(OSX == True):
        final += "> " + filename + ".mp3"
    else:
        final += "c:\\" + filename + ".mp3"

    # writes contents of fileset to a file named 'sequence.txt'
    f = open('sequence.txt', 'w')
    for x in fileset:
        f.write(x)
        f.write('\n')
    f.close()

    # calls command to command shell
    call(final, shell=True)

# function to generate the command line prompt needed to combine female mp3s
### same logic as concatenateMale() function
def concatenateFemale():
    global number, reasons, endings, filename, fileset, OSX

    fileset.append("female")

    if(OSX):
        final = "cat f-b1-hello_caller.mp3 f-b2-lady_at.mp3 "
    else:
        final = "copy /b f-b1-hello_caller.mp3 + f-b2-lady_at.mp3 + "
    fileset.append("f-b1-hello_caller.mp3")
    fileset.append("f-b2-lady_at.mp3")

    for x in number:
        final += numToMP3dict[x] + " "
        if(OSX == False):
            final += "+ "
        fileset.append(numToMP3dict[x])

    if(OSX):
        final += "f-r0.1-unable_to_take_call.mp3 f-r0.2-she_is_busy.mp3 "
    else:
        final+= "f-r0.1-unable_to_take_call.mp3 + f-r0.2-she_is_busy.mp3 "
    fileset.append("f-r0.1-unable_to_take_call.mp3")
    fileset.append("f-r0.2-she_is_busy.mp3")

    for y in reasons:
        if(OSX == False):
            final+= "+ "
        final += reasonsToMP3dict[y] + " "
        fileset.append(reasonsToMP3dict[y])

    for z in endings:
        if(OSX == False):
            final+= "+ "
        final += endingsToMP3dict[z] + " "
        fileset.append(endingsToMP3dict[z])

    if(OSX):
        final += "> " + filename + ".mp3"
    else:
        final += "c:\\" + filename + ".mp3"

    f = open('sequence.txt', 'w')
    for x in fileset:
        f.write(x)
        f.write('\n')
    f.close()

    call(final, shell=True)

# function that removes all of the files from desktop needed for concatenation
def removeFiles():
    global fileset

    fileset.pop(0) # removes 'male' or 'female' since they are not filenames
    for x in list(set(fileset)): # ensures file is deleted only once
        os.remove(x)

# function that prints out male reasons found in array
def maleReasons():
    global malereasons
    for x in malereasons:
        print x

# function that prints out male endings found in array
def maleEndings():
    global maleendings
    for x in maleendings:
        print x

# function that prints out female reasons found in array
def femaleReasons():
    global femalereasons
    for x in femalereasons:
        print x

# function that prints out female endings found in array
def femaleEndings():
    global femaleendings
    for x in femaleendings:
        print x

# function that checks the numbers inputted by user matches the number of
# available options for that set of reasons or endings
# mainset is the set inputted by user, numset is the possible range of numbers
def checkNumbers(mainset, numset):
    mainlist = list(set(mainset))
    for x in range(len(mainlist)):
        # if the user inputted an invalid number
        if mainlist.pop() not in numset: return False
    return True

# function to check if the command line inputs are correct
def correctCommandLineInputs():
    global gender, number, reasons, endings

    # gender is m or f
    if (gender != "m" and gender != "f"):
        return False

    # phone number length is 10
    if (len(number) != 10):
        return False

    # checks if the numbers inputted are in the range of the sets
    if (gender == "m"):
        if(checkNumbers(reasons, set(' 1234')) == False):
            return False
        if(checkNumbers(endings, set (' 12345')) == False):
            return False
    if (gender == "f"):
        if(checkNumbers(reasons, set(' 12345')) == False):
            return False
        if(checkNumbers(endings, set(' 12')) == False):
            return False

    # returns true if passed all tests
    return True

# main function (if command line inputs were not used)
def main():
    global gender, number, reasons, endings

    print("")

    # code to determine the gender of the caller, with input validation
    incorrectgender = True
    while incorrectgender:
        gender = raw_input("Enter 'm' for male or 'f' for female: ")
        if (gender == "m" or gender == "f"):
            # input was correct, can exit while loop
            incorrectgender = False
        else:
            print ("Oops, that wasn't an option!")

    print("")

    # code to find the phone number of the caller, with input validation
    incorrectnumber = True
    while incorrectnumber:
        number = raw_input("Please enter your 10-digit phone number: ")
        number = filter(str.isdigit, number) # ensures input is only digits
        if (len(number) == 10):
            # input was correct, can exit while loop
            incorrectnumber = False
        else:
            print ("Oops, the phone number did not have 10 digits!")

    print("")

    # code to find the reasons desired in the voice mail message
    # depends on gender
    print ("Listed are the available reasons for not answering the phone: ")
    if (gender == "m"):
        maleReasons() # prints reasons
        m_incorrectreasons = True
        while m_incorrectreasons:
            reasons = raw_input("Please choose the reason(s) " \
                        "you are unable to come to the phone (numbers 1-4): ")
            if(checkNumbers(reasons, set(' 1234'))):
                # input was correct, can exit while loop
                m_incorrectreasons = False
            else:
                print("Sorry, please only enter the numbers 1-4.")
    else:
        femaleReasons() # prints reasons
        f_incorrectreasons = True
        while f_incorrectreasons:
            reasons = raw_input("Please choose the reason(s) " \
                        "you are unable to come to the phone (numbers 1-5): ")
            if(checkNumbers(reasons, set(' 12345'))):
                # input was correct, can exit while loop
                f_incorrectreasons = False
            else:
                print("Sorry, please only enter the numbers 1-5.")

    print("")

    # code to find the endings desired in the voice mail message
    # depends on gender
    print ("Listed are the available endings for closing the message: ")
    if(gender == "m"):
        maleEndings() # prints endings
        m_incorrectendings = True
        while m_incorrectendings:
            endings = raw_input("Please choose the ending(s) " \
                        "you would like in your message (numbers 1-5): ")
            if(checkNumbers(endings, set(' 12345'))):
                # input was correct, can exit while loop
                m_incorrectendings = False
            else:
                print("Sorry, please only enter the numbers 1-5.")
    else:
        femaleEndings() # prints endings
        f_incorrectendings = True
        while f_incorrectendings:
            endings = raw_input("Please choose the ending(s) " \
                        "you would like in your message (numbers 1-2): ")
            if(checkNumbers(endings, set(' 12'))):
                # input was correct, can exit while loop
                f_incorrectendings = False
            else:
                print("Sorry, please only enter the numbers 1-2.")

    print("")
    confirm()

# function for printing out all gathered information for user to confirm
# then allows them to re-enter information if not satisfied
# or downlaod the file if satisfied
def confirm():
    global gender, number, reasons, endings, filename

    # replaces any spaces with no spaces (needed for listing them)
    reasons = reasons.replace(" ", "")
    endings = endings.replace(" ", "")

    print("Please confirm the following information.")

    # information printed depends on gender
    if (gender == "m"):
        print("Gender: male")
        print("Phone number: " + number)
        print("Reasons: ")

        # prints reasons in order given
        reasons = list(OrderedDict.fromkeys(reasons))
        for x in reasons:
            print malereasons[int(x)-1] # accounts for array index

        print("Endings: ")
        # prints endings in order given
        endings = list(OrderedDict.fromkeys(endings))
        for x in endings:
            print maleendings[int(x)-1] # accounts for array index

    else:
        print("Gender: female")
        print("Phone number: " + number)
        print("Reasons: ")

        # prints reasons in order listed
        reasonslist = list(set(reasons))
        for x in reasonslist:
            print femalereasons[int(x)-1]

        print("Endings: ")
        # prints endings in order listed
        endingslist = list(set(endings))
        for x in endingslist:
            print femaleendings[int(x)-1]

    # while loop to ensure user enters 'y' or 'n'
    incorrectconfirm = True
    while incorrectconfirm:
        confirm = raw_input("If you are satisfied, enter 'y'. " \
                "If you are not and want to restart the program, enter 'n': ")
        if (confirm == "n" or confirm == "y"):
            incorrectconfirm = False
        else:
            print("Please enter 'y' or 'n'.")

    # if not confirmed, return to main function and start over
    if (confirm == "n"):
        main()

    # if confirmed, obtain filename and proceed to download
    else:
        print("")
        filename = raw_input("What would you like your file to be called? ")
        print("")
        download()

# function to call subfunctions to download required files
def download():
    global filename

    # ensures .mp3 isn't at the end of the filename already (prevents .mp3.mp3)
    if(filename[-4:] == ".mp3"):
        filename = filename[:-4]

    print("Now downloading your file, " + filename + ".mp3. Thank you!")

    # calling functions to download mp3s needed
    numberDownload()
    if (gender == "m"):
        maleDownload()
        concatenateMale()
    if (gender == "f"):
        femaleDownload()
        concatenateFemale()

    # removes files following the concatenation
    removeFiles()

########################## START OF PROGRAM ####################################
print("--- Welcome to the Old Spice Voice Mail Message Creator ---")

# determines if user is inputting correct number of arguments for command line
try:
    opts, args = getopt.getopt(sys.argv[1:], 'g:n:r:e:o:')
except getopt.GetoptError as e:
    print("One of the options is missing an argument. " \
            "Please check the documentation and try again.")
    sys.exit(2)

# user did not input command line arguments, wants to continue to main function
if len(sys.argv) < 2:
    main()

# incorrect number of arguments
elif (len(sys.argv) >= 2 and len(sys.argv) < 11 or len(sys.argv) > 11):
    print("Incorrect number of arguments. Five are required (-g -n -r -e -o).")

# parses information given in command line
else:
    for o, a in opts:
        if o == '-g':
            gender = a
        if o == '-n':
            number = filter(str.isdigit, a) # ensures number is only digits
        if o == '-r':
            reasons = a
        if o == '-e':
            endings = a
        if o == '-o':
            filename = a

    # calls function to ensure all input is correct, if not the program exits
    if(correctCommandLineInputs() == False):
        print("Sorry, one or more of the arguments were incorrect. " \
                "Please refer to the documentation and try again.")

    # continue to confirmation
    else:
        print("")
        confirm()
