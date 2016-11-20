__author__ = 'Don'

# global definitions for FALSE, TRUE, UNSURE, and NONE
# use these in your code, where necessary
FALSE  =  0
TRUE   =  1
UNSURE = -1
NONE   = "none"


def howDoYouKnowSheIsAWitch():
    print("CROWD: We have found a witch, amy we burn her?")
    print("CROWD: Burn her!  Burn her!")
    print("SIR BEDEVERE: How do you know she is a witch?")
    answer = NONE
    villager = 0

    while answer != "she looks like one":
        villager += 1
        print("VILLAGER", villager, ":")
        answer = input("")

    print("SIR BEDEVERE: Bring her forward")

    return TRUE



# TODO 1: add a while loop that will accept the phrase "they dressed me up like this"
# TODO 1: give the witch 3 attempts to get it right
# TODO 1: if she does, output the given message and return TRUE
# TODO 1: otherwise, return FALSE
def butYouAreDressedAsOne():
    print("WITCH: I'm not a witch.  I'm not a witch.")
    print("SIR BEDEVERE: But you are dressed as one...?")

    answer = NONE
    attempts = 1

    while answer != "they dressed me up like this" and attempts < 4:
        attempts += 1
        answer = input("WITCH: ")

    if answer == "they dressed me up like this":
        print("CROWD: No we didn't - no.")
        return TRUE
    else:
        return FALSE


# TODO 2: add a while loop that will look for the user to enter one of two strings
# TODO 2:    "well, we did do the nose" OR "that's her real nose"
# TODO 2: the loop should run as long as neither of the phrases has been entered
# TODO 2: if the string "well, we did do the nose" is entered, return TRUE
# TODO 2: otherwise, return FALSE
def andThisIsntMyNose():
    print("WITCH: And this isn't my nose, it's a false one.")
    print("SIR BEDEVERE: Well...?")

    answer = NONE
    villager = 0

    while answer != "well, we did do the nose" and answer != "that's her real nose":
        villager += 1
        print("VILLAGER", villager, ":")
        answer = input("")

    if answer == "well, we did do the nose":
        return TRUE
    else:
        return FALSE


# TODO 3: add a while loop that will look for the user to enter one of two strings
# TODO 3:    "and the hat" OR "she was wearing that hat"
# TODO 3: the loop should run as long as neither of the phrases has been entered
# TODO 3: if the phrase "and the hat" is entered,
# TODO 3: output the provided messages, and return TRUE
# TODO 3: otherwise, return FALSE
def andTheHat():
    print("SIR BEDEVERE: The Nose...?")
    answer = NONE
    villager = 0

    while answer != "and the hat" and answer != "she was wearing that hat":
        villager += 1
        print("VILLAGER", villager, ":")
        answer = input("")

    if answer == "and the hat":
        print("VILLAGER", villager, "But she is a witch.")
        print("CROWD: Burn her! Witch!  Burn her!")
        return TRUE
    else:
        return FALSE


