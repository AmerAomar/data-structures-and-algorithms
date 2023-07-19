# graph-business-trip
<!-- Description of the challenge -->
`Determine whether the trip is possible with direct flights, and how much it would cost.`

## Whiteboard Process
<!-- Embedded whiteboard image -->
![whiteboard](./business%20trip.png)

## Approach & Efficiency
 
`Time Complexity:`

O(N), where N is the number of cities in the trip list. We iterate through the list once.

`Space Complexity:`

O(1). The method uses a constant amount of space, regardless of the input size

## Solution
<!-- Show how to run your code, and examples of it in action -->
```python
def business_trip(self, cities=[]):
        '''
        Determine whether the trip is possible with direct flights, and calculate the cost of the trip.
        '''
        cost = 0

        for i in range(len(cities) - 1):
            current_city = cities[i]
            next_city = cities[i + 1]

            if next_city in self.get_neighbors(current_city):
                if next_city in self.vertices[current_city]:
                    flight_cost = self.vertices[current_city][next_city]
                    cost += flight_cost
                else:
                    return None
            else:
                return None

        return f"${cost}"

```
