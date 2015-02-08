# point_distance.py
#### Calculate distances between points in a CSV
test
###### Usage

`python point_distance.py path_to_csv`

If invalid data or duplicate point IDs are encountered, they will simply be
ignored - check the command line output for warnings.


###### Requirements:

* Python 2.7


###### Input:

CSV containing point id, x, y coordinate columns:

| id | x | y  |
|----|---|----|
| 1  | 0 | 0  |
| 2  | 0 | 1  |
| 3  | 0 | 2  |
| 4  | 0 | 5  |
| 5  | 0 | 10 |

All ID's must be unique whole numbers; all coordinates must be whole numbers
or decimal


###### Output:
CSV containing a matrix displaying distances between points will be created in
the current working directory

| id | 1  | 2 | 3 | 4 | 5  |
|----|----|---|---|---|----|
| 1  | 0  | 1 | 2 | 5 | 10 |
| 2  | 1  | 0 | 1 | 4 | 9  |
| 3  | 2  | 1 | 0 | 3 | 8  |
| 4  | 5  | 4 | 3 | 0 | 5  |
| 5  | 10 | 9 | 8 | 5 | 0  |
(Note - you get decimals as an output, not just integers like in this table)

###### Assumptions

* Input CSV is comma delimited
* IDs are unique and mandatory
* Values in coordinate fields are numeric (i.e. no exponential notation present)
* It is acceptable to ignore erroneous points (duplicate IDs, non-numeric values)


###### Testing

`python test_point_distance.py`

* Tests the critical function `point_distance` multiple times which calculates
distance between points.

* Tests the function `load_csv_rows` which imports the data from CSV, ignoring
faulty data.

* Tests the function `create_matrix` which creates the final matrix containing
distances calculated between points
