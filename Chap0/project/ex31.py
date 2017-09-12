print("You enter a dark room with two doors.",)
print("Do you go through door #1 or door #2?")

i = input(">")

if i == "1":
    print("""There's giant bear here eating a cheese cake. What do you do 
             1. Take the cake.
             2. Scream at the bear.
""")
    n = input(">") 
    if n == "1":
	    print("The bear eats your face off. Good job!")
    elif n == "2":
	    print("The bear eats your legs off. Good job!")
    else:
	    print("Well, doing %s is probably better. Bear runs away." % bear)

elif i == "2":

    print("""You strae into the endless abyss at Cthulhu's retina.
             1. Blueberries.
             2. Yellow jacket clothespins.
             3. Understanding revolvers yelling melodies.
""")
    insanity = input(">")
	
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")
		
	
else:
    print("You stumble around and fall on a knife and die. Good job!")
	
# 缩进多纯在与模块之间，如if else 中，只要是控制语句之内的语句都要缩进。