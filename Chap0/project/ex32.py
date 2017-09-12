the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list

for number in  the_count:
    print("This is count %r" % number)

# 同上	
for fruit in fruits:
    print("A fruit of type: %s" % fruit)
	
# also we can go through mixed lists too
# notice we hae to use %r since we don't know what's in items

for i in change:
    print("I got %r" % i)

# we can also build lists, first start with an empty one 
elements = []
for i in range (0,6):
    print("ADDING %d to the list." % i)
	#append is a funciton that lists understand
    elements.append(i)
	
	
for i in elements:
    print("Element was: %d" % i)
	
# for循环与list 结合，这个过程就是把list 中的数值赋值依次给 for后面的变量。即循环赋值给变量就可以用for语句来实现


	
