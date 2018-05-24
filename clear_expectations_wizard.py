#NOTES / THINGS TO ADD:
#add textwrap_print() to all the text
#add "I don't know" or "Kind of" functions (e.g., ***If they don't know if it's in Huzzah, give directions on how to find that.)
#[when all yes's] - gap?
    #"We know this
    #can be stressful ..."
#When sending an email to HR, give the option to notify them or not but include the reason why they would want to.
    #I would feel uncomfortable if they were notified without my consent

#--------------START CODE--------------#

import textwrap
import os

#cwd = os.getcwd()
#textwrap.fill(cwd)

#--------------BASIC FUNCTIONS FOR SIMPLICITY--------------#

def textwrap_print(words):
    print(textwrap.fill(words,replace_whitespace=False))

def enter_yes_or_no(loop):
    if loop[0] != "n" or "y":
        print("I'm sorry. Just to make sure I understand completely, please enter either 'YES' or 'NO' \n")

def help_ending():
    #textwrap_print("""
    #We know this all easier said than done, but just using this process is a step forward!
#
    #If you need help with the above suggestion(s), please reach out to wecare@zappos.com and someone from HR will help you out.
    #""")
    print("\nBest of luck and have a wonderful day!")

def nohelp_ending():
    print(textwrap.dedent("""
        If you need help with anything else, feel free to use this wizard again,
        or reach out to wecare@zappos.com and someone from HR will help you out.
        """))

print("LET THE TEST BEGIN!")

#--------------LOOP FUNCTIONS--------------#

def agreed_upon_interpretation():
    while True:
        agreed_upon_work = input("Do you agree with your Lead Link that you did not meet that expectation? \n").lower()
        if agreed_upon_work[0] == "y":
            print(textwrap.fill("""Your honesty is appreciated. Since you and your Lead Link had a mutual understanding of the expectation and it was not met, you should be provided with feedback to help you improve, as well as be given a reasonable amount of time to implement those learnings.

We know this can be stressful, but mistakes are part of the learning process. Your Lead Link should be guiding you through this and helping you grow. If you feel they aren't doing that for you, please reach out to wecare@zappos.com and someone from HR will help you out.
""",replace_whitespace=False))
            break
        if agreed_upon_work[0] == "n":
            print(textwrap.fill("Then there is definitely a misunderstanding that needs to be cleared up. HR will reach out to you shortly to assist."))
            #add function to e-mail something to HR
            help_ending()
            break
        enter_yes_or_no(agreed_upon_work)
        continue

def defined_in_huzzah():
    while True:
        #change the below part to a normal input if it can be done with textwrap.
        print(textwrap.fill("Do you agree with your Lead Link's interpretation of what that expectation entails? (i.e., Is your understanding of what you were supposed to do the same as what your Lead Link is saying you should have done?)"))
        mutual = input("".lower())
        #mutual = input(textwrap.fill("""Do you agree with your Lead Link's interpretation of what that expectation entails? I.E., is your understanding of what you were supposed to do the same as what your Lead Link is saying you should have done?\n
#""")).lower()
        if mutual[0] == "y":
            agreed_upon_interpretation()
            break
        if mutual[0] == "n":
            print(textwrap.fill("You can't be held accountable to an expectation unless it's 'clear', which means there is a mutual understanding of what that expectation entails. Inform your Lead Link that expectations need to be clearly defined in Huzzah for you to be held accountable to them."))
            help_ending()
            break
        enter_yes_or_no(mutual)
        continue

def example_was_given():
    while True:
        given_example = input("Was the example you were given an expectation that is clearly defined in Huzzah? \n").lower()
        if given_example[0] == "y":
            #provided_expectation = input("Please copy/paste the exact expectation in question. \n").lower()
            #print("Thank you.")
            defined_in_huzzah()
            break
        if given_example[0] == "n":
            print(textwrap.fill("If there wasn't a clearly defined expectation, you can't be expected to have known any better. Inform your Lead Link that expectations need to be clearly defined in Huzzah for you to be held accountable to them."))
            help_ending()
            break
        enter_yes_or_no(given_example)
        continue

def dun_been_questioned():
    while True:
        unclear_expectation = input("Was a specific example given as to what expectation you were not meeting? \n").lower()
        if unclear_expectation[0] == "y":
            example_was_given()
            break
        if unclear_expectation[0] == "n":
            #print(textwrap.fill("Then you couldn't possibly know what you did or didn't do. Ask your Lead Link for clarity around what you did or didn't do to make them question you, and get specific examples! They should be able to point out a clear expectation in Huzzah. Hopefully that should clear things up for everyone."))
            textwrap_print("Then you couldn't possibly know what you did or didn't do. Ask your Lead Link for clarity around what you did or didn't do to make them question you, and get specific examples! They should be able to point out a clear expectation in Huzzah. Hopefully that should clear things up for everyone.")
            help_ending()
            break
        enter_yes_or_no(unclear_expectation)
        continue

def base_script():
    while True:
        value_question = input("Has your productivity/value come into question? \n").lower()
        if value_question[0] == "y":
            dun_been_questioned()
            break
        if value_question[0] == "n":
            print("In that case, you just keep doing what you've been doing.")
            nohelp_ending()
            break
        enter_yes_or_no(value_question)
        continue

base_script()

#--------------TESTING: RE-RUN PROGRAM--------------#

while True:
    re_run = input("\n---Do you want to re-run this wizard?--- \n").lower()
    if re_run[0] == "y":
        base_script()
    if re_run[0] == "n":
        print("Bye, Felicia!")
        exit()
    enter_yes_or_no(re_run)
    continue
