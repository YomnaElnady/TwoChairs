from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import numpy as np

def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

def CompleteChair():

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1,.7,.8)
    glScale(2.9,0.5,2.5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, .7, .8)
    glTranslate(0,2.5,-3)
    glScale(3,2.6,0.5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, .7, .8)
    glTranslate(3, -2, -1.5)
    glScale(0.5,3,0.5 )
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, .7, .8)
    glTranslate(-3, -4, -3)
    glScale(0.5,4, 0.5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, .7, .8)
    glTranslate(-2,-3,2.3)
    glScale(0.5, 3, 0.5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1, .7, .8)
    glTranslate(2.7, -3, 2.3)
    glScale(0.5, 3, 0.5)
    glutWireCube(2)
    glPopAttrib()
    glPopMatrix()





def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    CompleteChair()
    glTranslate(-8,0,0)
    CompleteChair()
    glFlush()




glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"chair")
glutInitWindowSize(700,700)
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()