# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube

class Cube:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class CubeVolumeCalculator:
    @staticmethod
    def calc_cube_volume(cube):
        return cube.x * cube.y * cube.z

