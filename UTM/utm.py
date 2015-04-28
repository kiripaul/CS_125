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


## Defining a TM class first so that it can be passed to the UTM:: M = (States, Input_alphabet, Tape_alphabet, Transition_function, Start_state, Blank_symbol, Finish_state)
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
                self.transition = TM.getTransitionFunction()
                self.start_state = 'q0'
                self.blank = '-'
                self.accept = TM.getAcceptState()
                self.tape = {}

        def loadTape(self):
                for i in range(len(self.winput)):
                        self.tape[i] = self.winput[i]
                #print(self.tape)

        def runUTM(self):
                self.loadTape()
                current_state = self.start_state
                current_input_key = self.tape[0]
                print("Current Input Key: "+current_input_key)
                print("Starting State: "+current_state)
                halt = False
                head_counter = 0
                next_state = ''
                while(halt==False):
                        transition_row = self.transition[current_state]
                        print("Transition Row: "+str(transition_row))
                        for i in range(len(transition_row)): #find the proper transition row for the current state
                                transition_bloc = transition_row[i]
                                print("Transition Bloc: "+str(transition_bloc))
                                if transition_bloc[current_input_key]: # find the proper truple for a given input
                                        print("Transition Bloc with Key: "+str(transition_bloc[current_input_key]))
                                        next_state = transition_bloc[current_input_key][0]
                                        print("Next State: "+next_state)
                                        if next_state == 'HALT':
                                                print("HALT STATE REACHED")
                                                break
                                        if next_state == self.accept:
                                                print("ACCEPT STATE REACHED")
                                                break
                                        break
                        
                        halt = True
                
                
                        

Modus_TM = TM(['q0','q1','q2','q3','q4','q5','q6'],[0,1,'-'],{'q0':[{'0':['q1','-','R']},{'1':['q5','-','R']},{'-':['HALT']}],
                                                               'q1':[{'0':['q1','0','R']},{'1':['q2','1','R']},{'-':['HALT']}],
                                                               'q2':[{'0':['q3','1','L']},{'1':['q2','1','R']},{'-':['q4','-','L']}],
                                                               'q3':[{'0':['q3','0','L']},{'1':['q3','1','L']},{'-':['q0','-','R']}],
                                                               'q4':[{'0':['q4','0','L']},{'1':['q4','-','L']},{'-':['q6','0','R']}],
                                                               'q5':[{'0':['q5','-','R']},{'1':['q5','-','R']},{'-':['q6','-','R']}],
                                                               'q6':[{'0':['HALT']},['HALT'],['HALT']]},'q6')

modus_utm = UTM(Modus_TM,'000100')
modus_utm.runUTM()

               
        

                
