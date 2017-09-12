class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
                   
bulls_on_parade = Song(["They rally around the family",
                         "With pockets full of shells"])
                         
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

#有一个类是Song 他有一对象是object,这个对象的属性是self.    他执行的动作在def 函数定义中
#而属性定义在函数__init__,用self 的意图是为了区分变量和属性。