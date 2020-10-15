import abc

class OpenGL(metaclass=abc.ABCMeta):

    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name

    @abc.abstractmethod
    def draw(self,x:int,y:int)->None:...

    @abc.abstractmethod
    def drawLine(self,x1:int,y1:int,x2:int,y2:int)->None:...

    def __repr__(self):
        return f"{type(self)}:{self.id} {self.name}"

class NVidia(OpenGL):

    def __init__(self, id:int):
        #OpenGL.__init__(self,id,"NVidia")
        super().__init__(id,"NVidia")

    def draw(self,x:int,y:int):
        print(f"NVidia({x},{y})")

    def drawLine(self,x1:int,y1:int,x2:int,y2:int):
        print(f"NVidia({x1},{y1})-({x2},{y2})")

    def _specialise(self):
        pass

class Intel(OpenGL):

    def __init__(self, id:int):
        #OpenGL.__init__(self,id,"NVidia")
        super().__init__(id,"Intel")

    def draw(self,x:int,y:int):
        print(f"Intel({x},{y})")

    def drawLine(self,x1:int,y1:int,x2:int,y2:int):
        print(f"Intel({x1},{y1})-({x2},{y2})")

class VideoGame():

    def __init__(self, driver:OpenGL):
        self.driver = driver

    def play(self):
        self.driver.draw(0,0)
        self.driver.drawLine(0,0,10,10)
