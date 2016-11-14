__author__ = 'djhake2'
# TODO 1: copy all of the code from the target program to be tested, EXCEPT
# TODO 1: FOR THE CALL TO main(), and place the code here.



# TODO 2: create a function from the TODO 9 code by moving this function definition above
# TODO 2:the code for TODO 9.
# TODO 2: DO NOT INCLUDE the final prompt that waits for the user to Press Enter to Exit in that function.
def isSheReallyAWitch(looksLikeAWitch, notHerRealClothes, theyDidTheNose, theyDidTheHat, theyDressedHerUp):


# TODO 3: place this code at the end of main(), above the code for the new isSheReallyAWitch function.
# TODO 3:  It will call the isHSeReallyAWitch  function that we just made.
# TODO 3: It will also pause for the user before exiting
# TODO 3: delete the same line that was previously in the code that followed the TODO 9 code
    # now check all of the villager's input to determine whether she really is a witch
    isSheReallyAWitch(looksLikeAWitch, notHerRealClothes, theyDidTheNose, theyDidTheHat, theyDressedHerUp)

    input("Press Enter to Exit")







# TODO 4: now run this program and execute the test cases from the test case PDF file
# TODO 4: and record the results in the test case document:
# TODO 4:    'P' for PASS
# TODO 4:    'F' for FAIL
# TODO 4:    'X' if the function is not implemented, does not compile, or crashes the program
def testMain():
    answer = input("Enter 'run' to run the program, anything else to test the program: ")
    if answer == "run":
        # we're going to run the program
        main()
    else:
        # we're going to test the program
        stillTesting = TRUE
        print("Testing MontyPythonWitchScene.py")
        while stillTesting:
            testTODO = int(input("Enter TODO # to test(1-9), any other # to quit: "))

            if testTODO == 1:
                print("*** Testing TODO 1: butYouAreDressedAsOne() ***")
                if butYouAreDressedAsOne() == TRUE:
                    print("*** test result: TRUE ***")
                else:
                    print("*** test result: FALSE ***")

            elif testTODO == 2:
                print("*** Testing TODO 2: andThisIsntMyNose() ***")
                if (andThisIsntMyNose() == TRUE):
                    print("*** test result: TRUE ***")
                else:
                    print("*** test result: FALSE ***")

            elif testTODO == 3:
                print("*** Testing TODO 3: andTheHat() ***")
                if andTheHat() == TRUE:
                    print("*** test result: TRUE ***")
                else:
                    print("*** test result: FALSE ***")

            elif testTODO == 4:
                print("*** Testing TODO 4: didYouDressHerUpLikeThis() ***")
                if didYouDressHerUpLikeThis() == TRUE:
                    print("*** test result: TRUE ***")
                else:
                    print("*** test result: FALSE ***")

            elif testTODO == 5:
                print("*** Testing TODO 5: soHowDoWeTellWhetherSheIsMadeOfWood() ***")
                if soHowDoWeTellWhetherSheIsMadeOfWood() == TRUE:
                    print("*** test result: TRUE ***")
                else:
                    print("*** test result: FALSE ***")

            elif testTODO == 6:
                print("*** Testing TODO 6: doesWoodSinkInWater() ***")
                doesWoodSinkInWater()
                print("*** test result ***")

            elif testTODO == 7:
                print("*** Testing TODO 7: getWitchWeight() ***")
                print("*** test result: Witch's weight =", getWitchWeight(), "***")

            elif testTODO == 8:
                print("*** Testing TODO 8: sheWeighsTheSameAsADuck() ***")
                witchWeight = int(input("Enter witch's test weight: "))
                duckWeight  = int(input("Enter duck's test weight:  "))

                if sheWeighsTheSameAsADuck(witchWeight, duckWeight) == TRUE:
                    print("*** test result: TRUE ***")
                else:
                    print("*** test result: FALSE ***")

            elif testTODO == 9:
                print("*** Testing TODO 9: Enter 1 for TRUE or 0 for FALSE ***")
                looksLikeAWitch   = int(input("looksLikeAWitch   = "))
                notHerRealClothes = int(input("notHerRealClothes = "))
                theyDidTheNose    = int(input("theyDidTheNose    = "))
                theyDidTheHat     = int(input("theyDidTheHat     = "))
                theyDressedHerUp  = int(input("theyDresedHerUp   = "))

                isSheReallyAWitch(looksLikeAWitch, notHerRealClothes, theyDidTheNose, theyDidTheHat, theyDressedHerUp)

                print("*** test result ***")
            else:
                stillTesting = FALSE

testMain()
