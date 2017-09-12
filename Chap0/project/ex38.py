ten_things = "Apples oranges Crows Telephone Light Sugar"
print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() #删除最后一个元素并输出
    print ("Adding: ",next_one)
    stuff.append(next_one)
    print("There's %d items now." % len(stuff))
    
print("There we go: ",stuff)

print("Let's do some things with stuff.")

print (stuff[1])
print (stuff[-1])
print (stuff.pop())
print (' '.join(stuff))  #用''中定义的字符联结元素
print ('#'.join(stuff[3:5]))


#主要是针对列表的炒作  
