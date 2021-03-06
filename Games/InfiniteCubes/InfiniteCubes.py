"""
Infinite Cubes Game
"""

# Imports
import random
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Main Vars
VERTICES = (
    (1, -1, -1), 
    (1, 1, -1), 
    (-1, 1, -1), 
    (-1, -1, -1), 
    (1, -1, 1), 
    (1, 1, 1), 
    (-1, -1, 1), 
    (-1, 1, 1)
)
EDGES = (
    (0, 1), 
    (0, 3), 
    (0, 4), 
    (2, 1), 
    (2, 3), 
    (2, 7), 
    (6, 3), 
    (6, 4), 
    (6, 7), 
    (5, 1), 
    (5, 4), 
    (5, 7)
)
SURFACES = (
    (0, 1, 2, 3), 
    (3, 2, 7, 6), 
    (6, 7, 5, 4), 
    (4, 5, 1, 0), 
    (1, 5, 7, 2), 
    (4, 0, 3, 6)
)
COLORS = (
    (1, 0, 0), 
    (0, 1, 0), 
    (0, 0, 1), 
    (1, 0, 0), 
    (1, 1, 1), 
    (0, 1, 1), 
    (1, 0, 0), 
    (0, 1, 0), 
    (0, 0, 1), 
    (1, 0, 0), 
    (1, 1, 1), 
    (0, 1, 1)
)
GROUND_VERTICES = (
    (-10, -1.1, 20), 
    (10, -1.1, 20), 
    (-10, -1.1, -300), 
    (-10, -1.1, -300)
)

# Main Functions
# Object Functions
def Object_Ground():
    glBegin(GL_QUADS)
    for vertex in GROUND_VERTICES:
        glColor3fv((0, 0.5, 0.5))
        glVertex3fv(vertex)
    glEnd()

def Object_Cube(vertices):
    glBegin(GL_QUADS)
    for surface in SURFACES:
        color_index = 0
        for vertex in surface:
            glColor3fv(COLORS[color_index])
            glVertex3fv(vertices[vertex])
            color_index += 1
    glEnd()

    glBegin(GL_LINES)
    for edge in EDGES:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# Set Functions
def SetVertices(generateBounds, max_distance, min_distance=20, camera_x=0, camera_y=0):
    camera_x = -1*int(camera_x)
    camera_y = -1*int(camera_y)
    
    x_value_change = random.randrange(camera_x - generateBounds[0], camera_x + generateBounds[0])
    y_value_change = random.randrange(camera_y - generateBounds[1], camera_y + generateBounds[1])
    z_value_change = random.randrange(-1 * max_distance, -1 * min_distance)

    new_vertices = []

    for vertex in VERTICES:
        new_vertex = []

        new_x = vertex[0] + x_value_change
        new_y = vertex[1] + y_value_change
        new_z = vertex[2] + z_value_change

        new_vertex.append(new_x)
        new_vertex.append(new_y)
        new_vertex.append(new_z)
        
        new_vertices.append(new_vertex)

    return new_vertices

def main(x_speed, y_speed, z_speed, n_cubes, max_distance, min_distance, generateBounds, displayObj=print):
    # Params
    display = (800, 600)
    # Params

    # Init
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(
        45,  # FOV in degrees
        display[0] / display[1], # Aspect Ratio - Width / Height
        0.1, max_distance # Clipping Plane
    )
    glTranslatef(0, 0, -40) # Translate Initial Looking Position
    # glRotatef(25, 2, 1, 0) # Initial Rotation

    # Create the cubes dict
    cube_dict = {}
    for x in range(n_cubes):
        cube_dict[x] = SetVertices(generateBounds, max_distance, min_distance)

    # Start
    x_move = 0
    y_move = 0
    cur_x = 0
    cur_y = 0
    PASSED_COUNT = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    x_move = x_speed
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    x_move = -x_speed
                if event.key in [pygame.K_UP, pygame.K_w]:
                    y_move = -y_speed
                if event.key in [pygame.K_DOWN, pygame.K_s]:
                    y_move = y_speed
            if event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_a]:
                    x_move = 0
                if event.key in [pygame.K_RIGHT, pygame.K_d]:
                    x_move = 0
                if event.key in [pygame.K_UP, pygame.K_w]:
                    y_move = 0
                if event.key in [pygame.K_DOWN, pygame.K_s]:
                    y_move = 0 
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     if event.button == 4:
            #         glTranslate(0, 0, 1.0)
            #     if event.button == 5:
            #         glTranslate(0, 0, -1.0)

        # glRotatef(1, 1, 1, 1) # Rotate Animation
        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]
        cur_x += x_move
        cur_y += y_move
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # Clearing screen at each frame to repaint
        glTranslate(x_move, y_move, z_speed)
        # Object_Ground()
        # Generate Cubes
        for cube in cube_dict:
            Object_Cube(cube_dict[cube])
        # Delete Out of Vision Cubes
        for cube in cube_dict:
            if camera_z <= cube_dict[cube][0][2]:
                PASSED_COUNT += 1
                displayObj("Passed " + str(PASSED_COUNT) + " cubes!")
                new_max = int(-1*(camera_z - (max_distance*generateBounds[2])))
                cube_dict[cube] = SetVertices(generateBounds, new_max, int(camera_z), cur_x, cur_y)

        pygame.display.flip()
        pygame.time.wait(10)

# # Driver Code
# # Params
# max_distance = 100
# min_distance = 20
# n_cubes = 25

# x_speed = 0.3
# y_speed = 0.3
# z_speed = 2

# # x and y are distance from camera pos to generate
# # z is multiplied with max_distance for generation
# generateBounds = (25, 25, 2) 

# # Params