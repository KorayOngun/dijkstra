lines = [["a","e",1],["a","c",6],["a","b",5],["e","c",2],["c","b",1],["c","d",4],["b","f",1],["f","d",3],["f","h",2],["d","h",5]]

start = "a"
target = "h"

distance = {
    "b":float("inf"),
    "c":float("inf"),
    "d":float("inf"),
    "e":float("inf"),
    "f":float("inf"),
    "h":float("inf")}

for s,d,p in lines:
    if s==start:
        distance[d]=p
        continue
    else:
        if distance[s]+p < distance[d]:
            distance[d] = distance[s]+p

print(distance)