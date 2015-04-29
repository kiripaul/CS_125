## Author: Paul Kiripolsky
## Class: CS 125, UVM Spring 2015
## Project: Universal Turing Machine Challenge

## Simple Sample call to TM class:  Modus_TM = TM(['q0','q1','q2','q3','q4','q5','q6'],[0,1,'-'],
##                                                              {'q0':[{'0':['q1','-','R']},{'1':['q5','-','R']},{'-':['HALT']}],
##                                                               'q1':[{'0':['q1','0','R']},{'1':['q2','1','R']},{'-':['HALT']}],
##                                                               'q2':[{'0':['q3','1','L']},{'1':['q2','1','R']},{'-':['q4','-','L']}],
##                                                               'q3':[{'0':['q3','0','L']},{'1':['q3','1','L']},{'-':['q0','-','R']}],
##                                                               'q4':[{'0':['q4','0','L']},{'1':['q4','-','L']},{'-':['q6','0','R']}],
##                                                               'q5':[{'0':['q5','-','R']},{'1':['q5','-','R']},{'-':['q6','-','R']}],
##                                                               'q6':[{'0':['HALT']},{'1':['HALT']},{'-':['HALT']}]},'q6')




## Defining a TM class first so that it can be passed to the UTM:: M = (States, Input_alphabet, Tape_alphabet, Transition_function, Start_state, Blank_symbol, Finish_state)
        ## @@====================================================================================
        ## Note that the transition function can be predefined and be passed by reference.
        ## It is highly recommended (i.e. don't deviate from this method) to define the transition
        ## function as a dictionary input and it should follow the general form:
        ## {'state':[{'input':['NextState','TapeSymbol','HeadDirection']},{...},{...}...]}
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

        def getBlankSymbol(self):
                return self.blank_sym

## Defining the UTM
## The input, winput, for the UTM is assumed to be of a String data type
class UTM:
        def __init__(self, TM, winput):
                self.winput = list(winput)
                self.states = TM.getStates()
                self.talphabet = TM.getTapeAlphabet()
                self.transition = TM.getTransitionFunction()
                self.start_state = 'q0'
                self.blank = TM.getBlankSymbol()
                self.accept = TM.getAcceptState()
                self.tape = {}
        
        def loadTape(self):
                ## @@Takes: self
                ## @@Returns: Dictionary with keys being int 
                for i in range(len(self.winput)):
                        self.tape[i] = self.winput[i]
                print(self.tape)

        def runUTM(self):
                import collections
                self.loadTape()
                self.current_state = self.start_state
                self.current_input_key = self.tape[0] #current index on tape
                self.next_input_key = ''
                original_input_string_length = len(self.tape)
                halt = False
                head_counter = 0
                while(halt==False):
                        print("Current Input on Tape: "+self.current_input_key)
                        print("Current State of TM: "+self.current_state)
                        transition_row = self.transition[self.current_state]# Looking for which state transition we need given the current state
                        print("Transition Row: "+str(transition_row))
                        try:
                                for item in transition_row:
                                        if self.current_input_key in item: # Looking for the proper transition given our key
                                                self.transition_bloc=item[self.current_input_key]          
##                                print("Transition Bloc: "+str(self.transition_bloc))
                                next_state = self.transition_bloc[0] # Get the next State
                                print("Next State: "+next_state)
                                if next_state == 'HALT' and self.current_state == self.accept:
                                        print("String has been accepted and consumed")
                                        print(self.tape)
                                        halt = True
                                        break
                                elif next_state == 'HALT' and self.current_state != self.accept:
                                        halt = True
                                        print("String cannot be consumed")
                                        break
                                self.current_state = next_state   # Setting the current state to be the next state
                                print("New Symbol to be Written: "+self.transition_bloc[1])
##                                print("Head Counter At: " + str(head_counter))
                                self.tape[head_counter] = self.transition_bloc[1]# Writie this symbol into the current position
                                move_where = self.transition_bloc[2] # Figure out where head moves
##                                print("Moving to the: "+move_where)
                                if move_where == 'R':
                                        head_counter+=1
                                        if head_counter >= original_input_string_length:
                                                self.next_input_key = self.blank
                                        elif head_counter < 0:
                                                self.next_input_key = self.blank
                                        else:
                                                 self.next_input_key= self.tape[head_counter]
                                elif move_where == 'L':
                                        head_counter -=1
                                        if head_counter >= original_input_string_length:
                                                self.next_input_key = self.blank
                                        elif head_counter < 0:
                                                self.next_input_key = self.blank
                                        else:
                                                 self.next_input_key= self.tape[head_counter]
                                        
                                self.current_input_key = self.next_input_key # Move the head to the next position on the tape and make it the current key
                                self.tape = collections.OrderedDict(sorted(self.tape.items())) # Organizing the tape dicitonary
##                                print("Head Counter At: " + str(head_counter))        
                                print("Next Input Key: "+self.current_input_key)
                                print(self.tape)
                                print("Moving On............................")
                        except KeyError:
                                print("Key Error")
                                pass
                        
                print(self.tape)

Modus_TM = TM(['q0','q1','q2','q3','q4','q5','q6'],[0,1,'-'],{'q0':[{'0':['q1','-','R']},{'1':['q5','-','R']},{'-':['HALT']}],
                                                               'q1':[{'0':['q1','0','R']},{'1':['q2','1','R']},{'-':['HALT']}],
                                                               'q2':[{'0':['q3','1','L']},{'1':['q2','1','R']},{'-':['q4','-','L']}],
                                                               'q3':[{'0':['q3','0','L']},{'1':['q3','1','L']},{'-':['q0','-','R']}],
                                                               'q4':[{'0':['q4','0','L']},{'1':['q4','-','L']},{'-':['q6','0','R']}],
                                                               'q5':[{'0':['q5','-','R']},{'1':['q5','-','R']},{'-':['q6','-','R']}],
                                                               'q6':[{'0':['HALT']},{'1':['HALT']},{'-':['HALT']}]},'q6')

modus_utm = UTM(Modus_TM,'000100')
modus_utm.runUTM()

               
        

                
