def character_xor(input_string, char):
	output_string = ""

	for c in input_string:
		output_string += chr(ord(c)^char)

	return output_string


def calculate_score(input_string):

	frequencies = {
	    'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253, 'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094, 'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
	    'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929, 'q': .00095, 'r': .05987, 's': .06327, 't': .09056, 'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
	    'y': .01974, 'z': .00074, ' ': .13000
	}															

	#frequencies taken from wikipedia

	calculated_sum = 0

	for c in input_string:
		if c in frequencies:
			calculated_sum += frequencies[c]

	return calculated_sum


def main():

	hex_string = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
	decoded_string = bytearray.fromhex(hex_string).decode()

	all_character_xors = []

	for i in range(256):
		char_xor = character_xor(decoded_string, i)
		all_character_xors.append([calculate_score(char_xor.lower()), char_xor])

	all_character_xors.sort()

	print(all_character_xors[-1][1])

main()
