"""
Description: a python implementation of the rules of eliza
Author: Lauren Olson
"""

import re
import random

general_responses = ["tell me more", "okay", "fascinating", "could you explain more"]

def main():
	user_input = input("hello!\n")
	while(1):
		reply = generate_response(user_input)
		user_input = input(reply)


def generate_response(user_input):
	num = random.randint(0, 3)
	ret = general_responses[num]
	makes_you_think = re.match(".*you.*me", user_input)
	if(makes_you_think):

		end = re.search("you.*", user_input)
		end = end.group(0)
		end = end.replace("me", "")
		end = end.replace("you", "")
		ret = "what makes you think I" + end + "you?"
	
	you_are = re.match("[Y|y]ou are.*", user_input)
	if(you_are):
		end = re.search("[Y|y]ou are.*", user_input).group(0)
		end = end[7:]
		ret = "so, I'm " + end + ", am I?"

	
	am_i = re.match(".*am i.*", user_input)
	if(am_i):
		end = re.search("am i.*", user_input)
		end = end.group(0)[4:]
		num = random.randint(0,1)
		l = ["do you believe you are" + end , "why do you ask"]
		ret =  l[num]

	help_you = re.match("i am.*", user_input)
	if(help_you):
		end = re.search("i am.*", user_input).group(0)
		end = end[4:]
		ret = "do you think coming here will help you not to be" + end
		
	
	return ret + "\n"  	


if __name__ == "__main__":
	main()
