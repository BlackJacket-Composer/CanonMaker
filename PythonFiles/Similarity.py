from music21 import *
import numpy as np
import pylab as pl
import os
from scipy import spatial, stats


WTC = '/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Bach WTC Subjects/'
wtc1_Bfmin = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Bfmin.xml')
canon_data = {}
WTC1_canonPercent = {0: 3.3333333333333335, 1: 1.4814814814814816, 2: 11.481481481481481, 3: 40.74074074074074, 4: 10.0, 5: 1.6666666666666667, 6: 0.0, 7: 0.7407407407407408, 8: 15.0, 9: 0.0, 10: 1.6666666666666667, 11: 11.666666666666666, 12: 5.9259259259259265, 13: 1.4814814814814816, 14: 0.0, 15: 29.444444444444446, 16: 38.333333333333336, 17: 1.4814814814814816, 18: 2.2222222222222223, 19: 1.1111111111111112, 20: 0.0, 21: 12.222222222222221, 22: 5.185185185185185, 23: 0.5555555555555556}
WTC2_canonPercent = {24: 0.8888888888888888, 25: 25.0, 26: 5.555555555555555, 27: 0.0, 28: 0.0, 29: 0.0, 30: 0.31746031746031744, 31: 1.4814814814814816, 32: 16.38888888888889, 33: 0.0, 34: 0.0, 35: 0.0, 36: 0.0, 37: 1.6666666666666667, 38: 0.0, 39: 0.6349206349206349, 40: 0.0, 41: 0.0, 42: 0.0, 43: 19.25925925925926, 44: 0.0, 45: 0.0, 46: 1.7777777777777777, 47: 0.0}
WTC2_length = {24: 29, 25: 12, 26: 16, 27: 23, 28: 12, 29: 24, 30: 23, 31: 18, 32: 8, 33: 55, 34: 25, 35: 28, 36: 25, 37: 25, 38: 45, 39: 25, 40: 25, 41: 26, 42: 24, 43: 14, 44: 26, 45: 32, 46: 15, 47: 23}
WTC1_length = {0: 17, 1: 25, 2: 22, 3: 4, 4: 18, 5: 14, 6: 28, 7: 15, 8: 20, 9: 24, 10: 23, 11: 15, 12: 21, 13: 22, 14: 33, 15: 16, 16: 10, 17: 19, 18: 17, 19: 18, 20: 41, 21: 13, 22: 17, 23: 25}
wtc_length = {0: 17, 1: 25, 2: 22, 3: 4, 4: 18, 5: 14, 6: 28, 7: 15, 8: 20, 9: 24, 10: 23, 11: 15, 12: 21, 13: 22, 14: 33, 15: 16, 16: 10, 17: 19, 18: 17, 19: 18, 20: 41, 21: 13, 22: 17, 23: 25, 24: 29, 25: 12, 26: 16, 27: 23, 28: 12, 29: 24, 30: 23, 31: 18, 32: 8, 33: 55, 34: 25, 35: 28, 36: 25, 37: 25, 38: 45, 39: 25, 40: 25, 41: 26, 42: 24, 43: 14, 44: 26, 45: 32, 46: 15, 47: 23}
wtc_data = {0: 3.3333333333333335, 1: 1.4814814814814816, 2: 11.481481481481481, 3: 40.74074074074074, 4: 10.0, 5: 1.6666666666666667, 6: 0.0, 7: 0.7407407407407408, 8: 15.0, 9: 0.0, 10: 1.6666666666666667, 11: 11.666666666666666, 12: 5.9259259259259265, 13: 1.4814814814814816, 14: 0.0, 15: 29.444444444444446, 16: 38.333333333333336, 17: 1.4814814814814816, 18: 2.2222222222222223, 19: 1.1111111111111112, 20: 0.0, 21: 12.222222222222221, 22: 5.185185185185185, 23: 0.5555555555555556, 24: 0.8888888888888888, 25: 25.0, 26: 5.555555555555555, 27: 0.0, 28: 0.0, 29: 0.0, 30: 0.31746031746031744, 31: 1.4814814814814816, 32: 16.38888888888889, 33: 0.0, 34: 0.0, 35: 0.0, 36: 0.0, 37: 1.6666666666666667, 38: 0.0, 39: 0.6349206349206349, 40: 0.0, 41: 0.0, 42: 0.0, 43: 19.25925925925926, 44: 0.0, 45: 0.0, 46: 1.7777777777777777, 47: 0.0}
rhythmic_variance = [30.59523809523809, 37.77777777777778, 22.22222222222222, 44.444444444444436, 67.88048552754435, 19.487179487179485, 21.7283950617284, 24.28571428571428, 20.350877192982455, 0.0, 14.545454545454545, 22.857142857142858, 33.25396825396825, 49.2063492063492, 28.749999999999996, 38.22222222222222, 22.22222222222222, 18.51851851851852, 8.333333333333332, 27.45098039215686, 9.666666666666666, 11.111111111111109, 40.833333333333336, 15.555555555555555, 14.285714285714283, 23.030303030303028, 23.703703703703702, 3.03030303030303, 24.24242424242424, 4.347826086956523, 33.333333333333336, 33.893557422969195, 28.571428571428573, 25.008818342151674, 18.055555555555554, 9.876543209876543, 29.682539682539687, 42.77777777777777, 2.727272727272727, 22.222222222222218, 26.66666666666667, 5.333333333333332, 20.289855072463766, 15.384615384615385, 5.333333333333332, 18.924731182795696, 28.571428571428566, 14.545454545454545]
WTC_canonNumber = {0: 6, 1: 4, 2: 31, 3: 110, 4: 18, 5: 3, 6: 0, 7: 2, 8: 27, 9: 0, 10: 3, 11: 42, 12: 16, 13: 8, 14: 0, 15: 106, 16: 69, 17: 4, 18: 4, 19: 2, 20: 0, 21: 44, 22: 14, 23: 2, 24: 2, 25: 45, 26: 10, 27: 0, 28: 0, 29: 0, 30: 2, 31: 4, 32: 59, 33: 0, 34: 0, 35: 0, 36: 0, 37: 6, 38: 0, 39: 2, 40: 0, 41: 0, 42: 0, 43: 52, 44: 0, 45: 0, 46: 8, 47: 0}
melodic_variation = [78.6497713398284, 90.76726744416143, 70.1004947114358, 86.60254037844386, 101.6782254883588, 82.21888548451322, 71.1025401052407, 86.26058265484801, 46.97408542844452, 54.692596833785515, 68.92002730341882, 101.51286955758401, 59.22469278917488, 50.41008302500835, 90.09046988296042, 103.96522472262106, 54.609194192632145, 109.66245532978276, 41.5620909893548, 45.23443208612048, 83.87654042446768, 65.46536707079771, 79.05694150420949, 81.60579579678277, 78.72376628113507, 71.26966450997983, 66.66666666666666, 71.22108635358704, 92.96222517045284, 69.85816038567194, 82.16314960794824, 92.74230003348497, 35.35533905932738, 104.51052090383932, 70.22669219871398, 101.00021523868583, 89.16798613889469, 88.57539161640776, 46.83743350642876, 113.4552701106709, 92.52717680081582, 93.87366900090764, 59.63648483460119, 41.95235392680606, 89.18825850158447, 60.57803272210589, 77.17996763956492, 112.49402634348354]
freq_int = [2, 1, 9, -1, 2, 1, -2, -2, 2, 3, 2, -1, -2, -2, -2, 1, -4, 1, 5, 2, -2, 2, 2, -1, 2, 2, -2, 2, 0, -1, -2, -2, -2, -2, -2, 0, 2, 2, 2, 0, 2, 2, -2, -4, 0, 2, -2, 1]
first_int = [2, -1, 2, -1, 2, 2, -3, 7, 2, 3, 2, 1, 5, 2, 2, 1, 7, -1, -1, -1, 2, -5, -1, -4, -2, -4, 4, -1, 0, 2, 7, 0, 2, 2, -1, -7, -2, -4, -3, -4, -7, 2, 2, -4, -2, 2, 4, -4]
first_int_b1 = [-2, -4, 4, -1, 0, 2, 7, 0, 2, 2, -1, -7, -2, -4, -3, -4, -7, 2, 2, -4, -2, 2, 4, -4]
first_int_b2 = [2, -1, 2, -1, 2, 2, -3, 7, 2, 3, 2, 1, 5, 2, 2, 1, 7, -1, -1, -1, 2, -5, -1, -4]
key_profile = {0: 0, 1: 0, 2: 1, 3: 1, 4: 2, 5: 2, 6: 3, 7: 3, 8: 4, 9: 4, 10: 5, 11: 5, 12: 6, 13: 6, 14: 7, 15: 7, 16: 8, 17: 8, 18: 9, 19: 9, 20: 10, 21: 10, 22: 11, 23: 11, 24: 0, 25: 0, 26: 1, 27: 1, 28: 2, 29: 2, 30: 3, 31: 3, 32: 4, 33: 4, 34: 5, 35: 5, 36: 6, 37: 6, 38: 7, 39: 7, 40: 8, 41: 8, 42: 9, 43: 9, 44: 10, 45: 10, 46: 11, 47: 11}
first_pitch = [60, 72, 68, 49, 50, 62, 70, 63, 64, 64, 60, 60, 73, 54, 67, 62, 56, 56, 69, 57, 65, 70, 59, 66, 67, 67, 49, 49, 62, 62, 51, 63, 52, 64, 65, 72, 65, 61, 74, 62, 75, 68, 57, 64, 72, 58, 47, 66]
wtc_no_prolation = {0: 12, 1: 11, 2: 10, 3: 53, 4: 10, 5: 0, 6: 4, 7: 12, 8: 6, 9: 3, 10: 0, 11: 23, 12: 6, 13: 6, 14: 0, 15: 34, 16: 26, 17: 4, 18: 0, 19: 5, 20: 0, 21: 35, 22: 16, 23: 3, 24: 0, 25: 27, 26: 15, 27: 0, 28: 2, 29: 4, 30: 14, 31: 6, 32: 60, 33: 0, 34: 2, 35: 4, 36: 0, 37: 6, 38: 0, 39: 0, 40: 2, 41: 4, 42: 0, 43: 36, 44: 3, 45: 15, 46: 44, 47: 5}
wtc_no_prolation_percent = {0: 20.0, 1: 12.222222222222221, 2: 11.11111111111111, 3: 58.88888888888889, 4: 16.666666666666664, 5: 0.0, 6: 4.444444444444445, 7: 13.333333333333334, 8: 10.0, 9: 6.666666666666667, 10: 0.0, 11: 19.166666666666668, 12: 6.666666666666667, 13: 3.3333333333333335, 14: 0.0, 15: 28.333333333333332, 16: 43.333333333333336, 17: 4.444444444444445, 18: 0.0, 19: 8.333333333333332, 20: 0.0, 21: 29.166666666666668, 22: 17.77777777777778, 23: 2.5, 24: 0.0, 25: 45.0, 26: 25.0, 27: 0.0, 28: 3.3333333333333335, 29: 6.666666666666667, 30: 6.666666666666667, 31: 6.666666666666667, 32: 50.0, 33: 0.0, 34: 4.444444444444445, 35: 6.666666666666667, 36: 0.0, 37: 5.0, 38: 0.0, 39: 0.0, 40: 2.2222222222222223, 41: 3.8095238095238098, 42: 0.0, 43: 40.0, 44: 2.857142857142857, 45: 6.666666666666667, 46: 29.333333333333332, 47: 8.333333333333332}


