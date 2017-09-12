from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
	
    next = input('>')
    if "0" in next or "1" in next:
	    how_much = int(next)
    else:
	    dead("Man, learn to type a number.")
		
    if how_much < 50:
	    print("Nice, you're not greedy,you win!")
	    exit(0)
    else:
	    dead("You greedy bastard!")
		
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
	
    while True:
	    next = input(">")
	    if next == "take honey":
		    dead("The bear looks at you then slaps your face off.")
	    elif next == "taunt bear" and not bear_moved:
		    print("The bear has move from the door.You can go through it now.")
		    bear_moved = True
	    elif next == "taunt bear" and bear_moved:
		    dead("The bear getst pissed off and chews your leg off.")
	    elif next == "open door" and bear_moved:
		    gold_room()
	    else:
		    print("I got no idea what that means.")
			
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
	
    next = input(">")
	
    if "flee" in next:
	    start()
    elif "head" in next:
	    dead("Well that was tasty!")
    else:
	    cthulhu_room()
		
def dead(why):
    print(why, "Good job!")
    exit(0)
	
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
	
    next = input(">")
	
    if next == "left":
	    bear_room()
    elif next == "right":
	    cthulhu_room()
    else:
	    dead("You stumble around the room until you starve.")
		
start()

# 这么多分支有控制语句很难控制，所以用函数定义决策场景，然后可以穿插调用，而且所有函数内部函数名称都用next而不相互影响。外部输入变量名称不同
# 涉及重复执行的都可以用WHILE语句实现，exit()函数可以从程序任意退出程序。  if in 语句  与for  in  语句类似 还以为只能用于for语句呢