#doc for this API: https://developers.google.com/maps/documentation/distance-matrix/intro#unit_systems
import googlemaps

#matrix to store the distances
matrix = [[0 for x in range(len(place))] for y in range(len(place))] 

#creates instance using the API key
gmaps = googlemaps.Client(key='AIzaSyAXt4dTGgM-q-JEEFg9CM6B73bxvmsflUQ')

#use google maps API
result = gmaps.distance_matrix(place, place, mode="driving", avoid="tolls", units="imperial")

#store results into matrix
for i in range(len(place)):
    for j in range(len(place)):
        matrix[i][j] = result["rows"][i]["elements"][j]["distance"]["value"]

#visualize matrix
#print(matrix)

#start with dfs
minLen = float("inf")
minPath = ""

def dfs(stops,visited,path,length,lastStop):
    if len(visited) == len(stops) and lastStop == len(place)-1:
        global minLen
        global minPath            
        if length < minLen:
            minLen = length
            minPath = path
        return
    for i in range(len(stops)):
        if i in visited:
            continue
        visited.add(i)
        dfs(stops,visited,path+dic[i]+"->",length+matrix[lastStop][i],i)
        visited.remove(i)
        
#init for dfs, start at 0
visitedInit = set()
visitedInit.add(0)
pathInit = dic[0] + "->"
for i in range(1,len(place)-1): #no need to use start and end as second point of dfs
    lengthInit = matrix[0][i]
    dfs(place,visitedInit,pathInit,lengthInit,0)
    
print(minPath[:-2])
print(minLen)