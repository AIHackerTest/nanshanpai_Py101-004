people = 30
cars = 40
buses = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")
	
if buses > cars:
    print("That's too many buses.")
elif buses < cars:
    print("Maybe we could take the buses.")
else:
    print("We still can't decide.")
	
if people > buses:
    print("Alright, let's just take the buses.")
else:
    print("Fine, let's stay home then.")
	
	
	
#if elif else，其实是一个组合起来的条件判断语句，如果单独用if 那if也是一个单独的条件判断语句，
#if 和 elif 都是任务的充分条件，而else就是两种条件之外的执行条件，即not(if+elif)