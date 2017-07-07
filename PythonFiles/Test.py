WTC = '/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Bach WTC Subjects/'
wtc1_Bfmin = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Bfmin.xml')
canon_data = {}
WTC1_canonPercent = {0: 3.3333333333333335, 1: 1.4814814814814816, 2: 11.481481481481481, 3: 40.74074074074074, 4: 10.0, 5: 1.6666666666666667, 6: 0.0, 7: 0.7407407407407408, 8: 15.0, 9: 0.0, 10: 1.6666666666666667, 11: 11.666666666666666, 12: 5.9259259259259265, 13: 1.4814814814814816, 14: 0.0, 15: 29.444444444444446, 16: 38.333333333333336, 17: 1.4814814814814816, 18: 2.2222222222222223, 19: 1.1111111111111112, 20: 0.0, 21: 12.222222222222221, 22: 5.185185185185185, 23: 0.5555555555555556}
WTC1_length = {0: 17, 1: 25, 2: 22, 3: 4, 4: 18, 5: 14, 6: 28, 7: 15, 8: 20, 9: 24, 10: 23, 11: 15, 12: 21, 13: 22, 14: 33, 15: 16, 16: 10, 17: 19, 18: 17, 19: 18, 20: 41, 21: 13, 22: 17, 23: 25}
wtc_length = {0: 17, 1: 25, 2: 22, 3: 4, 4: 18, 5: 14, 6: 28, 7: 15, 8: 20, 9: 24, 10: 23, 11: 15, 12: 21, 13: 22, 14: 33, 15: 16, 16: 10, 17: 19, 18: 17, 19: 18, 20: 41, 21: 13, 22: 17, 23: 25, 24: 29, 25: 12, 26: 16, 27: 23, 28: 12, 29: 24, 30: 23, 31: 18, 32: 8, 33: 55, 34: 25, 35: 28, 36: 25, 37: 25, 38: 45, 39: 25, 40: 25, 41: 26, 42: 24, 43: 14, 44: 26, 45: 32, 46: 15, 47: 23}
wtc_data = {0: 3.3333333333333335, 1: 1.4814814814814816, 2: 11.481481481481481, 3: 40.74074074074074, 4: 10.0, 5: 1.6666666666666667, 6: 0.0, 7: 0.7407407407407408, 8: 15.0, 9: 0.0, 10: 1.6666666666666667, 11: 11.666666666666666, 12: 5.9259259259259265, 13: 1.4814814814814816, 14: 0.0, 15: 29.444444444444446, 16: 38.333333333333336, 17: 1.4814814814814816, 18: 2.2222222222222223, 19: 1.1111111111111112, 20: 0.0, 21: 12.222222222222221, 22: 5.185185185185185, 23: 0.5555555555555556, 24: 0.8888888888888888, 25: 25.0, 26: 5.555555555555555, 27: 0.0, 28: 0.0, 29: 0.0, 30: 0.31746031746031744, 31: 1.4814814814814816, 32: 16.38888888888889, 33: 0.0, 34: 0.0, 35: 0.0, 36: 0.0, 37: 1.6666666666666667, 38: 0.0, 39: 0.6349206349206349, 40: 0.0, 41: 0.0, 42: 0.0, 43: 19.25925925925926, 44: 0.0, 45: 0.0, 46: 1.7777777777777777, 47: 0.0}
rhythmic_variance = [30.59523809523809, 37.77777777777778, 22.22222222222222, 44.444444444444436, 67.88048552754435, 19.487179487179485, 21.7283950617284, 24.28571428571428, 20.350877192982455, 0.0, 14.545454545454545, 22.857142857142858, 33.25396825396825, 49.2063492063492, 28.749999999999996, 38.22222222222222, 22.22222222222222, 18.51851851851852, 8.333333333333332, 27.45098039215686, 9.666666666666666, 11.111111111111109, 40.833333333333336, 15.555555555555555, 14.285714285714283, 23.030303030303028, 23.703703703703702, 3.03030303030303, 24.24242424242424, 4.347826086956523, 33.333333333333336, 33.893557422969195, 28.571428571428573, 25.008818342151674, 18.055555555555554, 9.876543209876543, 29.682539682539687, 42.77777777777777, 2.727272727272727, 22.222222222222218, 26.66666666666667, 5.333333333333332, 20.289855072463766, 15.384615384615385, 5.333333333333332, 18.924731182795696, 28.571428571428566, 14.545454545454545]
WTC_canonNumber = {0: 6, 1: 4, 2: 31, 3: 110, 4: 18, 5: 3, 6: 0, 7: 2, 8: 27, 9: 0, 10: 3, 11: 42, 12: 16, 13: 8, 14: 0, 15: 106, 16: 69, 17: 4, 18: 4, 19: 2, 20: 0, 21: 44, 22: 14, 23: 2, 24: 2, 25: 45, 26: 10, 27: 0, 28: 0, 29: 0, 30: 2, 31: 4, 32: 59, 33: 0, 34: 0, 35: 0, 36: 0, 37: 6, 38: 0, 39: 2, 40: 0, 41: 0, 42: 0, 43: 52, 44: 0, 45: 0, 46: 8, 47: 0}