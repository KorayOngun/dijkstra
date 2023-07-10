import time

tic = time.perf_counter()

lines = [["a","c",6],["a","b",5],["e","c",2],["c","b",1],["b","f",1],["c","d",4],["f","d",3],["d","h",5],["f","h",2],["a","e",1]]

start = "a"
target = "h"



distance = {
    "a":float("inf"),
    "b":float("inf"),
    "c":float("inf"),
    "d":float("inf"),
    "e":float("inf"),
    "f":float("inf"),
    "h":float("inf")}

for i in range(2):
    for s,d,p in lines:
        if s==start and distance[d]==float("inf"):
            distance[d]=p
            continue
        else:
            if distance[s]+p < distance[d]: 
                distance[d] = distance[s]+p

toc = time.perf_counter()

print(f"{toc - tic:0.4f}")

print(distance)