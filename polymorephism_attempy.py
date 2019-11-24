#!/home/aaron4udemy/anaconda3/envs/udem/bin/python
class Square():
    def __init__(self, side=2):
        self.side = side

    def __pow__(self, s2):
        return self.side ** s2.side


s1 = Square()
s2 = Square(3)
print(str(s1 ** s2))
