## Author: Paul Kiripolsky
## Class: CS 125, UVM Spring 2015
## Project: Universal Turing Machine Challenge


## Defining a TM class first so that it can be passed to the UTM
class TM:
	def __init__(self, states, tape_alpha, transition_func, finish_state):
		self.states = states
		self.input_alpha = [0,1]
		self.tape_alpha = tape_alpha
		self.transition_func = transition_func
		self.start_state = 'q0' #in the definition of this TM and UTM, I will always use q0 as a start state
		self.blank_sym = "/"
		self.finish_state = finish_state

