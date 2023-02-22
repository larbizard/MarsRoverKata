from django.test import TestCase
from .models import Planet
from .models import Rover
from .models import Obstacle

from rest_framework.test import APIClient

class RoverTestCase(TestCase):
    def setUp(self):
        planet1 = Planet.objects.create(name="Mars", size=8)
        Rover.objects.create(name="Wall-e", positionX=4, positionY=1, planet=planet1, direction='N')
        Rover.objects.create(name="Armstrong", positionX=8, positionY=1, planet=planet1, direction='N')
        Rover.objects.create(name="Perseverance", positionX=3, positionY=3, planet=planet1, direction='N')
        Obstacle.objects.create(name="TheRock", positionX=3, positionY=5, planet=planet1)

    def test_rover_is_at_edge(self):
        rover = Rover.objects.get(name="Armstrong")
        self.assertTrue(rover.isAtEdge(position=rover.positionX))
        self.assertTrue(rover.isAtEdge(position=rover.positionY))

    def test_rover_is_at_not_edge(self):
        rover = Rover.objects.get(name="Wall-e")
        self.assertFalse(rover.isAtEdge(position=rover.positionX))
        self.assertTrue(rover.isAtEdge(position=rover.positionY))

    def test_move_rover_to_position(self):
        """
            Make the robot move following this sequence lfffrbb starting at position (4, 1) 
            expected destination is (1, 3)
        """

        sequence = "lfffrbb"

        rover = Rover.objects.get(name="Wall-e")
        print(f'Starting position: ({rover.positionX}, {rover.positionY}) direction {rover.direction}')
        rover.followSequence(sequence)

        print(f'Arriving position: ({rover.positionX}, {rover.positionY}) direction {rover.direction}')
        self.assertEqual(rover.positionX, 1)
        self.assertEqual(rover.positionY, 3)
    
    def test_move_rover_to_position_with_obstacle(self):
        """
         Make the robot move following this sequence llffrbb starting at position (3, 3) 
         expected to see obstacle at position (3, 5) after turning left twice and moving forward
        """

        sequence = "llffrbb"

        rover = Rover.objects.get(name="Perseverance")

        # Obstacle is at position (3, 5)

        print(f'Starting position: ({rover.positionX}, {rover.positionY}) direction {rover.direction}')
        rover.followSequence(sequence)

        print(f'Arriving position: ({rover.positionX}, {rover.positionY}) direction {rover.direction}')
        self.assertEqual(rover.positionX, 3)
        self.assertEqual(rover.positionY, 4)

    def test_request_rover_moving(self):
        client = APIClient()
        rover = Rover.objects.get(name="Wall-e")
        response = client.post(f'/move/{rover.pk}', {'sequence': 'lfffrbb'}, format='json')
        assert response.status_code == 200

    def test_request_rover_moving_conflict_with_obstacle(self):
        client = APIClient()
        rover = Rover.objects.get(name="Perseverance")
        response = client.post(f'/move/{rover.pk}', {'sequence': 'llffrbb'}, format='json')
        assert response.status_code == 409