from music21 import *
import copy
import numpy as np
import pylab as pl
import os



WTC = '/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Bach WTC Subjects/'
wtc1_Bfmin = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Bfmin.xml')
twinkle = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Twinkle.xml')
twink = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/TwinkleShort.xml')
row = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/row.xml')
boat = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/realRow.xml')
wtc1_Cmaj = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Cmaj.xml')


# prolation_amount = [.3333333, .5, .66666666, 1, 1.5, 2, 3]
# prolation_amount = [1, 1.25, 1.5, 1.75, 2, .75, .5]
prolation_amount = [1]
# offset_amount = [0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
# offset_amount = [0, 1, 2, 3, 4]
# transposition_amount = [-8, -7, -6, -5, -4, -3, -2, 1, 2, 3, 4, 5, 6, 7, 8]
transposition_amount = [-8, -7, -6, -5, -4, -3, -2, 1, 2, 3, 4, 5, 6, 7, 8]
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
    # s = stream.Stream()
    for x in transposition_amount:
        for y in prolation_amount:
            for z in range(int(melody.flat.notesAndRests.quarterLength / 2)):
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
    # s = stream.Score()
    # for x in range(1, len(trues)):
    #     f1 = trues[x-1]
    #     f11 = trues[x]
    #     if s.duration.quarterLength <1:
    #         s.insert(0, copy.deepcopy(f1[0]))
    #         s.insert(0, copy.deepcopy(f1[1]))
    #         s[0].insertAndShift(s.duration.quarterLength, copy.deepcopy(f11[0]))
    #         s[1].insertAndShift(s[1].duration.quarterLength, copy.deepcopy(f11[1]))
    #     else:
    #         s[0].insertAndShift(s[0].duration.quarterLength, copy.deepcopy(f11[0]))
    #         s[1].insertAndShift(s[1].duration.quarterLength, copy.deepcopy(f11[1]))
    # s.show()
    # s.show('midi')
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
    score = stream.Score(id='canon')
    p1 = stream.Part(id='melody')
    p1.append(melody)
    w = stream.Stream()
    x = stream.Stream(function)
    for n in x.flat.notesAndRests:
        if w.duration.quarterLength + n.duration.quarterLength <= melody.duration.quarterLength:
            w.append(n)
    if w.duration.quarterLength < melody.duration.quarterLength:
        w.append(note.Rest(quarterLength=abs(w.duration.quarterLength - melody.duration.quarterLength)))
    p2 = stream.Part(id='canon')
    p2.append(w)
    # score.insert(0, p1)
    score.insert(0, p2)
    return score


# def transpositions(melody, transposition):
#     newMelody = copy.deepcopy(melody)
#     for x in newMelody.flat.notes:
#         x.pitch.midi += transposition
#     return newMelody


def d_transpositions(melody, transposition):
    newMelody = copy.deepcopy(melody)
    tStream = newMelody.parts[0].flat.transpose(interval.GenericInterval(transposition))
    for n in tStream.notes:
        n.pitch.accidental = melody.flat.getContextByClass(key.KeySignature).accidentalByStep(n.step)
    return tStream


def offsets(melody, offset):
    s = copy.deepcopy(melody)
    s.insertAndShift(note.Rest(quarterLength=offset))
    # m = stream.Stream()
    # for n in s.flat.notesAndRests:
    #     if m.duration.quarterLength + n.duration.quarterLength <= melody.duration.quarterLength:
    #         m.append(n)
    # r = note.Rest(quarterLength=1)
    # if m.duration.quarterLength < melody.duration.quarterLength:
    #     m.append(r)
    return s


# def prolations(melody, time):
#     newMelody = copy.deepcopy(melody)
#     prolation = stream.Stream()
#     for n in newMelody.flat.notesAndRests:
#         n.quarterLength = (n.quarterLength * time)
#         prolation.append(n)
#     return prolation


def prolations(melody, time):
    newMelody = copy.deepcopy(melody)
    prolation = stream.Stream()
    # shorten = stream.Stream()
    for n in newMelody.flat.notesAndRests:
        n.quarterLength = (n.quarterLength * time)
        prolation.append(n)
    # for x in prolation.flat.notesAndRests:
    #     if shorten.duration.quarterLength + x.duration.quarterLength <= melody.duration.quarterLength:
    #         shorten.append(x)
    # r = note.Rest(quarterLength=1)
    # if shorten.duration.quarterLength < melody.duration.quarterLength:
    #     shorten.append(r)
    return prolation


def intervalStream(element):
    """chordifys the two melodies and gets a list of intervals"""
    chords = element
    harmonies = chords.chordify(removeRedundantPitches=True)
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
            # print("parallel fifths")
            checker += 1
            parallel_fifths += 1
        elif intervals[x] == 0 and intervals[x - 1] == 0:
            # print("parallel octaves")
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
            # print('dissonant buddy')
        elif intervals[x - 1] == 6 and intervals[x] != (4 or 3 or 9 or 8):
            checker += 1
            print("bad tritone resolution")
        elif intervals[x - 1] == 5 and intervals[x] != (4 or 3 or 7 or 8 or 9):
            checker += 1
        elif intervals[x - 1] in seconds and intervals[x] != (4 or 3 or 0):
            checker += 1
            # print("bad 2, bad 2")
        elif intervals[x - 1] == sevenths and intervals[x] != (0 or 9 or 8):
            checker += 1
            print("bad 7, bad 7")
    if checker > 1:
        return False
    else:
        return True
#
comparison(WTC)
# multi_tester(wtc1_Bfmin)
