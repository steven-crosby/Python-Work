"""
CS241 MELLOR
STUDENT: Steven Crosby
ASSIGNMENT: Asteroids

Week 08 MILESTONE:
[ ] Create the classes and subbed out functions
[ ] Get large asteroid to display and move

WEEK 09 MILESTONE:
[ ] Show the ship correctly moving
[ ] Bullets being fired correctly
[ ] Wrapping around screen edges for the ship, bullets, and rocks
[ ] Completely implemented the Velocity and FlyingObject classes.

WEEK 10 MILESTONE:
[ ] Collisions between bullets and rocks
[ ] Collisions between the ship and rocks
[ ] Rocks correctly breaking apart when hit
[ ] Lists correctly cleaned up when rocks and/or bullets are destroyed


CLASSES
1. Point
2. Velocity
3. FlyingObjects
4. StarShip
5. SmallRock
6. MediumRock
7. LargeRock
8. Bullet
9. Game

"""
import arcade
import random
import math


# INITIALIZATION OF POINT. USED FOR: STARSHIP, SHIPSHIELD, BULLETS, ROCKS
class Point:
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y


# INITIALIZATION OF VELOCITY. USED FOR: STARSHIP, SHIPSHIELD, BULLETS, ROCKS
class Velocity:
    def __init__(self, init_dx, init_dy):
        self.dx = init_dx
        self.dy = init_dy


# EXECUTES START POINT FOR ROCKS AND THEIR TRAVEL ANGLE
class AsteroidAngle:
    def __init__(self):
        pass

    @staticmethod
    def execute_angle(start):
        """
        The object will pass  in random start number
        This number will decide which side of the screen the
        astroid will spawn at.

        This function will return an appropriate angle
        that the astroid should start will with.
        """

        # LEFT
        if start == 1:
            return random.randint(-30, 30)
        # RIGHT
        elif start == 2:
            return random.randint(150, 210)
        # BOTTOM
        elif start == 3:
            return random.randint(60, 120)
        # TOP
        else:
            return random.randint(240, 300)
