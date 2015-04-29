from lsystems import Rule, expand
import rhinoscriptsyntax as rs

a = 90

@Rule
def left(d):
  pass

@Rule
def right(d):
  pass

@Rule
def forward(x):
  pass

@Rule
def A(s):
    return [
        left(a),
        B(s),
        forward(s),
        right(a),
        A(s),
        forward(s),
        A(s),
        right(a),
        forward(s),
        B(s),
        left(a)]
 
@Rule
def B(s):
    return [
        right(a),
        A(s),
        forward(s),
        left(a),
        B(s),
        forward(s),
        B(s),
        left(a),
        forward(s),
        A(s),
        right(a)]



pos = rs.VectorCreate([0,0,0],[0,0,0]) #position starts at zero
heading = rs.VectorCreate([0,0,0],[0,1,0]) # start facing +y
axis = rs.VectorCreate([0,0,0],[0,0,1]) # rotate about z axis
points = [pos]

#Keeping the pun :)
turtleShell = """

def right(d):
  global heading,axis
  heading = rs.VectorRotate(heading,d,axis)

def left(d):
  global heading,axis
  heading = rs.VectorRotate(heading,-d,axis)

def forward(s):
  global heading,axis,points,pos
  pos = rs.VectorAdd(pos,heading)
  points.append(pos)


%s

rs.AddPolyline(points)
 
"""

    
def main():
    # expand from Axiom A 5 times
    result = expand(A(10), 7)
 
    # TODO: these things probably belong in the lsystems package
    # convert output to functional string syntax
    result = map(lambda x: x.pretty, result)    
    # filter out non-terminals and put each command on its own line
    commands = "\n".join(filter(lambda x: x[0] not in ['A', 'B'], result))
 
    # adds the generated commands to the file
    turtleProgram = turtleShell % commands
 
    
    #f = open('program.py', 'w')  
    #f.write(turtleProgram)
    exec(turtleProgram)
  
     
    
    
 
    # another option is to write turtleProgram to a file and run it separately
    #with open('outputProgram.py', 'w') as f:
    #    f.write(turtleProgram)
 
 
if __name__ == "__main__":
    main()




