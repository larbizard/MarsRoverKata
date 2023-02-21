from django.db import models

class Rover(models.Model):
    DIRECTION = [
        ('N', 'North'),
        ('S', 'South'),
        ('E', 'East'),
        ('W', 'West')
    ]
    id = models.AutoField()
    name = models.CharField(max_length=50)
    positionX = models.FloatField()
    positionY = models.FloatField()
    direction = models.CharField(choices=DIRECTION)

    def moveForward(self):
        print('Moving Forward')
        if self.direction == 'N':
            self.positionY = self.positionY - 1

        if self.direction == 'S':
            self.positionY = self.positionY + 1

        if self.direction == 'E':
            self.positionX = self.positionX + 1

        if self.direction == 'W':
            self.positionX = self.positionX - 1            

    def moveBackward(self):
        print('Moving Backward')
        if self.direction == 'N':
            self.positionY = self.positionY + 1

        if self.direction == 'S':
            self.positionY = self.positionY - 1

        if self.direction == 'E':
            self.positionX = self.positionX - 1

        if self.direction == 'W':
            self.positionX = self.positionX + 1        

    def turnLeft(self):
        print('Turning Left')
        if self.direction == 'N':
            self.direction = 'W'

        if self.direction == 'S':
            self.direction = 'E'

        if self.direction == 'E':
            self.direction = 'N'

        if self.direction == 'W':
            self.direction = 'S'


    def turnRight(self):
        print('Turning Right')
        if self.direction == 'N':
            self.direction = 'E'

        if self.direction == 'S':
            self.direction = 'W'

        if self.direction == 'E':
            self.direction = 'S'

        if self.direction == 'W':
            self.direction = 'N'

class Obstacle(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=50)
    positionX = models.FloatField()
    positionY = models.FloatField()