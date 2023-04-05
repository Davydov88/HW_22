# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)

class Unit:
    def __init__(self, field, x, y, is_flying, is_crawling, speed=1):
        self.field = field
        self.x = x
        self.y = y
        self.is_flying = is_flying
        self.is_crawling = is_crawling
        self.speed = speed

    def move(self, direction):
        if self.is_flying and self.is_crawling:
            raise ValueError('Рожденный ползать летать не должен!')

        if self.is_flying:
            self._fly(direction)
        elif self.is_crawling:
            self._crawl(direction)
        else:
            raise ValueError('Юнит должен ползать или летать')

    def _fly(self, direction):
        speed = self.speed * 1.2
        if direction == 'UP':
            self.y += speed
        elif direction == 'DOWN':
            self.y -= speed
        elif direction == 'LEFT':
            self.x -= speed
        elif direction == 'RIGHT':
            self.x += speed
        else:
            raise ValueError(f'Недопустимое направление: {direction}')
        self.field.set_unit(x=self.x, y=self.y, unit=self)

    def _crawl(self, direction):
        speed = self.speed * 0.5
        if direction == 'UP':
            self.y += speed
        elif direction == 'DOWN':
            self.y -= speed
        elif direction == 'LEFT':
            self.x -= speed
        elif direction == 'RIGHT':
            self.x += speed
        else:
            raise ValueError(f'Недопустимое направление: {direction}')
        self.field.set_unit(x=self.x, y=self.y, unit=self)


#     ...
