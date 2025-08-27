class DFA:
    def __init__(self,states,alphabet,transition,start_state,accept_state):
       self.states=states
       self.alphabet=alphabet
       self.transition=transition
       self.start_state=start_state
       self.accept_state=accept_state


    def accepts(self, string):
        current_state = self.start_state
        for symbol in string:
            if symbol not in self.alphabet:
                return False
            current_state = self.transition[current_state].get(symbol)
            if current_state is None:
                return False
        return current_state in self.accept_state
    

states = {'q0', 'q1', 'q2','q3'}
alphabet = {'a', 'b'}
transition = {
    "q0": {'a': 'q1'},
    "q1": {'a': 'q0', 'b': 'q3'}, 
    "q3": {'a': 'q2','b':'q1'},
    "q2": {'b': 'q0', 'a': 'q3'}
}

start_state = "q0"
accept_state = {"q3"}

dfa = DFA(states,alphabet,transition,start_state,accept_state)



print(dfa.accepts("aaab"))  # TRUE
print(dfa.accepts("ababab"))  # TRUE
print(dfa.accepts("ababab"))  # TRUE

print(dfa.accepts("abab"))  # FALSE
print(dfa.accepts("babaa"))  # FALSE
print(dfa.accepts("ababaa"))  # FALSE

