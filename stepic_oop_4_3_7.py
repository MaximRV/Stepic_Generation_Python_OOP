class Gun:
    def __init__(self):
        self.shoot_counter = 0

    def shoot(self):
        self.shoot_counter += 1
        if self.shoot_counter % 2 != 0:
            print('pif')
        else:
            print('paf')

    def shots_count(self):
        return self.shoot_counter

    def shots_reset(self):
        self.shoot_counter = 0

gun = Gun()

print(gun.shots_count())
gun.shoot()
print(gun.shots_count())
gun.shoot()
print(gun.shots_count())