# TODO 4: this is a complicated one - write code to implement the following logic
# TODO 4: at any point, if the villagers say no 4 or more times in a row, then return FALSE
# TODO 4: if the villagers say "no" exactly 3 times in a row
# TODO 4: AND then say "yes" AT LEAST 2 times in a row, AND then say "a bit" exactly 2 times in a row
# TODO 4: you should return TRUE
# TODO 4: NOTE: this one takes a lot of thought and experimentation to figure out
# TODO 4: HINTS: use the provided variables to keep track of the various consecutive word counts
# TODO 4: HINTS: if you are looking for consecutive words, and a word comes in that is out of place,
# TODO 4: HINTS: remember to restart the appropriate counts
def didYouDressHerUpLikeThis():
    print("SIR BEDEVERE: Did you dress her up like this...?")

    # declare and initialize variables

    # initialize so that
    answer = NONE

    # counts villager's responses
    villager = 0

    # counts consecutive "no"s
    noCount = 0

    # counts consecutive "yes"s after 3 consecutive "no"s
    yesCount = 0

    # counts Consecuitve "a bit"s after 3 consecutive "no"s and >= 2 consecutive "yes"s
    aBitCount = 0

    # initialize to value that allows while loop to run
    returnValue = UNSURE

    # accept villager input until returnValue is set to TRUE or FALSE
    while returnValue == UNSURE:
        # count the villager responses and prompt for input
        villager += 1
        print("VILLAGER", villager, ":")
        answer = input("")

        # if less than 3 no's in-a-row
        # STATE: -, N, NN
        if noCount < 3:
            # if villager answered "no"
            # count no's and reset other counts
            if answer == "no":
                # NEW STATE: N, NN, NNN
                noCount  += 1
                yesCount  = 0
                aBitCount = 0
            # otherwise, reset all counts and start over
            else:
                # NEW STATE: -
                noCount   = 0
                yesCount  = 0
                aBitCount = 0
        # else if 3 no's in a row
        # STATE: NNN...
        elif noCount == 3:
            # if all other counts are 0
            # STATE: NNN
            if yesCount == 0 and aBitCount == 0:
                # if another "no", then 4-in-a-row, we're done, they did NOT dress her up like this
                if answer == "no":
                    # NEW STATE: NNNN
                    returnValue = FALSE
                # if "yes", then count it
                elif answer == "yes":
                    # NEW STATE: NNNY
                    yesCount += 1
                # otherwise, out of order, reset all counts and start over
                else:
                    # NEW STATE: -
                    noCount   = 0
                    yesCount  = 0
                    aBitCount = 0
            # else if counting yes's and 0 "a bit"s, yet
            # STATE: NNN or NNNY
            elif yesCount < 2 and aBitCount == 0:
                # if "no", start over at 1 "no"
                if answer == "no":
                    # NEW STATE: N
                    noCount   = 1
                    yesCount  = 0
                    aBitCount = 0
                # if "yes", count it
                elif answer == "yes":
                    # NEW STATE: NNNY or NNNYY
                    yesCount += 1
                # else, out-of-order, reset all counts, and start over
                else:
                    # NEW STATE: -
                    noCount   = 0
                    yesCount  = 0
                    aBitCount = 0
            # else, if 2 or more "yes"s in-a-row
            # STATE: NNNYY*...
            elif yesCount >= 2:
                # if no "a bit"s yet
                # STATE: NNNYY*
                if aBitCount == 0:
                    # if "no", start over at 1 "no"
                    if answer == "no":
                        # NEW STATE: N
                        noCount   = 1
                        yesCount  = 0
                        aBitCount = 0
                    # if "yes", keep counting them
                    elif answer == "yes":
                        # NEW STATE: NNNYY*
                        yesCount += 1
                    # if "a bit", start counting them
                    elif answer == "a bit":
                        # NEW STATE: NNNYY*B
                        aBitCount += 1
                    # anything else is out-of-order, reset all counts and start over
                    else:
                        # NEW STATE -
                        noCount   = 0
                        yesCount  = 0
                        aBitCount = 0
                # if we have one "a bit"
                # STATE: NNNYY*B
                elif aBitCount == 1:
                    # if "no", start over at 1 "no"
                    if answer == "no":
                        # NEW STATE: N
                        noCount   = 1
                        yesCount  = 0
                        aBitCount = 0
                    # if a second "a bit", we're done, they dressed her up like this
                    elif answer == "a bit":
                        # NEW STATE: NNNYY*BB
                        returnValue = TRUE
                    # anything else is out of order, reset all counts and start over
                    else:
                        # NEW STATE: -
                        noCount   = 0
                        yesCount  = 0
                        aBitCount = 0

    return returnValue

def sheTurnedMeIntoANewt():
    print("VILLAGER #1: She has got a wart")
    print("SIR BEDEVERE: What makes you think she is a witch")
    print("VILLAGER #3: Well, she turned me into a newt.")
    print("SIE BEDEVERE: A newt?")
    print("VILLAGER #3: I got better")
    print("VILLAGER #2: Burn her anyway")


def tellMeWhatDoYouDoWithWitches():
    print("SIR BEDEVERE: Quiet!  Quiet!  Quiet! There are ways of telling whether she is a witch.")
    print("CROWD: Are there?  What are they?")
    print("VILLAGER #2: Do they hurt?")
    print("SIR BEDEVERE: Tell me, what do you do with witches...?")

    answer   = NONE
    villager = 0

    while answer != "burn":
        villager += 1
        print("VILLAGER", villager, ":")
        answer = input("")


def andWhatDoYouBurnApartFromWitches():
    print("SIR BEDEVERE: And what do you burn apart from witches...?")
    answer   = NONE
    villager = 0

    while answer != "wood":
        villager += 1
        print("VILLAGER", villager, ":")
        answer = input("")


def soWhyDoWitchesBurn():
    print("SIR BEDEVERE: So, why do witches burn...?")
    answer   = NONE
    villager = 0

    while answer != "because they're made of wood?":
        villager += 1
        print("VILLAGER", villager, ":")
        answer = input("")

    print("Good!")


