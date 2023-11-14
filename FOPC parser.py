from pyparsing import Word, alphas, infixNotation, opAssoc

# Define logical operators
and_op = "and"
or_op = "or"
not_op = "not"

# Define logical variables
variable = Word(alphas)

# Define the FOPC grammar
expr = infixNotation(variable,
                    [(not_op, 1, opAssoc.RIGHT),
                     (and_op, 2, opAssoc.LEFT),
                     (or_op, 2, opAssoc.LEFT)])

# Parse FOPC expressions
result = expr.parseString("A and B or not C")
print(result[0])
