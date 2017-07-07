from music21 import *
import copy
import numpy as np
import pylab as pl
import os



WTC = '/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Bach WTC Subjects/'
wtc1_Bfmin = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Bfmin.xml')
Josquin = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Josquin.xml')

# prolation_amount = [.3333333, .5, .66666666, 1, 1.5, 2, 3]
# prolation_amount = [.5, 1, 1.5, 2]
prolation_amount = [1]
# offset_amount = [0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
# offset_amount = [0, 1, 2, 3, 4]
transposition_amount = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
# transposition_amount = [1]
prolation_dict = {}
offset_dict = {}
transposition_dict = {}
all_dict = {}
corpus_dict = {}
a = corpus.getComposer('palestrina')


def comparison(songs):
    list_songs = []
    for root, dirs, files in os.walk(songs):
        for file_name in files:
            path = os.path.join(root, file_name)
            tempStream = converter.parse(path)
            list_songs.append(tempStream)
    for song in list_songs:
        corpus_dict[list_songs.index(song)] = multi_tester(song)
    X = np.arange(len(corpus_dict))
    pl.title('Canon Success in Bach\'s WTC')
    pl.ylabel('number of canons')
    pl.xlabel('subjects from WTC')
    pl.bar(X, corpus_dict.values(), align='center', width=0.5)
    pl.xticks(X, corpus_dict.keys())
    ymax = max(corpus_dict.values()) + 1
    pl.ylim(0, ymax)
    pl.show()
    print(corpus_dict)


def multi_tester(melody):
    alls = []
    trues = []
    for x in transposition_amount:
        for y in prolation_amount:
            for z in range(int(melody.flat.notesAndRests.quarterLength - 2)):
            # for z in range(0, 1):
                alls.append(score_maker(melody, offsets(prolations(d_transpositions(melody, x), y), z)))
    for p in alls:
        tests = intervalStream(p)
        if (parallel_checker(tests)) == False or (resolve_diss(tests)) == False:
            all_dict[p] = False
        elif (parallel_checker(tests)) == True and (resolve_diss(tests)) == True:
            all_dict[p] = True
            trues.append(p)
            # p.show()
    print("true: ", len(trues))
    print("total: ", len(alls))
    percentage = float(len(trues)) / float(len(alls)) * 100.0
    print(percentage, "percent")
    print(len(trues))
    return len(trues)
    # return percentage
    # print all_dict
    # return all_dict


def tester(melody, function, amounts, dict):
    for p in amounts:
        tests = intervalStream(score_maker(melody, function(melody, p)))
        if (parallel_checker(tests)) == False or (resolve_diss(tests)) == False:
            dict[p] = False
        elif (parallel_checker(tests)) == True and (resolve_diss(tests)) == True:
            dict[p] = True
    print(function, amounts, dict)
    return dict


# def retrograde_tester(melody, retrograde)


def score_maker(melody, function):
    """puts the altered melody in a score below the original"""
    score = stream.Score(id='canon')
    p1 = stream.Part(id='melody')
    p1.append(melody)
    score.insert(p1)
    score.insert(function)
    return score


def transpositions(melody, transposition):
    newMelody = copy.deepcopy(melody)
    for x in newMelody.flat.notes:
        x.pitch.midi += transposition
    return newMelody


def d_transpositions(melody, transposition):
    newMelody = copy.deepcopy(melody)
    tStream = newMelody.parts[0].flat.transpose(interval.GenericInterval(transposition))
    for n in tStream.notes:
        n.pitch.accidental = melody.flat.getContextByClass(key.KeySignature).accidentalByStep(n.step)
    return tStream


def offsets(melody, offset):
    s = melody.flat
    s.shiftElements(offset, classFilterList=[note.Note, note.Rest])
    return s


def prolations(melody, time):
    newMelody = copy.deepcopy(melody)
    prolation = stream.Stream()
    for n in newMelody.flat.notesAndRests:
        n.quarterLength = (n.quarterLength * time)
        prolation.append(n)
    return prolation


def intervalStream(element):
    """chordifys the two melodies and gets a list of intervals"""
    chords = element
    harmonies = chords.chordify(removeRedundantPitches=False)
    harm = harmonies.flat.getElementsByClass('Chord')
    intervals = []
    final_ints = []
    for x in harm:
        if len(x) == 2:
            intervals.append(x)
    for x, y in intervals:
        final_ints.append(abs((x.pitch.midi - y.pitch.midi) % 12))
    return final_ints


def parallel_checker(intervals):
    checker = 1
    parallel_fifths = 0
    parallel_octaves = 0
    thirds = [3, 4]
    sixths = [8, 9]
    for x in range(1, len(intervals)):
        if intervals[x] == 7 and intervals[x - 1] == 7:
            # print "parallel fifths"
            checker += 1
            parallel_fifths += 1
        elif intervals[x] == 0 and intervals[x - 1] == 0:
            # print "parallel octaves"
            checker += 1
            parallel_octaves += 1
    for x in range(3, len(intervals)):
        if intervals[x - 3] in thirds and intervals[x - 2] in thirds and intervals[x - 1] in thirds \
                and intervals[x] in thirds:
            checker += 1
            # print "3 motion too similar"
        elif intervals[x - 3] in sixths and intervals[x - 2] in sixths and intervals[x - 1] in sixths \
                and intervals[x] in sixths:
            checker += 1
            # print "6 motion too similar"
    if checker > 1:
        return False
    else:
        return True


def resolve_diss(intervals):
    checker = 1
    seconds = [1, 2]
    sevenths = [10, 11]
    dissonant = [1, 2, 5, 6, 10, 11]
    for x in range(1, len(intervals)):
        if intervals[x - 1] in dissonant and intervals[x] in dissonant:
            checker += 1
        elif intervals[x - 1] == 6 and intervals[x] != (4 or 3 or 9 or 8):
            checker += 1
            # print "bad tritone resolution"
        elif intervals[x - 1] == 5 and intervals[x] != (4 or 3 or 7 or 8 or 9):
            checker += 1
        elif intervals[x - 1] == 5 and intervals[x] != (4 or 3 or 7 or 8 or 9):
            checker += 1
        elif intervals[x - 1] in seconds and intervals[x] != (4 or 3 or 0):
            checker += 1
            # print "bad 2, bad 2"
        elif intervals[x - 1] == sevenths and intervals[x] != (0 or 9 or 8):
            checker += 1
           # print "bad 7, bad 7"
    if checker > 1:
        return False
    else:
        return True

comparison(WTC)