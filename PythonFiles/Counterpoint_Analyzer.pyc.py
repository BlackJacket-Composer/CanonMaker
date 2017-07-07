from music21 import *
import copy

# song = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Dufay Single Melody.xml'))
# song = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/bad melody.xml'))
# song = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach Subject Art.xml'))
song = stream.Stream(converter.parse('/Users/Daniel/OneDrive/FSU/Fall 2015/Seminar/Final Project/Prolation tests/Bach WTC1 Cmaj.xml'))
prolation_amount = [.25, .5, .75, 1, 1.25, 1.5, 1.75, 2.0]
offset_amount = [0.0, .25, .5, .75, 1.25, 1.5, 1.75, 2.0]
transposition_amount = range(-12, 13)
prolation_dict = {}
offset_dict = {}
transposition_dict = {}
all_dict = {}

"""todo: make a generic "maker" to create scores; have all functions return newMelody; for multi_tester, loop through
newMelody things, then combine parts in "maker", figure out all dict"""

def multi_tester(melody):
    alls = []
    for x in transposition_amount:
        alls.append(transposition_maker(offset_maker(melody, offset_amount), x))
    for thing in alls:
        thing.show()
            # for z in prolation_amount:
                # options = transposition_maker(offset_maker(prolation_maker(melody, z), y), x)
                # options.show()
    #             if (parallel_checker(options)) == False or (resolve_diss(options)) == False:
    #                 # all_dict[options] = False
    #                 print 'false'
    #             elif (parallel_checker(options)) == True and (resolve_diss(options)) == True:
    #                 # all_dict[options] = True
    #                 options.show()
    #                 print 'true'
    # print "all: ", all_dict



def tester(melody, function, amounts, dict):
    for p in amounts:
        tests = intervalStream(score_maker(melody, function(melody, p)))
        if (parallel_checker(tests)) == False or (resolve_diss(tests)) == False:
            dict[p] = False
        elif (parallel_checker(tests)) == True and (resolve_diss(tests)) == True:
            dict[p] = True
    print dict
    return dict


# def retrograde_tester(melody, retrograde)

def transposition_tester(melody, transposition):
    for p in transposition:
        interval_test = intervalStream(score_maker(melody, transpositions(melody, p)))
        if (parallel_checker(interval_test)) == False or (resolve_diss(interval_test)) == False:
            transposition_dict[p] = False
        elif (parallel_checker(interval_test)) == True and (resolve_diss(interval_test)) == True:
            transposition_dict[p] = True
    print "transposition: ", transposition_dict
    return transposition_dict


def offset_tester(melody, offset):
    for p in offset:
        interval_test = intervalStream(offset_maker(melody, p))
        if (parallel_checker(interval_test)) == False or (resolve_diss(interval_test)) == False:
            offset_dict[p] = False
        elif (parallel_checker(interval_test)) == True and (resolve_diss(interval_test)) == True:
            offset_dict[p] = True
    print "offset: ", offset_dict
    return offset_dict


def prolation_tester(melody, time):
    for p in time:
        interval_test = intervalStream(prolation_maker(melody, p))
        if (parallel_checker(interval_test)) == False or (resolve_diss(interval_test)) == False:
            prolation_dict[p] = False
        elif (parallel_checker(interval_test)) == True and (resolve_diss(interval_test)) == True:
            prolation_dict[p] = True
    print "prolation: ", prolation_dict
    return prolation_dict


def score_maker(melody, function):
    score = stream.Score(id='canon')
    p1 = stream.Part(id='melody')
    p1.append(melody)
    score.insert(0, p1)
    p2 = stream.Part(id='canon')
    p2.append(function)
    score.insert(p2)
    return score


def transposition_maker(melody, transposition):
    score = stream.Score(id='prolation canon')
    p1 = stream.Part(id='melody')
    p1.append(melody)
    score.insert(0, p1)
    p2 = stream.Part(id='canon')
    p2.append(transpositions(melody, transposition))
    score.insert(0, p2)
    # score.show()
    return score


def transpositions(melody, transposition):
    newMelody = copy.deepcopy(melody)
    n = newMelody.flat.getElementsByClass("Note")
    for x in n:
        x.midi += transposition
    return newMelody


def prolation_maker(melody, time):
    regMelody = copy.deepcopy(melody)
    proMelody = copy.deepcopy(melody)
    score = stream.Score(id='prolation canon')
    p1 = stream.Part(id='melody')
    p1.append(regMelody)
    score.insert(0, p1)
    p2 = stream.Part(id='canon')
    p2.append(prolations(proMelody, time))
    score.insert(0, p2)
    # score.show()
    return score


def offsets(melody, offset):
    p2 = stream.Stream()
    newMelody = melody.flat.notesAndRests
    p2.insertAndShift(offset, newMelody)
    p2.show()
    return p2


def prolations(melody, time):
    newMelody = copy.deepcopy(melody)
    prolation = stream.Stream()
    for n in newMelody.flat.notesAndRests:
        n.quarterLength = (n.quarterLength * time)
        prolation.append(n)
    return prolation


def intervalStream(element):
    # harms = copy.deepcopy(melody)
    chords = element
    # chords = prolation_maker(harms, element)
    harmonies = chords.chordify(removeRedundantPitches=False)
    harm = harmonies.flat.getElementsByClass('Chord')
    intervals = []
    final_ints = []
    for x in harm:
        if len(x)==2:
            intervals.append(x)
    for x, y in intervals:
        final_ints.append(interval.Interval(noteStart=x, noteEnd=y))
    # print final_ints
    # print len(final_ints)
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
        # else:
        #     print "fine"
    print "parallel fifths: ", parallel_fifths, "parallel octaves: ", parallel_octaves
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

# prolation_maker(song)
# print intervalStream(song)
# resolve_diss(intervalStream(song))
# parallel_checker(intervalStream(song))
# prolation_tester(song, prolation_amount)
# transposition_tester(song, transposition_amount)
# offset_tester(song, offset_amount)
# intervalStream(song, .5)
# multi_tester(song)
