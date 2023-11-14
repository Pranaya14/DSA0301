class PluralizationStateMachine:
    def __init__(self):
        self.current_state = "q0"
        self.result = ""
        
    def transition(self, input_symbol):
        if self.current_state == "q0":
            if input_symbol == "s":
                self.current_state = "q1"
                self.result += input_symbol
            elif input_symbol == "y":
                self.current_state = "q2"
                self.result += input_symbol
            else:
                self.result += input_symbol
        elif self.current_state == "q1":
            if input_symbol == "e":
                self.current_state = "q3"
                self.result += input_symbol
            else:
                self.result += input_symbol
        elif self.current_state == "q2":
            self.result += input_symbol
            if input_symbol == "s":
                self.current_state = "q4"
                self.result += input_symbol
            else:
                self.current_state = "q0"
        elif self.current_state == "q3":
            self.result += input_symbol
            if input_symbol == "s":
                self.current_state = "q4"
                self.result += input_symbol
            else:
                self.current_state = "q0"
        else:
            self.result += input_symbol
            self.current_state = "q0"

    def generate_plural(self, singular_noun):
        self.result = ""
        self.current_state = "q0"
        
        for symbol in singular_noun:
            self.transition(symbol)
        
        if self.current_state == "q3":
            # Pluralize by changing "y" to "ies"
            self.result = self.result[:-1] + "ies"
        elif self.current_state == "q4":
            # Pluralize by adding "es"
            self.result += "es"
        else:
            # Default pluralization by adding "s"
            self.result += "s"
        
        return self.result

# Test the pluralization
singular_nouns = ["cat", "dog", "city", "baby", "bus", "box", "story"]

pluralizer = PluralizationStateMachine()
for noun in singular_nouns:
    plural_form = pluralizer.generate_plural(noun)
    print(f"Singular: {noun}, Plural: {plural_form}")