# TODO 5: write a while loop that accepts the phrase "if she weighs the same as a duck"
# TODO 5: and give the user 3 attempts to enter the correct phrase
# TODO 5: if the correct answer is provided, print the given message and return TRUE
# TODO 5: otherwise, return FALSE
def soHowDoWeTellWhetherSheIsMadeOfWood():
    print("SIR BEDEVERE: So, how do we tell whether she is made of wood...?")
    answer   = NONE
    villager = 1

    # wait for a correct wild guess, but only for three attempts
    while answer != "if she weighs the same as a duck" and villager < 4:
        print("VILLAGER", villager, ":")
        answer = input("")
        villager += 1

    if answer == "if she weighs the same as a duck":
        print("SIR BEDEVERE: Well, that was certainly an inspired guess")
        return TRUE
    else:
        return FALSE

# TODO 6: write a while loop that accepts either of two phrases
# TODO 6:   "no, it floats" OR "throw her into the pond"
# TODO 6: if the phrase is "no, it floats", output the given message
def doesWoodSinkInWater():
    print("SIR BEDEVERE: Does wood sink in water...?")
    answer   = NONE
    villager = 0

    while answer != "no, it floats" and answer != "throw her into the pond":
        villager += 1
        print("VILLAGER", villager, ":")
        answer = input("")

    if answer == "no, it floats":
        print("VILLAGER", villager + 1, ": it floats, throw her into the pond!")


def whatElseFloatsInWater():
    print("SIR BEDEVERE: What else floats in water...?")
    answer   = NONE
    villager = 0

    while answer != "a duck":
        villager += 1
        print("VILLAGER", villager, ":")
        answer = input("")

    print("CROWD: Oooh.")


def soLogically():
    print("SIR BEDEVERE: Exactly!  So,logically...")
    print("VILLAGER: If...she...weighs the same as a duck...she's made of wood.")
    print("SIR BEDEVERE: And therefore?")
    print("VILLAGER: A witch")


# this function collects the weight of the duck from the user
# the weight is validated to be between 3 and 10 pounds, inclusive
# the user is allowed up to 3 attempts to enter a valid weight
# the function returns a weight of 1 for the duck if the weight
# is out of range and the maximum of attempts was reached
def getDuckWeight():
    print("SIR BEDEVERE: We shall use my largest scales.")
    print("SIR BEDEVERE: First, enter the weight of an unladen European duck:")

    weight   = -1
    attempts = 1

    while (weight < 3 or weight > 10) and attempts <= 3:
        weight = int(input("#: "))
        attempts += 1

        if weight < 3:
            print("SIR BEDEVERE: That seems awfully light for a European duck.")
        elif weight > 10:
            print("SIR BEDEVERE: That seems awfully heavy for a European duck - are you sure it's unladen?")

    # if weight isn't valid, set it to 1 and print a message
    if weight < 3 or weight > 10:
        print("SIR BEDEVERE: Obviously, you can't find an unladen European duck.  Let her go.")
        weight = 1

    return weight


# TODO 7: add a while loop that collects the witch's weight from the user
# TODO 7: the loop should continue to accept input until the entered value
# TODO 7: is between 2 and 200 pounds inclusive for a maximum of 4 attempts
# TODO 7: the function should accept and return the weight as an integer
# TODO 7: make sure to declare and initialize your test values
# TODO 7: whenever an invalid weight is entered, print the appropriate message
# TODO 7: if a valid weight is not entered within the maximum # of attempts,
# TODO 7: print the third message, and return a weight of 100 for the witch
def getWitchWeight():
    print("SIR BEDEVERE: Now, enter the weight of the alleged witch:")

    weight   = -1
    attempts = 1

    while (weight < 2 or weight > 200) and attempts <= 4:
        weight = int(input("#: "))
        attempts += 1

        if weight < 2:
            print("SIR BEDEVERE: That seems awfully light for a witch - perhaps she's a fairy.")
        elif weight > 200:
            print("SIR BEDEVERE: That seems awfully heavy for a witch - perhaps we could build a bridge out of her.")

    if (weight < 2 or weight > 200):
        print("SIR BEDEVERE: Obviously, at that weight, she won't weigh the same as a duck.  Let her go.")
        weight = 100

    return weight


# TODO 8: supply the logic statement that completes the function
# TODO 8: if the witch weighs within +/- 33% of the duck's weight
# TODO 8:   then print the appropriate statement and return TRUE,
# TODO 8:   otherwise print the appropriate statement and return FALSE
def sheWeighsTheSameAsADuck(witch, duck):
    if witch >= duck * 0.67 and witch <= duck * 1.33:
        print("SIR BEDEVERE: She falls within the weight range for an unladen European duck.")
        return TRUE
    else:
        print("SIR BEDEVERE: She falls outside the weight range for an unladen European duck.")
        return FALSE


