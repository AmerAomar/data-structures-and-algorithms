# Merge Sort
<!-- Description of the challenge -->

## Whiteboard Process
<!-- Embedded whiteboard image -->
![merge sort](cc27.png)

## Approach & Efficiency

The Merge Sort algorithm has a time complexity of O(n log n) in all cases. This means that the time it takes to sort an array of size n grows logarithmically with respect to the input size. Merge Sort achieves this efficiency by dividing the array into smaller subarrays, sorting them recursively, and then merging the sorted subarrays back together.

Merge Sort has a space complexity of O(n) due to the additional space required to store the temporary arrays during the merging process.

## samples have been tested

[8,4,23,42,16,15]

[20,18,12,8,5,-2]

[5,12,7,5,5,7]

[2,3,5,7,13,11]

## All of the Samples above Pased

After installing the dependencies using this command

```python
pip install -r requirements.txt
```

You can run the tests using this command

```python
pytest test.py
```
