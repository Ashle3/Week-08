from number_guess import subtract_turn, runAttempt, main
import random
import os
import pytest

def runAttemptsTests(numAttempts:int, ranNum:int, reduceRunsBy:int = 0, defaultGuess:int = -1):
    
    numAttempts = 10
    
    ranNum = random.randint(1,101)
    
    attemptsLeft = numAttempts
    
    guesses = []
    
    attemptsRun = 0
    
    while(attemptsLeft-reduceRunsBy > 0):
        (attemptsLeft, guesses) = runAttempt(guesses, attemptsLeft, ranNum, True, defaultGuess)
        attemptsRun += 1
        
        assert type(attemptsLeft) == int, (f"type(attemptsLeft) == {type(attemptsLeft)} " +
                                           f"attemptsLeft == {attemptsLeft}")
        assert type(guesses) == list, (f"type(guesses) == {type(guesses)} " +
                                       f"guesses == {guesses}")
        for i in range(len(guesses)):
            assert type(guesses[i]) == int, (f"type(guesses[{i}]) == {type(guesses[i])} " + 
                                             f"guesses[{i}] == {guesses[i]}")
            
            assert guesses[i] == defaultGuess, (f"guesses[{i}] == {guesses[i]} "+
                                                f"defaultGuess == {defaultGuess}")
        
        assert len(guesses) == attemptsRun, (f"len(guesses) == {len(guesses)} " + 
                                           f"guesses == {guesses} " +
                                           f"attemptsRun == {attemptsRun}")
        assert (attemptsRun + attemptsLeft) == numAttempts
    
    
    assert attemptsRun + reduceRunsBy == numAttempts, (f"attemptsRun == {attemptsRun} " +
                                        f"numAttempts == {numAttempts}")
    
    return (attemptsLeft, guesses)

def AltNumAttempts(numAttempts:int):
    ranNum = random.randint(1,101)
    
    attemptsGiven = numAttempts
    
    runAttemptsTests(attemptsGiven, ranNum)
    
    
    ranNum = 50
    
    (attemptsLeft, guesses) = runAttemptsTests(attemptsGiven, ranNum, 1)
    
    (attemptsLeft, guesses) = runAttempt(guesses, attemptsLeft, ranNum, True, ranNum)
    
    assert attemptsLeft == -1, (f"attemptsLeft == {attemptsLeft}")
    
    for i in range(len(guesses)-1):
        assert type(guesses[i]) == int, (f"type(guesses[{i}]) == {type(guesses[i])} " + 
                                         f"guesses[{i}] == {guesses[i]}")
        
        assert guesses[i] == -1, (f"guesses[{i}] == {guesses[i]} "+
                                  f"defaultGuess == {-1}")
    
    assert type(guesses[i]) == int, (f"type(guesses[{i}]) == {type(guesses[i])} " + 
                                     f"guesses[{i}] == {guesses[i]}")
        
    assert guesses[-1] == ranNum, (f"guesses[{-1}] == {guesses[-1]} "+
                              f"ranNum == {ranNum}")

def test601():
    AltNumAttempts(11)
    AltNumAttempts(12)
    AltNumAttempts(13)
    

def test602():
    
    AltNumAttempts(9)
    AltNumAttempts(8)
    AltNumAttempts(7)

def testSubtract_turn():
    inputs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    outputs = [0, 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    
    assert len(inputs) == len(outputs), (f"len(inputs) == {len(inputs)}, "+
                                         f"len(outputs) == {len(outputs)}")
    
    for i in range(len(inputs)):
        result = subtract_turn(inputs[i])
        
        assert type(result) == type(outputs[i]), \
        (f"type(result) == {type(result)}, result == {result}, " + 
         f"type(outputs[{i}]) == {type(outputs[i])}, outputs[{i}] == {outputs[i]}")
        
        assert result == outputs[i], (f"result == {result}, outputs[{i}] == {outputs[i]}")
        
  
#change working directory to current directory
path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])