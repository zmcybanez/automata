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
    

states = {'a', 'b', 'c'}
alphabet = {'0', '1'}
transition = {
    "a": {'0': 'a', '1': 'b'},
    "b": {'0': 'c', '1': 'a'}, 
    "c": {'1': 'c'}     
}

start_state = "a"
accept_state = {"c"}

dfa = DFA(states,alphabet,transition,start_state,accept_state)



print(dfa.accepts("10"))  # TRUE
print(dfa.accepts("101"))  # TRUE
print(dfa.accepts("1011"))  # TRUE

print(dfa.accepts("00100"))  # FALSE
print(dfa.accepts("11001"))  # FALSE
print(dfa.accepts("10010"))  # FALSE

