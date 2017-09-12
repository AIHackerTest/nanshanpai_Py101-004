#关于列表 编程 中位置是从0 开始的比如 animals = ['bear', 'tiger', 'penguin', 'zebra']  bear 提取位置为animals[0] 
#而从序数角度讲bear是一个动物。

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

i = 0

while i < 6:
    
    print("cardinal number %d is the list %r:" % (i,animals[i]))
    i += 1
	
    print("ordianl number %d is the list %r:" % (i,animals[i-1]))