# в задании представлен один класс который нужно разбить на 4
# Воин      - Warrior
# Лекарь    - Healer
# Дерево    - Tree
# Ловушка   - Trap

# Воин в состоянии защищаться от врагов, атаковать и передвигаться по полю
# Лекарь может защищаться, лечить воина и панически спасаться бегством
# Дерево может защищаться (попробуй разруби сходу) и гореть в огне
# Ловушка не может ничего кроме как атаковать того, кто на нее наступит
# Для решения этой задачи не используйте наследование

class Warrior:
    def init(self):
        self.health = 100

    def attack(self):
        print("Warrior attacks")

    def defense(self):
        print("Warrior defends")

    def move(self):
        print("Warrior moves")

class Healer:
    def init(self):
        self.health = 50

    def attack(self):
        print("Healer can't attack")

    def defense(self):
        print("Healer defends")

    def move(self):
        print("Healer runs away")

    def healer_defense(self):
        print("Healer can defend himself")

    def healer_move(self):
        print("Healer can move")

    def heal(self, warrior):
        warrior.health += 10
        print(f"Healer heals warrior. Warrior's health: {warrior.health}")


class Tree:
    def init(self):
        self.health = 200

    def attack(self):
        print("Tree can't attack")

    def defense(self):
        print("Tree defends")

    def move(self):
        print("Tree can't move")

    def tree_defense(self):
        print("Tree can defend itself")

    def on_fire(self):
        self.health -= 20
        print(f"Tree is on fire. Tree's health: {self.health}")


class Trap:
    def init(self):
        self.damage = 30

    def attack(self):
        print("Trap can't attack")

    def defense(self):
        print("Trap can't defend")

    def move(self):
        print("Trap can't move")

    def trap_attack(self):
        print(f"Trap attacks. Damage: {self.damage}")


if __name__ == '__main__':
    unit = Warrior()
    healer = Healer()
    tree = Tree()
    trap = Trap()
