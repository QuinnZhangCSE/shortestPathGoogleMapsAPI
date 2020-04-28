# shortestPathGoogleMapsAPI
Find shortest path between latitude and longitudes using the google maps distance matrix API

4/28/2020

This problem has been solved with google OR-Tools. I have two programs, one that finds the route for any amount of vehicles with the attempt to have all vehicles travel the same distance, another with the attempt to have all vehicles with the same number of stops.

-----------------------------------------------------------------------------------------------------------------------------------

4/11/2020:

Finished:

Optimized depth first search algorithm

-----------------------------------------------------------------------------------------------------------------------------------

4/10/2020:

Finished:

Used google maps API to obtain the distance matrix for a list of latitude and longitude. Use depth first search algorithm to compute the shortest path, then display the travel order and total distance for the shortest path.

Roadmap:

To allow user input names and locations instead of changing the source code.

The API can only calculate the distance matrix for 10 points, with the start and end points defined, can only calculate for 10-2=8 locations. Aim for scalability, this problem can be solved by combining the matrix obtained by mutiple API requests. The API have a constraint of 10^3 elements per second, this can be bypassed by adding a timed pause in the code for API request.
