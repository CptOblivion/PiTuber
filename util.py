def mapRange(left, right, val, range):
  return min(1, max(0, (val - left) / (right - left))) * range