hero.moveRight(3)

# You should recognize this from the last level.
enemy1 = hero.findNearestEnemy()
hero.attack(enemy1)
enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)
hero.moveDown()
# Now attack enemy1.
hero.moveRight(2)
hero
