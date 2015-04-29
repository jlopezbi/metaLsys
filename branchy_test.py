import rhinoscriptsyntax as rs

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

########## OTHER CONTEXT FUNCTIONS ############

def roll(a):
  global state
  rotMat = rs.XformRotation2(a/2,getX(state),getPos(state))
  state = rotMat*state

def pitch(a):
  global state
  rotMat = rs.XformRotation2(a/2,getY(state),getPos(state))
  state = rotMat*state

def yaw(a):
  global state
  rotMat = rs.XformRotation2(a/2,getZ(state),getPos(state))
  state = rotMat*state
  #state = rs.XformMultiply(rotMat,state)

def S():
  rs.AddPoint(getPos(state))

def F(l):
  global state
  pntA = getPos(state)
  vec = getX(state)
  vec = rs.VectorUnitize(vec)
  vec = rs.VectorScale(vec,l)

  transMat = rs.XformTranslation(vec)
  state = state*transMat
  pntB = getPos(state)
  rs.AddLine(pntA,pntB)

def PushState():
  global state
  stack.append(state)

def PopState():
  global state
  state = stack.pop()

def initState():
  global state, stack
  state = rs.XformIdentity()
  stack = [state]

########################################

def main():
  
  initState()
  print "initial State:",
  print state
  F(10)
  PushState()
  yaw(-45)
  pitch(45)
  F(5)
  PopState()
  yaw(10)
  F(5)
  
  
  

if __name__ == "__main__":
    main()