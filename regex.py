from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):
    def __init__(self) -> None:
        self.next_states: list[State] = []

    @abstractmethod
    def check_self(self, char: str) -> bool:
        """
        Function checks whether the current character is handled by the current state.
        """
        pass

    def check_next(self, char: str) -> list[State]:
        """
        Returns a list of next possible states based on the input character.
        """
        valid_states = []
        for state in self.next_states:
            if state.check_self(char):
                valid_states.append(state)
        return valid_states

    @abstractmethod
    def name(self) -> str:
        """
        Returns the name of the current state for debugging purposes.
        """
        pass


class StartState(State):
    def __init__(self):
        super().__init__()

    def check_self(self, char: str) -> bool:
        return False

    def name(self) -> str:
        return "StartState"


class TerminationState(State):
    # Implement

    def __init__(self):
        super().__init__()

    def check_self(self, char: str) -> bool:
        return False
    def name(self) -> str:
        return "TerminationState"


class DotState(State):
    def __init__(self):
        super().__init__()
# Implement
    def check_self(self, char: str) -> bool:
        return True
# Implement
    def name(self) -> str:
        return "DotState"


class AsciiState(State):
    # Implement
    def __init__(self, symbol: str) -> None:
        super().__init__()
        self.curr_sym = symbol
# Implement
    def check_self(self, curr_char: str) -> bool:
        return self.curr_sym == curr_char
# Implement
    def name(self) -> str:
        return f"AsciiState({self.curr_sym})"


class StarState(State):
     # Implement
    def __init__(self, checking_state: State):
        super().__init__()
        self.checking_state = checking_state
        self.next_states.append(self)
        self.next_states.extend(checking_state.next_states)  # Can skip to next states

    def check_self(self, char: str) -> bool:
        return self.checking_state.check_self(char)

    def name(self) -> str:
        return f"StarState({self.checking_state.name()})"


class PlusState(State):
    
    def __init__(self, checking_state: State):
        super().__init__()
        self.checking_state = checking_state
        self.next_states.append(self)
        self.next_states.extend(checking_state.next_states)  # Can transition forward after repetition

    def check_self(self, char: str) -> bool:
        return self.checking_state.check_self(char)

    def name(self) -> str:
        return f"PlusState({self.checking_state.name()})"


class RegexFSM:
    def __init__(self, regex_expr: str) -> None:
        self.start_state: State = StartState()
        self.termination_state = TerminationState()
        self.states = [self.start_state]

        prev_state = self.start_state
        star_state = False

        for char in regex_expr:
            tmp_next_state = self.__init_next_state(char, prev_state)        
            if star_state == True:
                star_state = False
                self.start_state.next_states.append(tmp_next_state)
            if char == '*' :
                self.states.pop()
                self.start_state.next_states.pop()
            #self.start_state.next_states.pop()
                star_state= True
                self.start_state.next_states.append(tmp_next_state)
  
            #prev_state = tmp_next_state
            prev_state.next_states.append(tmp_next_state)
            prev_state = tmp_next_state
            self.states.append(tmp_next_state)                 

 
        prev_state.next_states.append(self.termination_state)
# Implement
    def __init_next_state(self, next_token: str, prev_state: State) -> State:
        if next_token == ".":
            return DotState()
        elif next_token == "*":
            if not self.states:
                raise ValueError("Invalid use of '*' operator.")
            return StarState(prev_state)
        elif next_token == "+":
            if not self.states:
                raise ValueError("Invalid use of '+' operator.")
            return PlusState(prev_state)
        elif next_token.isascii():
            return AsciiState(next_token)
        else:
            raise AttributeError(f"Character '{next_token}' is not supported")
# Implement
    def check_string(self, input_string: str) -> bool:
        current_states = [self.start_state]

        for char in input_string:
            print(f"Processing character: '{char}'")
            next_states = []
            for state in current_states:
                print(f"  Current state: {state.name()}")
                next_states.extend(state.check_next(char))

            if not next_states:
                print("  No valid transitions found. String rejected.")
                return False

            current_states = next_states
            print(f"  Next states: {[state.name() for state in current_states]}")

        # Check if any state can reach the termination state
        is_accepted = any(self.termination_state in state.next_states for state in current_states)
        print("String accepted." if is_accepted else "String rejected.")
        return is_accepted

    def print_states(self):
        print("RegexFSM States and Transitions:")
        for state in self.states:
            next_state_names = [s.name() for s in state.next_states]
            print(f"  {state.name()} -> {next_state_names}")
        print(f"  {self.termination_state.name()} -> []")


if __name__ == "__main__":
    regex_pattern = "a*4.+hi"

    regex_compiled = RegexFSM(regex_pattern)

    # Print the FSM states and transitions
    regex_compiled.print_states()

    # Test strings
    print(regex_compiled.check_string("aaaaaa4uuhi"))  # True
    print(regex_compiled.check_string("4uuhi"))  # True
    print(regex_compiled.check_string("meow"))  # False
