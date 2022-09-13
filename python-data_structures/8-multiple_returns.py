#!/usr/bin/python3
def multiple_returns(sentence):
	size = len(sentence)
	if size == 0:
		tmp = None
	else:
		tmp = sentence[0]
	return ((size, tmp))