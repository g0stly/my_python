#  выполнили Зотов и Ерофеевский


import random, math

class Hero:
    def __init__(self, new_name='Безымянный'):
        self.name = new_name
        self.x = random.randint(-100, 100)
        self.y = random.randint(-100, 100)
        self.health = 100
        self.speed = 1
        self.damage = 5
        self.state = 'walking'
        print(f'Игрок под ником "{self.name}" вошел в игру.\nОн находится в клетке с координатами ({self.x}, {self.y}).')
    
    
    def move(self, dest_x, dest_y):
        
        if self.x == dest_x and self.y == dest_y:  
            print(f'Игрок "{self.name}" уже давно находится в этой клетке. ({self.x}, {self.y})')
        
        else:
            print(f'Игрок "{self.name}" добежал до места назначения за', 
                  round(abs(dest_x - self.x) + abs(dest_y - self.y)/self.speed), f'минут. ({dest_x}, {dest_y})')
            self.x = dest_x
            self.y = dest_y
        if [self.x, self.y] in items:
            print('В этой ячейке есть бонус!')
            
    
    def attack(self, victim):
        
        if abs(self.x - victim.x + self.y - victim.y) <= 1:
            
            if self.state == 'walking' and victim.state == 'flying':
                victim.health -= self.damage*random.randint(0, 1)
            
            else:
                victim.health -= self.damage
            
            if victim.health <= 0: 
                print(f'Игрок "{self.name}" убил игрока "{victim.name}".\nПокойся с миром.')
            
            else: 
                print(f'Игрок "{victim.name}" атакован.\nЕго здоровье:', victim.health )
        
        else:
            print(f'Атака невозможна. Подойдите ближе. ({self.x}, {self.y})')

    
    def pick_up(self):
        
        if [self.x, self.y] in items:
            buff = random.choice(['Зелье скорости', 'Яд', 'Зелье здоровья'])
            
            if buff == 'Зелье скорости':
                self.speed *= 2
                print(f'Скорость игрока "{self.name}" увеличилась в 2 раза.')
            
            elif buff == 'Яд':
                self.health -= 50
                
                if self.health <= 0: 
                    print(f'Игрок "{self.name}" умер от яда.\nПокойся с миром.')
                else:
                    print(f'Игрок "{self.name}" отравился.\nЕго здоровье: {self.health} единиц.')
            
            else:
                self.health = 100  
                print(f'Здоровье игрока "{self.name}" восстановлено до 100 единиц.')
                
            items.remove([self.x, self.y])
        
        else:
            print(f'Подбирать в этой клетке нечего. ({self.x}, {self.y})') 
    

    def nearest_bonus(self):
        try:
            item = min(items, key = lambda x: distance(x, [self.x, self.y]))
            print(f'Ближайший к игроку "{self.name}" бонус находится в клетке {item[0], item[1]}.')
        except:
            print('Все бонусы подобраны.')


class Flying_Hero(Hero):
    def fly_up(self):
        if self.state == 'walking':
            self.state = 'flying'
            self.speed += 4
            print(f'Игрок под ником "{self.name}" взлетел.')
        
        else:
            print(f'"{self.name}" уже в воздухе!')

    def fly_down(self):
        if self.state == 'flying':
            self.state = 'walking'
            self.speed -= 4
            print(f'Игрок под ником "{self.name}" спустился на землю.')
        
        else:
            print(f'"{self.name}" уже на земле!')
            

def spawn_items():
    amount = random.randint(1, 5)
    coords = [[random.randint(-15, 15), random.randint(-15, 15)] for i in range(amount)]
    coords.append([33, 33])
    return coords


def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1]- b[1])
                      
            
if __name__ == '__main__':
    items = spawn_items()
    hero1 = Hero('Саша')
    hero2 = Flying_Hero('Аркаша')
    hero2.fly_up()
    hero2.move(33, 33)
    hero2.pick_up()
    hero1.move(32,32)
    hero1.attack(hero2)
    hero1.move(32,33)
    hero1.attack(hero2)





