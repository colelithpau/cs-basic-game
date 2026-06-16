# Move to the treasure room and defeat all the ogres.
hero.moveUp(4)
hero.moveRight(4)
hero.moveDown(4)
while True:
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.moveUp()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.moveLeft(2)
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    
    
    







