import sys
from optparse import OptionParser

'''
Read input rules file and store all rules in a dictionary
'''
def create_rules(filename):
	d, start_symbol = {}, None
	for line in open(filename, 'r'):
		key, value = line.split()[0], line.split()[2:]

		if start_symbol is None:
			start_symbol = key

		if key in d:
			d[key].append(value)
		else:
			d[key] = [value]

	return (start_symbol, d)


'''
Generate all strings in the language dentoed by the grammar, up to length
Grammars are tuples of:
	a dictionary of rules
	a start symbol
'''
def generate_language(grammar, length):
	start_symbol, rules = grammar[0], grammar[1]
	worklist = [start_symbol]
	non_terminals = rules.keys()

	while worklist:
		s = worklist.pop(0)

		if len(s.replace(' ', '')) <= length:
			leftmost_nonterminal = None 
			for i, char in enumerate(s):
				if char in non_terminals:
					leftmost_nonterminal = char
					leftmost_nonterminal_index = i
			
			if leftmost_nonterminal is None:
				print(s)
			else:
				for prodcution in rules[leftmost_nonterminal]:
					worklist.append(s[:leftmost_nonterminal_index] + ' '.join(prodcution) + s[leftmost_nonterminal_index+1:])


if __name__ == "__main__":
	parser = OptionParser()
	parser.add_option("-l", "--length", dest="length", default = 3, type = "int", help="generate strings up in the language denoted by the grammar up to this length")

	(options, args) = parser.parse_args()

	grammar_file = sys.argv[-1]
	grammar = create_rules(grammar_file)
	print(grammar)
	generate_language(grammar, options.length)