class Unit:
    def move(self, field, x, y, direction, is_flying, is_sneaking, speed=1):
        if is_flying and is_sneaking:
            raise ValueError('Cannot fly and sneak at the same time')

        if is_flying:
            speed *= 1.2
            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed
        elif is_sneaking:
            speed *= 0.5
            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed
        else:
            if direction == 'UP':
                new_y = y + speed
                new_x = x
            elif direction == 'DOWN':
                new_y = y - speed
                new_x = x
            elif direction == 'LEFT':
                new_y = y
                new_x = x - speed
            elif direction == 'RIGHT':
                new_y = y
                new_x = x + speed

        return field.set_unit(x=new_x, y=new_y, unit=self)


#     ...
