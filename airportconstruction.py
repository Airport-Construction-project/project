import math
def longestpath():
    n = int(input())
    p = []
    
    for i in range(n):
        x,y = map(int,input().split())
        p.append((x,y))
        
    distance = max_distPointtoPoint(n,p)
    
    return distance
def max_distPointtoPoint(n,p):
    l = []
   
    for i in range(n):
        for j in range(i+1,n):
            p1 = p[i]
            p2 = p[j]
            
            distance = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )
            distance2 = extend_line(n,p)
            if outorin(p,p1,p2) is True:
               l.append(distance)
               l.append(distance2)
            else:
                continue
    
    print(max(l))
    

def extend_line(n,p):
   
    for i in range(n):
        for j in range(i+1,n):
            dist = 0
            s = 10000
            p1 = p[i]
            p2 = p[j]
            p3 = (p2[0]-p1[0])
            if(p3 == 0):
                continue
            else:
               slope1 = (p2[1]-p1[1])/p3
               a = math.atan(slope1)
               p11 = (p1[0]+s*math.cos(a),p1[1] + s*math.sin(a))
               p22 = (p2[0]+s*math.cos(a),p2[1] + s*math.sin(a))
               equ1 = []
               equ2 = []
               equ3 = []
               equ1 = lineFromPoints(p1,p11)
               equ3 = lineFromPoints(p2,p22)
               for k in range(n):
                   for m in range(k+1,n):
                       q1 = p[k]
                       q2 = p[m]
                       intersect1 = doIntersect(p1,p11,q1,q2)
                       intersect2 = doIntersect(p2,p22,q1,q2)
                       if intersect1 is True:
                           break
                           slope2 = (q2[1]-q1[1])/(q2[0]-q1[0])
                           equ2 = lineFromPoints(q1,q2)
                           coordinate2 = []
                           coordinate2.append[equ2]
                           x0 = (equ1[1]*equ2[2] -equ1[2]*equ2[1])/(equ1[0]*equ2[1] - equ2[0]*equ1[1])
                           y0 = (equ2[0]*equ1[2] - equ1[0]*equ2[2])/(equ1[0]*equ2[1]-equ1[1]*equ2[0])
                           poi1 = zip(x0,y0)
                           dist = math.sqrt( ((int(p2[0])-int(poi1[0]))**2)+((int(p2[1])-int(poi1[1]))**2) )
                       elif intersect2 is True:
                           break
                           slope2 = (q2[1]-q1[1])/(q2[0]-q1[0])
                           x1 = (equ3[1]*equ2[2] -equ3[2]*equ2[1])/(equ3[0]*equ2[1] - equ2[0]*equ3[1])
                           y1 = (equ2[0]*equ3[2] - equ3[0]*equ2[2])/(equ3[0]*equ2[1]-equ3[1]*equ2[0])
                           poi2 = zip(x1,y1)
                           dist = math.sqrt( ((int(p1[0])-int(poi2[0]))**2)+((int(p1[1])-int(poi2[1]))**2) )
                       else:
                           break
    return dist                
def lineFromPoints(P, Q):
 
    a = Q[1] - P[1]
    b = P[0] - Q[0]
    c = a*(P[0]) + b*(P[1])
    coord = []
    coord.append(a)
    coord.append(b)
    coord.append(c)
    return coord

def onSegment(p, q, r):
    if ( (q[0]<= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and 
           (q[1]<= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))):
        return True
    return False
  
def orientation(p, q, r):
    val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1]- q[1]))
    if (val > 0):
          
        # Clockwise orientation
        return 1
    elif (val < 0):
          
        # Counterclockwise orientation
        return 2
    else:
          
        # Colinear orientation
        return 0
def doIntersect(p1,q1,p2,q2):
     o1 = orientation(p1, q1, p2)
     o2 = orientation(p1, q1, q2)
     o3 = orientation(p2, q2, p1)
     o4 =  orientation(p2, q2, q1)
     
    
     if ((o1 != o2) and (o3 != o4)):
        return True
        
   
     if ((o1 == 0) and onSegment(p1, p2, q1)):
        return True
  
    
     if ((o2 == 0) and onSegment(p1, q2, q1)):
        return True
  
   
     if ((o3 == 0) and onSegment(p2, p1, q2)):
        return True
  
    
     if ((o4 == 0) and onSegment(p2, q1, q2)):
        return True
     return False

def outorin(p,p1,p2):
    count = 0
    q1 = ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
    q2 = max(p)
    if doIntersect(p1,p2,q1,q2) is True:
          count += 1
     # Return true if count is odd, false otherwise
    return (count % 2 == 1)
    

longestpath()    

