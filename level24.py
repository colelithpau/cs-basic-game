# Use a while-true loop to both move and attack.

while True:
    hero.moveRight()
    hero.moveUp()
    hero.moveRight()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.moveDown(2)
    hero.moveUp()
    
    