def song_list(songs):
    list_songs = []
    for root, dirs, files in os.walk(songs):
        for file_name in files:
            path = os.path.join(root, file_name)
            tempStream = converter.parse(path)
            list_songs.append(tempStream)
    return list_songs


def first_degree(songs):
    song_ints = []
    ints = []
    for song in song_list(songs):
        allNotes = song.flat.getElementsByClass('Note')
        midiNotes = []
        # print allNotes
        for y in allNotes:
            midiNotes.append(y.pitch.midi)
        for y in midiNotes[:1]:
            ints.append(y)
    for x in ints:
        song_ints.append(x)
    print(song_ints)
    return song_ints


def rhythmic_variability(songs):
    wha = []
    list_songs = []
    for root, dirs, files in os.walk(songs):
        for file_name in files:
            path = os.path.join(root, file_name)
            tempStream = converter.parse(path)
            list_songs.append(tempStream)
    for song in list_songs:
        wha.append(analysis.patel.nPVI(song.flat.notesAndRests))
    # print(wha)
    return wha


def melodic_variability(songs):
    wha = []
    list_songs = []
    for root, dirs, files in os.walk(songs):
        for file_name in files:
            path = os.path.join(root, file_name)
            tempStream = converter.parse(path)
            list_songs.append(tempStream)
    for song in list_songs:
        wha.append(song.parts.flat.NoteEditorial.melodicIntervals)
    return wha
    # print(wha)