def burnHer():
     print("CROWD: A witch! A witch!")
     print("WITCH: It's a fair cop.")
     print("CROWD: Burn her!  Burn her!")


def shesNotAWitch():
    print("SIR BEDEVERE: She's not a witch!  She's not a witch!  Release her!")


def main():
    # does she look like a witch?
    looksLikeAWitch = howDoYouKnowSheIsAWitch()

    # are those her real clothes?
    notHerRealClothes = butYouAreDressedAsOne()

    # did they put the nose on her?
    theyDidTheNose = andThisIsntMyNose()

    # did they put the hat on her?
    theyDidTheHat = andTheHat()

    # did they dress her up?
    theyDressedHerUp = didYouDressHerUpLikeThis()

    # a villager claims she turned him into a newt
    sheTurnedMeIntoANewt()

    # Sir Bedevere teaches the villagers how to identify witches
    tellMeWhatDoYouDoWithWitches()
    andWhatDoYouBurnApartFromWitches()
    soWhyDoWitchesBurn()

    # if the villagers have a truly inspired guess, than skip the following
    # parts of the dialog
    if soHowDoWeTellWhetherSheIsMadeOfWood() == FALSE:
        doesWoodSinkInWater()
        whatElseFloatsInWater()
        soLogically()

    # TODO 9: and now for something completely different
    # TODO 9: we're going to put all of the pieces together and decide whether she is a witch or not
    # TODO 9: there were five variables being set while Sir Bedevere is asking questions:
    # TODO 9:     looksLikeAWitch: TRUE if she looks like a witch, FALSE otherwise
    # TODO 9:     notHerRealClothes: TRUE if she says they dressed her up like this, FALSE if those are her real clothes
    # TODO 9:     theyDidTheNose: TRUE if the villagers put the nose on her, FALSE if it is her real nose
    # TODO 9:     theyDidTheHat: TRUE if the villagers put the hat on her, FALSE if it is her own hat
    # TODO 9:     theyDressedHerUp: TRUE if the villagers admit to dressing her up, FALSE otherwise
    # TODO 9:
    # TODO 9: Here is where it gets interesting
    # TODO 9: write the logic statements to determine whether or not she is a witch, based on those 5 variables,
    # TODO 9: AND on her weight compared to that of a duck
    # TODO 9: the logic is as follows:
    # TODO 9:    if she does NOT look like a witch, then she is NOT a witch
    # TODO 9:    else, if those are her real clothes, then she IS a witch, burn her
    # TODO 9:    else, if the villagers did both the nose AND the hat
    # TODO 9:                   AND they dressed her up
    # TODO 9:                       get the duckWeight, and the witchWeight
    # TODO 9:                       AND then if she weighs the same as a duck, she IS a witch, burn her
    # TODO 9:                       if she does not weigh the same as a duck, she is NOT a witch
    # TODO 9:                   if the villagers did NOT admit to dressing her up, then she IS a witch, burn her
    # TODO 9:               if the villagers did neither the nose NOR the hat, she IS a witch, burn her
    # TODO 9:               else, they did one or the other but not both
    # TODO 9:                   get the duckWeight, and the witchWeight
    # TODO 9:                   AND then if she weighs the same as a duck, she IS a witch, burn her
    # TODO 9:                   if she does not weigh the same as a duck, she is NOT a witch
    # TODO 9:
    # TODO 9: make sure to call the appropriate functions for getting the duck weight: getDuckWeight()
    # TODO 9:    getting the witch weight: getWitchWeight(),
    # TODO 9:    and then comparing those weights (sheWeighsTheSameAsADuck()
    # TODO 9: make sure to pay attention to the return values for each function, and the paramters that must
    # TODO 9:    be passed to sheWeighsTheSameAsADuck()
    # TODO 9: also, if she is a witch, call burnHer(), and if she isn't, call shesNotAWitch()
    if looksLikeAWitch:
        if notHerRealClothes:
            if theyDidTheNose and theyDidTheHat:
                if theyDressedHerUp:
                    if sheWeighsTheSameAsADuck(getWitchWeight(), getDuckWeight()):
                        burnHer()
                    else:
                        shesNotAWitch()
                else:
                    burnHer()
            elif not theyDidTheNose and not theyDidTheHat:
                burnHer()
            else:
                if sheWeighsTheSameAsADuck(getWitchWeight(), getDuckWeight()):
                    burnHer()
                else:
                    shesNotAWitch()
        else:
            burnHer()
    else:
        shesNotAWitch()

    input("Press Enter to Exit")


main()
