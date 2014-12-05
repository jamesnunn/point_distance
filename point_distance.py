#!/usr/bin/env python
# encoding: utf-8

import csv
import math
import sys


def point_distance(x1, y1, x2, y2, dp=3):
    """ Calculate the distance between 2 2D points using Pythagorean theorem
    a^2 + b^2 = c^2. Return distance to <dp> decimal places.

    Parameters:
        x1, y1 - X and Y coordinate pair of first point
        x2, y2 - X and Y coordinate pair of second point
        dp     - decimal places of distance
    """
    # Get a^2 & b^2
    a2 = float(x2 - x1) ** 2
    b2 = float(y2 - y1) ** 2
    # Sum them to get c^2
    c2 = a2 + b2
    # Root the hypotenuse
    c = round(math.sqrt(c2), dp)

    return c


def load_csv_rows(input_file):
    """Read a CSV file into a list and perform validation checks on data during
    loading. Return a list of tuples representing point ID, x, y.

    Parameters:
        input_file - CSV file containing id, x, y columns

    """
    with open(input_file, 'rb') as in_file:
        print 'Loading rows from {}\n'.format(input_file)

        points_csv = csv.reader(in_file)

        # Create dict of points to work on, checking the contents of the rows
        # as we go
        pt_ids = []
        pts_list = []
        row_count = 0

        for row in points_csv:
            row_count += 1

            # Skip header row
            if row_count == 1:
                continue

            # Convert data to integer and float types; if errors are found,
            # skip it and log error
            try:
                in_pt_id, in_pt_x, in_pt_y = (int(row[0]),
                                              float(row[1]),
                                              float(row[2]))
            except ValueError:
                print 'WARNING: Ignored invalid data in row ' \
                      '{}\n'.format(row_count)
                continue

            # Check if duplicate ID exists, if it does, skip this one and
            # log error otherwise add it to the list of points
            if in_pt_id not in pt_ids:
                pts_list.append((in_pt_id, in_pt_x, in_pt_y))
                pt_ids.append(in_pt_id)
            else:
                print 'WARNING: Ignored duplicate ID ' \
                      '{} in row {}\n'.format(in_pt_id, row_count)
                continue
            # If we get to here, a new, clean, validated point has been added
    return pts_list


def create_distance_matrix(pts_list):
    """Generate a matrix of points - distance to point

    Parameters
        pts_list - list of points in the format [id, x_coord, y_coord]
    """
    print 'Generating distance matrix\n'
    header_row = ['PointId']  # Cell label to start output csv header row
    matrix = [header_row]

    # Now iterate through points and calculate distance to every other point
    for id1, x1, y1 in pts_list:
        # Add next ID to start of each row (in ID column)
        new_row = [id1]
        # Add IDs to the header row
        header_row.append(id1)
        for id2, x2, y2 in pts_list:
            # Add the distance calculated to the row
            new_row.append(point_distance(x1, y1, x2, y2))
        matrix.append(new_row)
    return matrix


def main(*args):
    INPUT_FILE = args[0]

    pts_list = load_csv_rows(INPUT_FILE)
    matrix = create_distance_matrix(pts_list)

    # Now write matrix to output csv
    with open('points_out.csv', 'wb') as out_file:
        points_out_csv = csv.writer(out_file)
        points_out_csv.writerows(matrix)

    print 'Operation complete'

if __name__ == '__main__':
    main(sys.argv[1])
