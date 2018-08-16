ITP 125 Final Project -
December 8th, 2016

The Old Spice voice message program can be run in two different ways:

(1) If the user wishes to make choices within the program, run (for OSX):

        python project.py

(2) If the user has preselected choices, run (for OSX):

        python project.py -g (a) -n (b) -r (c) -e (d) -o (e)

        The flags (-g -n -r -e -o) can be in any order.

        (a) -g = gender. Must select either 'm' for male or 'f' for female.
        (b) -n = number. Must input a ten digit phone number.
        (c) -r = reasons. Depending on the gender selected, there will be
            different valid responses. Check the section below. Must be digits.
        (d) -e = endings. Depending on the gender selected, there will be
            different valid responses. Must be digits.
        (e) -o = output filename. This is the mp3 file that the voicemail will
            be outputted to.

VALID CHOICES
For male:
  - reasons (numbers 1-4 are valid):
    [1] '... building an orphanage for children... '
    [2] '... cracking walnuts with their man mind.'
    [3] '... polishing their monocle smile.'
    [4] '... ripping out mass loads of weights.'
  - endings (numbers 1-5 are valid):
    [1] 'I'm on a horse.'
    [2] *jingle*
    [3] 'I'm on a phone.'
    [4] 'Swan dive!'
    [5] 'This voicemail is now diamonds.'

For female:
  - reasons (numbers 1-5 are valid):
    [1] '... ingesting my delicious old spice man smell.'
    [2] '... listening to me read romantic poetry... '
    [3] '... enjoying a delicious lobster dinner... '
    [4] '... being serenaded on the moon with a view of the Earth... '
    [5] '... riding a horse backwards with me.'
  - endings (numbers 1-2 are valid):
    [1] '... but she'll get back to you as soon as she can.'
    [2] 'Thanks for calling.'

    The program will check to confirm that the choices, whether given via the
command line or selected within the program, are correct. The only time the
program will quit is if the inputs on the command line had the incorrect number
of arguments, or the number of arguments was correct but something in there was
incorrect (for example, 5 was inputted when the valid range of numbers was 1-4).
Otherwise, the program will keep asking the user for inputs until a valid one
is inputted.

  Then, the user confirms or denies their valid choices. If they deny, the
program restarts from the beginning, regardless if the user entered
information via the command line or not.

  If they confirm, the program will ask for the filename (if one was not already
given), and then download the corresponding .mp3 file. The names of the files
used, along with the selected gender, will also be outputted to a file called
"sequence.txt". Be careful to ensure an important file is not already named
this, because whatever is written there will be overwritten.
