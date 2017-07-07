import matplotlib.pyplot as plt
import numpy as np
#
"""Routine Ideal"""
# plt.plot([0,1,2,3,4,5,6], 'b-')
# plt.plot([6,5,4,3,2,1,0], 'r-')
# # plt.plot([3,3,3.5], [2,3,2.5], 'go')
# plt.title("Example PGTs")
# plt.ylabel('second pulse group')
# plt.xlabel('first pulse group')
# plt.annotate('6-aggregate', xy=(.53, 5.53), xytext=(1, 5.7),
#             arrowprops=dict(facecolor='black', shrink=0.0),
#             )
# plt.annotate('symmetrical meter', xy=(5, 5), xytext=(3, 5.5),
#             arrowprops=dict(facecolor='black', shrink=0.1),
#             )
# plt.annotate('ideal', xy=(3, 2.93), xytext=(2.81, 2),
#             arrowprops=dict(facecolor='black', shrink=0.1),
#             )
# plt.grid(True)
# plt.show()
#
#
# """Someone Pull Me Out of Here"""
# # plt.axis([2, 8, 2, 8])
plt.plot([0,1,2,3,4,5,6, 7, 8, 9, 10], 'b-')
plt.plot([10, 9, 8, 7, 6,5,4,3,2,1,0], 'r-')
plt.plot([5,6,6], [5,5,4], 'go')
plt.title("Transformations in The Pineapple Thief's \"Someone Pull Me Out Of Here\"")
plt.ylabel('second pulse group')
plt.xlabel('first pulse group')
plt.xticks([0,1,2,3,4, 5, 6, 7, 8, 9, 10])
plt.yticks([0,1,2,3,4, 5, 6, 7, 8, 9, 10])
plt.grid(True)
plt.annotate(s='', xy=(6,5), xytext=(5,5), arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.annotate(s='', xy=(6,4), xytext=(6,5), arrowprops=dict(facecolor='black', arrowstyle='<->'))
plt.annotate(s='', xy=(5,5), xytext=(6,4), arrowprops=dict(facecolor='black', arrowstyle='->'))


plt.show()
#
# """Routine"""
# plt.plot([0,1,2,3,4,5,6], 'b-')
# plt.plot([6,5,4,3,2,1,0], 'r-')
# plt.plot([3,3,3.5], [2,3,2.5], 'go')
# plt.title("Transformations in Steven Wilson's \"Routine\"")
# plt.ylabel('second pulse group')
# plt.xlabel('first pulse group')
# plt.grid(True)
# plt.annotate(s='', xy=(3,3), xytext=(3,2), arrowprops=dict(facecolor='black', arrowstyle='->'))
# plt.annotate(s='', xy=(3.5,2.5), xytext=(3,3), arrowprops=dict(facecolor='black', arrowstyle='->'))
# plt.annotate(s='', xy=(3,2), xytext=(3.5,2.5), arrowprops=dict(facecolor='black', arrowstyle='->'))
# plt.show()
#
# """The Sound of Muzak"""
# plt.axis([2, 6, 2, 6])
# plt.plot([3, 4], [4, 4], 'go')
# plt.plot([0,1,2,3,4,5,6,7,8], 'b-')
# plt.plot([8,7,6,5,4,3,2,1,0], 'r-')
# plt.title("Transformations in Porcupine Tree's \"The Sound of Muzak\"")
# plt.ylabel('second pulse group')
# plt.xlabel('first pulse group')
# plt.grid(True)
# plt.annotate(s='', xy=(3,4), xytext=(4,4), arrowprops=dict(facecolor='black', arrowstyle='<->'))
# plt.show()
#
# """The Blind House"""
# plt.figure()
# plt.axis([0, 4, 0, 4])
# plt.xticks([0,1,2,3,4])
# plt.yticks([0,1,2,3,4])
# plt.plot([3, 2], [2, 2], 'go')
# plt.plot([0,1,2,3,4], 'b-')
# plt.plot([4,3,2,1,0], 'r-')
# plt.title("Transformations in Porcupine Tree's \"The Blind House\"")
# plt.ylabel('second pulse group')
# plt.xlabel('first pulse group')
# plt.grid(True)
# plt.annotate(s='', xy=(3,2), xytext=(2,2), arrowprops=dict(facecolor='black', arrowstyle='<->'))
# plt.show()
#
# """Once"""
# plt.axis([4, 12, 4, 12])
# plt.plot([9, 8], [7, 8], 'go')
# plt.plot([0,1,2,3,4,5,6,7,8,9,10,11,12], 'b-')
# plt.plot([16,15,14,13,12,11,10,9,8,7,6,5,4], 'r-')
# plt.title("Transformations in Blackfield's \"Once\"")
# plt.ylabel('second pulse group')
# plt.xlabel('first pulse group')
# plt.grid(True)
# plt.annotate(s='', xy=(9,7), xytext=(8,8), arrowprops=dict(facecolor='black', arrowstyle='<->'))
# plt.show()
#
# """Little Man"""
# # plt.axis([1, 5, 1, 5])
# plt.xticks([0,1,2,3,4,5,6])
# plt.yticks([0,1,2,3,4,5,6])
# plt.plot([3, 3, 2], [3, 2, 3], 'go')
# plt.plot([0,1,2,3,4,5,6], 'b-')
# plt.plot([6,5,4,3,2,1,0], 'r-')
# plt.title("Transformations in The Pineapple Thief's \"Little Man\"")
# plt.ylabel('second pulse group')
# plt.xlabel('first pulse group')
# plt.grid(True)
# plt.annotate(s='', xy=(3,2), xytext=(3,3), arrowprops=dict(facecolor='black', arrowstyle='->'))
# plt.annotate(s='', xy=(2,3), xytext=(3,2), arrowprops=dict(facecolor='black', arrowstyle='<->'))
# plt.annotate(s='', xy=(3,3), xytext=(2,3), arrowprops=dict(facecolor='black', arrowstyle='->'))
# plt.show()
#
# """All The Wars"""
# plt.axis([0, 8, 0, 8])
# plt.plot([4,4], [4,3], 'go')
# plt.plot([0,1,2,3,4,5,6,7,8], 'b-')
# plt.plot([8,7,6,5,4,3,2,1,0], 'r-')
# plt.title("Transformations in The Pineapple Thief's \"All The Wars\"")
# plt.ylabel('second pulse group')
# plt.xlabel('first pulse group')
# plt.grid(True)
# plt.annotate(s='', xy=(4,3), xytext=(4,4), arrowprops=dict(facecolor='black', arrowstyle='<->'))
# plt.show()
#
# """Raven"""
# # plt.axis([1, 5, 1, 5])
# plt.plot([3, 3], [4, 3], 'go')
# plt.plot([0,1,2,3,4,5,6], 'b-')
# plt.plot([6,5,4,3,2,1,0], 'r-')
# plt.title("Transformations in Steven Wilson's \"The Raven That Refused To Sing\"")
# plt.ylabel('second pulse group')
# plt.xlabel('first pulse group')
# plt.grid(True)
# plt.annotate(s='', xy=(3,4), xytext=(3,3), arrowprops=dict(facecolor='black', arrowstyle='<->'))
# plt.show()