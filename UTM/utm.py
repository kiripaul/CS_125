## Author: Paul Kiripolsky
## Class: CS 125, UVM Spring 2015
## Project: Universal Turing Machine Challenge

## Simple Sample call to TM class:  M = TM(['q0','q1','q2'],[0,1,'X','Y','-'],{'q0':[['q1','X','R'],['q2','Y','R']]},'q2')


## Defining a TM class first so that it can be passed to the UTM
class TM:
        def __init__(self, states, tape_alpha, transition_func, finish_state):
                self.states = states
                self.input_alpha = [0,1]
                self.tape_alpha = tape_alpha
                self.transition_func = transition_func
                self.start_state = 'q0' # In the definition of this TM and UTM, I will always use q0 as a start state
                self.blank_sym = "-" # Using '-' as the blank symbol
                self.finish_state = finish_state
                
        def getStates(self):
                return self.states

        def getTapeAlphabet(self):
                return self.tape_alpha

        def getTransitionFunction(self):
                return self.transition_func

        def getAcceptState(self):
                return self.finish_state

## Defining the UTM
## The input, winput, for the UTM is assumed to be of a String data type
class UTM:
        def __init__(self, TM, winput):
                self.winput = list(winput)
                self.states = TM.getStates()
                self.talphabet = TM.getTapeAlphabet()
                self.transition = TM.getTransitionFunction
                self.start_state = 'q0'
                self.blank = '-'
                self.accept = TM.getAcceptState()
                self.tape = {}

        def loadTape(self):
                for i in range(len(self.winput)):
                        self.tape[i] = self.winput[i]
                        print(self.tape)
                
