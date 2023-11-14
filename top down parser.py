class SimpleParser:
    def __init__(self, grammar):
        self.grammar = grammar

    def parse(self, input_string):
        self.tokens = input_string.split()
        self.current_token_index = 0

        try:
            self.parse_sentence()
            print("Parsing successful!")
        except ValueError as e:
            print(f"Parsing failed: {e}")

    def match(self, expected_token):
        if self.current_token_index < len(self.tokens) and self.tokens[self.current_token_index] == expected_token:
            self.current_token_index += 1
        else:
            raise ValueError(f"Expected '{expected_token}', found '{self.tokens[self.current_token_index]}'")

    def parse_sentence(self):
        self.parse_subject()
        self.match('VERB')
        self.parse_object()

    def parse_subject(self):
        self.match('NOUN')

    def parse_object(self):
        self.match('NOUN')

# Example usage
grammar = {
    'SENTENCE': [['SUBJECT', 'VERB', 'OBJECT']],
    'SUBJECT': [['NOUN']],
    'OBJECT': [['NOUN']],
}

parser = SimpleParser(grammar)
parser.parse("cat VERB dog")
