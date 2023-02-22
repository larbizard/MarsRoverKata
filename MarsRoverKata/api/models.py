from django.db import models
from django.core.exceptions import FieldError


class Planet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    size = models.IntegerField() # The size is the integer that defines the amount of latitudes and longitudes of the planet


class Rover(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    positionX = models.IntegerField()
    positionY = models.IntegerField()
    direction = models.CharField(max_length=1)
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)

    def getNextPosition(self, forward):
        if forward:
            if self.direction == 'N':
                if self.positionY == 1:
                    return (self.positionX, self.positionY)
                else:
                    return (self.positionX, self.positionY - 1)

            elif self.direction == 'S':
                if self.positionY == self.planet.size:
                    return (self.positionX, self.positionY)
                else:
                    return (self.positionX, self.positionY + 1)

            elif self.direction == 'E':
                if self.positionX == self.planet.size:
                    return (1, self.positionY)
                else:            
                    self.positionX = self.positionX + 1
                    return (self.positionX + 1, self.positionY)

            elif self.direction == 'W':
                if self.positionX == 1:
                    return (self.planet.size, self.positionY)
                else:
                    return (self.positionX - 1, self.positionY)        
            else:
                raise FieldError
        else:
            if self.direction == 'N':
                if self.positionY == self.planet.size:
                    return (self.positionX, self.positionY)
                else:
                    return (self.positionX, self.positionY + 1)

            elif self.direction == 'S':
                if self.positionY == 1:
                    return (self.positionX, self.positionY)
                else:
                    return (self.positionX, self.positionY - 1)

            elif self.direction == 'E':
                if self.positionX == 1:
                    return (self.planet.size, self.positionY)
                else:
                    return (self.positionX - 1, self.positionY)

            elif self.direction == 'W':
                if self.positionX == self.planet.size:
                    return (1, self.positionY)
                else:
                    return (self.positionX + 1, self.positionY)
            else:
                raise FieldError

    def checkForObstacle(self, coordinates):
        if len(Obstacle.objects.filter(positionX=coordinates[0], positionY=coordinates[1])) >= 1:
            return True
        else:
            return False

    def followSequence(self, sequence):
        for s in sequence:
            print(f'Current position: ({self.positionX}, {self.positionY}) direction {self.direction}')
            if s == 'l':
                self.turnLeft()
            elif s == 'r':
                self.turnRight()
            elif s == 'f':
                if not self.moveForward():
                    return False
            elif s == 'b':
                if not self.moveBackward():
                    return False
            else:
                raise FieldError
        return True

    def moveForward(self):
        print('Moving Forward')
        (x, y) = self.getNextPosition(True)
        if self.checkForObstacle((x, y)):
            print(f'Warning obstacle detected at position ({x}, {y}) aborting sequence!')
            return False
        else:
            self.positionX = x
            self.positionY = y
            return True


            
    def moveBackward(self):
        print('Moving Backward')
        (x, y) = self.getNextPosition(False)
        if self.checkForObstacle((x, y)):
            print(f'Warning obstacle detected at position ({x}, {y}) aborting sequence!')
            return False
        else:
            self.positionX = x
            self.positionY = y
            return True


    def turnLeft(self):
        print('Turning Left')
        if self.direction == 'N':
            self.direction = 'W'

        elif self.direction == 'S':
            self.direction = 'E'

        elif self.direction == 'E':
            self.direction = 'N'

        elif self.direction == 'W':
            self.direction = 'S'
        else:
            raise FieldError

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

    def isAtEdge(self, position):
        if position == self.planet.size or position == 1:
            return True
        return False

class Obstacle(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    positionX = models.IntegerField()
    positionY = models.IntegerField()
    planet = models.ForeignKey(Planet, on_delete=models.CASCADE)