"""TODO: make chart that compares interval frequency with success"""


def interval_chart(songs):
    most_int = []
    for x in intervalStream(song_list(songs)):
        most_int.append(max(set(x), key=x.count))
    # print(most_int)
    pl.bar(range(0, 48), most_int, width=0.5)
    pl.xticks(range(0, 48))
    pl.title("Interval Sum vs Canonic Success")
    pl.ylabel("most frequent interval")
    pl.xlabel("WTC subject")
    pl.show()

    # pl.bar(X, corpus_dict.values(), align='center', width=0.5)
    # pl.xticks(X, corpus_dict.keys())
    # ymax = max(corpus_dict.values()) + 1
    # pl.ylim(0, ymax)
    # pl.show()
    # print(corpus_dict)



def interval_comparison(songs):
    """interval makeup of entire WTC"""
    song_stuff = intervalStream(song_list(songs))
    all_intervals = []
    for x in song_stuff:
        intervalMakeup = {}
        x = sorted(x)
        for y in range(-12, 13):
            intervalMakeup[y] = 0
            for z in x:
                if z == y:
                    intervalMakeup[z] +=1
                    # else:
                    #     intervalMakeup[z] = 1
        all_intervals.append(intervalMakeup)
    # print(all_intervals)
    return all_intervals


