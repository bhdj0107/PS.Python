import sys
chk = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 4, 7: 3, 8: 2, 9: 1, 10: 0, 11: 1, 12: 2, 13: 3, 14: 4, 15: 5, 16: 6, 17: 7, 18: 8, 19: 9, 20: 10, 21: 9, 22: 8, 23: 7, 24: 6, 25: 5, 26: 4, 27: 3, 28: 2, 29: 1, 30: 0, 31: 1, 32: 2, 33: 3, 34: 4, 35: 5, 36: 6, 37: 7, 38: 8, 39: 9, 40: 10, 41: 11, 42: 12, 43: 13, 44: 14, 45: 15, 46: 14, 47: 13, 48: 12, 49: 11, 50: 10, 51: 9, 52: 8, 53: 7, 54: 6, 55: 5, 56: 4, 57: 3, 58: 2, 59: 1, 60: 0, 61: 1, 62: 2, 63: 3, 64: 4, 65: 5, 66: 6, 67: 7, 68: 8, 69: 9, 70: 10, 71: 11, 72: 12, 73: 13, 74: 14, 75: 15, 76: 16, 77: 17, 78: 18, 79: 19, 80: 20, 81: 19, 82: 18, 83: 17, 84: 16, 85: 15, 86: 14, 87: 13, 88: 12, 89: 11, 90: 10, 91: 9, 92: 8, 93: 7, 94: 6, 95: 5, 96: 4, 97: 3, 98: 2, 99: 1, 100: 0}

N = int(sys.stdin.readline())
N = N % 100
if chk[N] == 0:
  print(0)
elif chk[N] > 0 and chk[N] <= 5:
  print(1)
elif chk[N] > 5 and chk[N] <= 10:
  print(2)
elif chk[N] > 10 and chk[N] <= 15:
  print(3)
elif chk[N] > 15 and chk[N] <= 20:
  print(4)
