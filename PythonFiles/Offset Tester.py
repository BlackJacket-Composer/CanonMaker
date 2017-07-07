from music21 import *
import copy

Dufay2 = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Dufay Puzzle.xml'))
Dufay = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Dufay Single Melody.xml'))
Something = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/bad melody.xml'))
Art_Subject = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach Subject Art.xml'))
wtc1_Cmaj = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Cmaj.xml'))
wtc1_Cmin = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Cmin.xml'))
wtc1_Csmaj = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Csmaj.xml'))
# prolation_amount = [.5, 1, 1.5, 2.0]
prolation_amount = [1]
offset_amount = [0, .5, 1, 1.5, 2, 2.5, 3, 3.5, 4]
transposition_amount = range(-12, 13)
prolation_dict = {}
offset_dict = {}
transposition_dict = {}
all_dict = {}

"""todo: make a generic "maker" to create scores; have all functions return newMelody; for multi_tester, loop through
newMelody things, then combine parts in "maker", figure out all dict"""


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
    print("true: ", len(trues))
    print("total: ", len(alls))
    print(all_dict)
    # return all_dict


def tester(melody, function, amounts, dict):
    for p in amounts:
        tests = intervalStream(score_maker(melody, function(melody, p)))
        if (parallel_checker(tests)) == False or (resolve_diss(tests)) == False:
            dict[p] = False
        elif (parallel_checker(tests)) == True and (resolve_diss(tests)) == True:
            dict[p] = True
    print(dict)
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
    # p2.insertAndShift(offset, newMelody)
    p2.insert(offset, newMelody)
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
        final_ints.append(interval.Interval(noteStart=x, noteEnd=y))
    # print intervals
    return final_ints


def parallel_checker(intervals):
    checker = 1
    parallel_fifths = 0
    parallel_octaves = 0
    for x in range(1, len(intervals)):
        if intervals[x] == interval.Interval('P5') and intervals[x-1] == interval.Interval('P5'):
            # print "parallel fifths"
            checker += 1
            parallel_fifths += 1
        elif intervals[x] == interval.Interval('P8') and intervals[x-1] == interval.Interval('P8'):
            # print "parallel octaves"
            checker += 1
            parallel_octaves += 1
    for x in range(4, len(intervals)):
        if intervals[x-4] == intervals[x-3] and intervals[x-4] == intervals[x-2] and intervals[x-4] == intervals[x-1] and intervals[x-4] == intervals[x]:
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
    for x in range(1, len(intervals)):
        # if intervals[x-1] == (interval.Interval('m2') or interval.Interval('M2') or interval.Interval('P4') or interval.Interval('m7') or interval.Interval('M7') or interval.Interval('m9') or interval.Interval('M9')) and intervals[x] == (interval.Interval('m2') or interval.Interval('M2') or interval.Interval('P4') or interval.Interval('m7') or interval.Interval('M7') or interval.Interval('m9') or interval.Interval('M9')):
        if intervals[x-1].isConsonant() == False and intervals[x].isConsonant() == False:
            # print x, "bad boy"
            checker += 1
        elif intervals[x-1].isConsonant() == False and intervals[x].isConsonant() == True:
            # print x, "resolved"
            checker += 0
        else:
            # print x, "fine"
            checker += 0
    if checker > 1:
        return False
    else:
        return True