def firstInterval(songs):
    """gets directed melodic intervals for given list of songs"""
    song_ints = []
    for song in songs:
        allNotes = song.flat.getElementsByClass('Note')
        midiNotes = []
        ints = []
        # print allNotes
        for y in allNotes:
            midiNotes.append(y.pitch.midi)
        for z in range(1, 2):
            inter = midiNotes[z] - midiNotes[z-1]
            ints.append(inter)
        for x in ints:
            song_ints.append(x)
    print(song_ints)
    return song_ints



def intervalStream(songs):
    """gets directed melodic intervals for given list of songs"""
    song_ints = []
    for song in songs:
        allNotes = song.flat.getElementsByClass('Note')
        midiNotes = []
        ints = []
        # print allNotes
        for y in allNotes:
            midiNotes.append(y.midi)
        for z in range(1, len(midiNotes)):
            inter = midiNotes[z] - midiNotes[z-1]
            ints.append(inter)
        song_ints.append(ints)
    # print(song_ints)
    return song_ints


def cosine_similarity(songs):
    for x in songs.values():
        dataSetI.append(x)
    for y in wtc_length.values():
        dataSetII.append(y)
    result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
    print("cosine", result)
    """result for book 1 is 0.35963251176; both books 0.273930506157"""


def interval_sum(sums):
    all_ints = []
    for x in sums:
        ints = []
        for z in x.values():
            ints.append(z)
        all_ints.append(sum(set(ints)))
    return all_ints






def pearson_sim(one, two):
    m = []
    n = []
    for x in one:
        m.append(x)
    for y in two:
        n.append(y)
    result_2 = stats.pearsonr(m, n)
    pl.scatter(m, n)
    pl.title(result_2)
    # pl.ylabel("interval sum")
    # pl.xlabel("canonic success")
    pl.show()
    print("pearson", result_2)


def melody_length(songs):
    list_songs = []
    for root, dirs, files in os.walk(songs):
        for file_name in files:
            path = os.path.join(root, file_name)
            tempStream = converter.parse(path)
            list_songs.append(tempStream)
    for song in list_songs:
        canon_data[list_songs.index(song)] = len(song.flat.notesAndRests)
    X = np.arange(len(canon_data))
    pl.title('Subject Length in Bach\'s WTC')
    pl.ylabel('number of notes and rests')
    pl.xlabel('subjects from WTC')
    pl.bar(X, canon_data.values(), align='center', width=1)
    pl.xticks(X, canon_data.keys())
    ymax = max(canon_data.values()) + 1
    pl.ylim(0, ymax)
    pl.show()
    # print(canon_data)
    return canon_data


def plotData(inData,color):
    for x in wtc_data.values():
        data1.append(x)
    for y in wtc_length.values():
        data2.append(y)
    x,y = zip(*inData)

    xMap = assignIDs(x)
    xAsInts = np.array([xMap[i] for i in x])

    pearR = np.corrcoef(xAsInts,y)[1,0]
    # least squares from:
    # http://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.lstsq.html
    A = np.vstack([xAsInts,np.ones(len(xAsInts))]).T
    m,c = np.linalg.lstsq(A,np.array(y))[0]

    pl.scatter(xAsInts,y,label='Data '+color,color=color)
    pl.plot(xAsInts,xAsInts*m+c,color=color,
             label="Fit %6s, r = %6.2e"%(color,pearR))
    pl.xticks(xMap.values(),xMap.keys())
    pl.legend(loc=3)


# interval_chart(WTC)