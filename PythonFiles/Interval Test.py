from music21 import *
import copy

Dufay2 = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Dufay Puzzle.xml')
Dufay = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Dufay Single Melody.xml')
Something = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/bad melody.xml')
Art_Subject = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach Subject Art.xml')
wtc1_Cmaj = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Cmaj.xml')
wtc1_Cmin = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Cmin.xml')
wtc1_Csmaj = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Csmaj.xml')
wtc1_Bfmin = converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Bfmin.xml')
# prolation_amount = [.3333333, .5, .66666666, 1, 1.5, 2, 3]
prolation_amount = [.5, 1, 1.5, 2]
# offset_amount = [0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
offset_amount = [0, 1, 2, 3, 4]
transposition_amount = range(-12, 13)
prolation_dict = {}
offset_dict = {}
transposition_dict = {}
all_dict = {}


def multi_tester(melody):
    alls = []
    trues = []
    for x in transposition_amount:
        for y in prolation_amount:
            for z in offset_amount:
                alls.append(score_maker(melody, offsets(prolations(transpositions(melody, x), y), z)))
    for p in alls:
        tests = intervalStream(p)
        if (parallel_checker(tests)) == False or (resolve_diss(tests)) == False:
            all_dict[p] = False
        elif (parallel_checker(tests)) == True and (resolve_diss(tests)) == True:
            all_dict[p] = True
            trues.append(p)
            p.show()
    # print "true: ", len(trues)
    # print "total: ", len(alls)
    # print float(len(trues)) / float(len(alls)) * 100.0, "percent"
    # print all_dict
    # return all_dict


def tester(melody, function, amounts, dict):
    for p in amounts:
        tests = intervalStream(score_maker(melody, function(melody, p)))
        if (parallel_checker(tests)) == False or (resolve_diss(tests)) == False:
            dict[p] = False
        elif (parallel_checker(tests)) == True and (resolve_diss(tests)) == True:
            dict[p] = True
    # print function, amounts, dict
    return dict


# def retrograde_tester(melody, retrograde)


def score_maker(melody, function):
    """puts the altered melody in a score below the original"""
    score = stream.Score(id='canon')
    p1 = stream.Part(id='melody')
    p1.append(melody)
    score.insert(p1)
    # function.show()
    # p2 = stream.Part(id='canon')
    # p2.append(function)
    # p2.show('text')
    score.insert(function)
    # score.show('text')
    # score.show()
    return score


def transpositions(melody, transposition):
    newMelody = copy.deepcopy(melody)
    n = newMelody.flat.getElementsByClass("Note")
    for x in n:
        x.pitch.midi += transposition
    return newMelody


def offsets(melody, offset):
    p2 = stream.Stream()
    aMelody = copy.deepcopy(melody)
    newMelody = aMelody.flat.notesAndRests
    k = aMelody.flat.getKeySignatures()
    # p2.insertAndShift(offset, newMelody)
    p2.insert((offset + 1), newMelody)
    p2.insert(k)
    # p2.show()
    return p2


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
        if len(x)==2:
            intervals.append(x)
    for x, y in intervals:
        final_ints.append(abs((x.pitch.midi - y.pitch.midi) % 12))
    return final_ints


def parallel_checker(intervals):
    checker = 1
    parallel_fifths = 0
    parallel_octaves = 0
    for x in range(1, len(intervals)):
        if intervals[x] == 7 and intervals[x-1] == 7:
            # print "parallel fifths"
            checker += 1
            parallel_fifths += 1
        elif intervals[x] == 0 and intervals[x-1] == 0:
            # print "parallel octaves"
            checker += 1
            parallel_octaves += 1
    for x in range(4, len(intervals)):
        if intervals[x-4] == intervals[x-3] and intervals[x-4] == intervals[x-2] and intervals[x-4] == intervals[x-1] \
                and intervals[x-4] == intervals[x]:
            checker += 1
            # print "motion too similar"
        # else:
        #     print "fine"
    # print "parallel fifths: ", parallel_fifths, "parallel octaves: ", parallel_octaves
    if checker > 1:
        return False
    else:
        return True


def resolve_diss(intervals):
    checker = 1
    consonant = [0, 3, 4, 7, 8, 9]
    dissonant = [1, 2, 5, 10, 11]
    for x in range(1, len(intervals)):
        if intervals[x-1] in consonant and intervals[x] in consonant:
            checker += 0
        elif intervals[x-1] in dissonant and intervals[x] in dissonant:
            checker += 1
        elif intervals[x-1] == 6 and (intervals[x] == 4 or intervals[x] == 3):
            # print "resolved tritone"
            checker += 0
        elif intervals[x-1] == 6 and (intervals[x] != 4 or intervals[x] != 3):
            checker += 1
            # print "bad tritone resolution"
        elif intervals[x-1] in dissonant and intervals[x] in consonant:
            # print "dissonance resolved"
            checker += 0
    if checker > 1:
        return False
    else:
        return True


# for x in corpus.getComposer('bach', fileExtensions=None):
#     y = converter.parse(x)
#     z = y.parts[0]
#     multi_tester(z)