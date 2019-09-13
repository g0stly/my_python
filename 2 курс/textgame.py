import random

class Hero:
    def __init__(self, new_name='Безымянный', x=0, y=0):
        self.name = new_name
        self.x = x
        self.y = y
        self.health = 100
        self.speed = 1
        self.damage = 5
        self.state = 'walking'
        print(f'Игрок под ником "{self.name}" вошел в игру.\nОн находится в клетке с координатами ({self.x}, {self.y}).\n')
    
    
    def move(self, dest_x, dest_y):
        
        if self.x == dest_x and self.y == dest_y:  
            print(f'Игрок "{self.name}" уже давно находится в этой клетке.\n')
        
        else:
            print(f'Игрок "{self.name}" добежал до места назначения за', 
                  round(abs(dest_x - self.x + dest_y - self.y)/self.speed), 'минут.\n')
            self.x = dest_x
            self.y = dest_y
            
    
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
            print('Атака невозможна. Подойдите ближе.')

    
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
            print('Подбирать в этой клетке нечего') 
    



class Flying_Hero(Hero):
    def fly_up(self):
        if self.state == 'walking':
            self.state = 'flying'
            self.speed += 4
            print(f'Игрок под ником "{self.name}" взлетел.\n')
        
        else:
            print(f'"{self.name}" уже в воздухе!\n')

    def fly_down(self):
        if self.state == 'flying':
            self.state = 'walking'
            self.speed += 4
            print(f'Игрок под ником "{self.name}" спустился на землю.\n')
        
        else:
            print(f'"{self.name}" уже на земле!\n')
            

def spawn_items():
    amount = random.randint(1, 5)
    coords = [[random.randint(-15, 15), random.randint(-15, 15)] for i in range(amount)]
    return coords            
                      
            
if __name__ == '__main__':
    items = spawn_items()
    hero1 = Hero('Naruto')
    hero2 = Hero('Sasuke')
    hero3 = Flying_Hero('Deidara')
