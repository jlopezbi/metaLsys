import rhinoscriptsyntax as rs
from lsystems import Rule, expand

a = 10
s = .5

@Rule
def roll(a):
  pass

@Rule 
def pitch(a):
  pass

@Rule
def yaw(a):
  pass

@Rule
def PushState():
  pass

@Rule
def PopState():
  pass

@Rule
def A(l):
  return [ 
    F(l),
    PushState(),
    yaw(a),
    A(l*s),
    PopState(),
    yaw(-a),
    A(l*s)]

@Rule
def F(l):
  pass

def resetGlobals():
  global state,stack
  state = rs.XformIdentity()
  stack = [state]

def getPos(xForm):
    x = xForm[0,3]
    y = xForm[1,3]
    z = xForm[2,3]
    return rs.VectorCreate([x,y,z],[0,0,0])

def getX(xForm):
    u = xForm[0,0]
    v = xForm[1,0]
    w = xForm[2,0]
    return rs.VectorCreate([u,v,w],[0,0,0])

def getY(xForm):
    u = xForm[0,1]
    v = xForm[1,1]
    w = xForm[2,1]
    return rs.VectorCreate([u,v,w],[0,0,0])

def getZ(xForm):
    u = xForm[0,2]
    v = xForm[1,2]
    w = xForm[2,2]
    return rs.VectorCreate([u,v,w],[0,0,0])

turtleShell = """
from branchy_test import *

state = rs.XformIdentity()
stack = [state]

%s

"""

def main():
  result = expand(A(50),5)

  result = map(lambda x: x.pretty, result)
  #result.insert(0,'initState()')
  print result[0]
  print result[1]
  commands = "\n".join(result)
  f = open('commands.py', 'w')  
  f.write(commands)
  #print commands
  turtleProgram = turtleShell % commands
  resetGlobals()
  exec(turtleProgram)

if __name__ == "__main__":
  main()