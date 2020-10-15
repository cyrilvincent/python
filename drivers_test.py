import unittest
import drivers
import numpy
import config
import jsonpickle

class DriversTest(unittest.TestCase):

    def testDriver(self):
        with self.assertRaises(TypeError):
            driver = drivers.OpenGL(0,"Toto")
        driver1 = drivers.NVidia(1)
        driver2 = drivers.Intel(2)


    def testVideoGame(self):
        vg = drivers.VideoGame(config.DRIVER)
        vg.play()
        vg = drivers.VideoGame(eval(config.DRIVER2))
        vg.play()
        with open("videogame.json","w") as f:
            json = jsonpickle.encode(vg)
            f.write(json)
