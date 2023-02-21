from django.db import models

class Rover:
    DIRECTION = [
        ('N', 'North'),
        ('S', 'South'),
        ('E', 'East'),
        ('W', 'West')
    ]
    id = models.AutoField()
    name = models.CharField(max_length=50)
    latitude = models.FloatField()
    longitude = models.FloatField()
    direction = models.CharField(choices=DIRECTION)

    def moveForward():
        print('Moving Forward')

    def moveBackward():
        print('Moving Forward')

    def turnLeft():
        print('Turning Left')

    def turnRight():
        print('Turning Right')