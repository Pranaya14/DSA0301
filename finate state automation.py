def ends_with_ab(input_string):
    # Define the states
    states = {
        'q0': {'a': 'q1', 'b': 'q0'},
        'q1': {'a': 'q1', 'b': 'q2'},
        'q2': {'a': 'q1', 'b': 'q0'},
    }
    
    current_state = 'q0'
    
    for char in input_string:
        if char not in states[current_state]:
            return False
        current_state = states[current_state][char]
    
    return current_state == 'q2'

# Test the automaton
test_strings = ["ab", "aab", "abb", "abab", "ba", "abc"]
for test_string in test_strings:
    if ends_with_ab(test_string):
        print(f"'{test_string}' matches the pattern.")
    else:
        print(f"'{test_string}' does not match the pattern.")
