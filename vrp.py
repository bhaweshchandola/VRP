__author__ = 'bhawesh.chandola'

from itertools import permutations


vehicle_capacity =60
def distance(point1, point2):

    return((point2[1] - point1[1])**2 + (point2[0] - point1[0])**2)**0.5
'''
The customer location is given in the format [x axis location,y axis location,demand]
'''
initial=[0,0,0] #depot location
#points=([0,0,0],[6,0,10],[2,3,30],[3,7,40],[0.5,9,10],[8,9,20],[10,3,25]) #dataset
#points=([0,0,0],[-92,88,16],[67,79,21],[-71,-37,15],[104,-36,24],[-177,27,4])  #dataset 1
#points = ([0,0,0],[-151,-8,7],[-146,93,29],[-37,129,5],[115,127,37],[323,246,31],[245,33,29],[129,-135,21],[-12,-144,35],[-129,-127,31],[-240,-64,11])  #dataset 2
points=([0,0,0],[-168,153,17],[-15,181,11],[161,140,10],[161,-40,18],[-115,-189,22],[-230,-42,7])
new_perm=[]   #new permutation with first index fixed
#perm=list(permutations(points))  #permutation of the points
perm = permutations(list(points))

for f in perm:
    if f[0] == initial:

        new_perm.append(f)


totaldistance=[]
vehicles_used=[] #number of vehicles used
index=0
s=0
cap=0  #capacity of the vehicle
vehicle_no=1
for p in new_perm:
    s=0
    cap=0
    vehicle_no=1
    for x in range(0,len(points)-1): #set according to the (elements in list-1)
        if cap+p[x][2]>=vehicle_capacity:   #capacity of vehice is defined to be 50 if that is excedded new vehicle is called
            vehicle_no=vehicle_no+1
            s=s+distance(p[x],p[0])  # vehicle returning to depot
            #s=s+distance(p[0],p[x+1])
            cap=p[x][2]

        else:
            cap=cap+p[x][2]
        s=s+distance(p[x],p[x+1])

    s=s+distance(p[x+1],p[0])
    totaldistance.append(s)
    vehicles_used.append(vehicle_no)


indi=totaldistance.index(min(totaldistance))
#print(totaldistance.index(min(totaldistance)))
#print(totaldistance)
print "Total Distance Covered",totaldistance[indi]
print "Best Path:",new_perm[indi]
print "Vehicles Used",vehicles_used[indi]

# for z in new_perm:
#     print(new_perm)
# print(vehicles_used)
final_route=new_perm[indi]
c=0
d=0
route_name=[]
for b in points:
    c=points.index(final_route[d])
    route_name.append(c)
    d=d+1
print "ROUTE : "
cap=0


for x in range(0,len(route_name)):
    if cap+final_route[x][2]>=60:
        cap=final_route[x][2]
        
        print "V"+str(route_name[x]),

    else:
        cap=cap+final_route[x][2]
        print "V"+str(route_name[x]),
print "V0"







