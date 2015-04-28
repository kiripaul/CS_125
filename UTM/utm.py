## Author: Paul Kiripolsky
## Class: CS 125, UVM Spring 2015
## Project: Universal Turing Machine Challenge

## Simple Sample call to TM class:  Modus_TM = TM(['q0','q1','q2','q3','q4','q5','q6'],[0,1,'-'],{'q0':[['q1','-','R'],['q5','-','R'],['HALT']],
##                                                                                               'q1':[['q1','0','R'],['q2','1','R'],['HALT']],
##                                                                                               'q2':[['q3','1','L'],['q2','1','R'],['q4','-','L']],
##                                                                                               'q3':[['q3','0','L'],['q3','1','L'],['q0','-','R']],
##                                                                                               'q4':[['q4','0','L'],['q4','-','L'],['q6','0','R']],
##                                                                                               'q5':[['q5','-','R'],['q5','-','R'],['q6','-','R']],
##                                                                                               'q6':[['HALT'],['HALT'],['HALT']]},'q6')


## Defining a TM class first so that it can be passed to the UTM
        ## @@====================================================================================
        ## Note that the transition function can be predefined and be passed by reference.
        ## It is highly recommended (i.e. don't deviate from this method) to define the transition
        ## function as a dictionary input.
        ## @@====================================================================================
class TM:
        def __init__(self, states, tape_alpha, transition_func, finish_state):
                self.states = states
                self.input_alpha = ['0','1']
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
                self.current_state = ''
                self.next_state = ''
                self.blank = '-'
                self.accept = TM.getAcceptState()
                self.tape = {}

        def loadTape(self):
                for i in range(len(self.winput)):
                        self.tape[i] = self.winput[i]
                print(self.tape)

        def runUTM(self):
                current_element = self.winput[0]
        

                
