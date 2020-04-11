#doc for this API: https://developers.google.com/maps/documentation/distance-matrix/intro#unit_systems
import googlemaps

#create list of places, and a list of names in the same order
#please put start to 0, and end to last in list
place = list(("""input list of latitude and longitude here"""))
name = ["""input names for places here, in order with the list above"""]

#matrix to store the distances
matrix = [[0 for x in range(len(place))] for y in range(len(place))] 

#creates instance using the API key
gmaps = googlemaps.Client(key='API_key') #replace API_key with your API key

#use google maps API
result = gmaps.distance_matrix(place, place, mode="driving", avoid="tolls")

#store results into matrix, units are in meters
for i in range(len(place)):
    for j in range(len(place)):
        matrix[i][j] = result["rows"][i]["elements"][j]["distance"]["value"]

#visualize matrix
#print(matrix)

#start with dfs
minLen = float("inf")
minPath = ""

def dfs(stops,visited,path,length,lastStop):
    if len(visited)+1 == len(stops): #if only the last stop is not visited
        global minLen
        global minPath            
        length = length+matrix[lastStop][len(stops)-1] 
        path = path+name[len(stops)-1]
        if length < minLen:
            minLen = length
            minPath = path
        return
    for i in range(1,len(stops)-1):
        if i in visited:
            continue
        visited.add(i)
        dfs(stops,visited,path+name[i]+"->",length+matrix[lastStop][i],i)
        visited.remove(i)
        
#init for dfs, start at 0
visitedInit = set()
visitedInit.add(0)
pathInit = name[0] + "->"
for i in range(1,len(place)-1): #no need to use start and end as second point of dfs
    lengthInit = matrix[0][i]
    dfs(place,visitedInit,pathInit,lengthInit,0)
    
print(minPath)
print(minLen)
