#!/usr/bin/env python
# encoding: utf-8

import unittest
from point_distance import point_distance, load_csv_rows, create_distance_matrix


class DistanceTest(unittest.TestCase):
    """Test calculations from
    http://ncalculators.com/geometry/length-between-two-points-calculator.htm
    """
    def test_point_distance_zero(self):
        self.assertEqual(point_distance(0, 0, 0, 0), 0.0)

    def test_point_distance_all_positive(self):
        self.assertEqual(point_distance(5.2, 3.8, 2.4, 8.9), 5.818)

    def test_point_distance_all_negative(self):
        self.assertEqual(point_distance(-6.3, -8.1, -2.4, -6.9), 4.080)

    def test_point_distance_positive_negative1(self):
        self.assertEqual(point_distance(-8.3, 2.1, 9.4, 7.4), 18.476)

    def test_point_distance_positive_negative2(self):
        self.assertEqual(point_distance(-8.3, 2.1, -9.4, 7.4), 5.413)

    def test_point_distance_positive_negative3(self):
        self.assertEqual(point_distance(-8.3, -2.1, -9.4, 7.4), 9.563)


class PointListTest(unittest.TestCase):
    def setUp(self):
        self.point_list = [(1, 0.000, 0.000),
                           (2, -7.358, 6.745),
                           (3, 2.848, -5.605),
                           (4, 1.077, 6.763),
                           (5, -5.552, 9.606),
                           (6, -3.267, 4.133),
                           (7, -9.046, -8.257),
                           (9, 6.406, -2.997),
                           (10, 5.874, 2.111),
                           (11, -5.598, -9.757)]

        self.matrix = [['PointId', 1, 2, 3, 4, 5, 6, 7, 9, 10, 11],
                       [1, 0.0, 9.982, 6.287, 6.848, 11.095, 5.268, 12.248, 7.072, 6.242, 11.249],
                       [2, 9.982, 0.0, 16.021, 8.435, 3.383, 4.854, 15.097, 16.863, 14.02, 16.596],
                       [3, 6.287, 16.021, 0.0, 12.494, 17.376, 11.499, 12.186, 4.411, 8.288, 9.411],
                       [4, 6.848, 8.435, 12.494, 0.0, 7.213, 5.078, 18.113, 11.12, 6.682, 17.818],
                       [5, 11.095, 3.383, 17.376, 7.213, 0.0, 5.931, 18.202, 17.373, 13.665, 19.363],
                       [6, 5.268, 4.854, 11.499, 5.078, 5.931, 0.0, 13.671, 12.017, 9.362, 14.084],
                       [7, 12.248, 15.097, 12.186, 18.113, 18.202, 13.671, 0.0, 16.323, 18.169, 3.76],
                       [9, 7.072, 16.863, 4.411, 11.12, 17.373, 12.017, 16.323, 0.0, 5.136, 13.777],
                       [10, 6.242, 14.02, 8.288, 6.682, 13.665, 9.362, 18.169, 5.136, 0.0, 16.506],
                       [11, 11.249, 16.596, 9.411, 17.818, 19.363, 14.084, 3.76, 13.777, 16.506, 0.0]]

    def test_load_csv_rows(self):
        self.assertEqual(load_csv_rows('test_points.csv'), self.point_list)

    def test_create_matrix(self):
        self.assertEqual(create_distance_matrix(self.point_list), self.matrix)


if __name__ == '__main__':
    unittest.main()
