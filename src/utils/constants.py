CLEFS = ['G', 'F']
KEY_SIGNATURES = ['F/d', 'C/a', 'G/e']
TIME_SIGNATURES = ['2/4', '3/4', '4/4', '6/8']
NOTATION_LENGTHS = [2, 4, 8, 16]
PITCHES = [
  'c3', 'd3', 'e3', 'f3', 'g3', 'a3', 'b3',
  'c4', 'd4', 'e4', 'f4', 'g4', 'a4', 'b4',
  'c5', 'd5', 'e5', 'f5', 'g5', 'a5', 'b5'
]

C4_G = 200
PITCH_POSITIONS_IN_G_CLEF = [
  C4_G+105, C4_G+90, C4_G+75, C4_G+60, C4_G+45, C4_G+30, C4_G+15,
  C4_G, C4_G-15, C4_G-30, C4_G-45, C4_G-60, C4_G-75, C4_G-90,
  C4_G-105, C4_G-120, C4_G-135, C4_G-150, C4_G-165, C4_G-180, C4_G-195,
]

C4_F = C4_G - 180
PITCH_POSITIONS_IN_F_CLEF = [
  C4_F+105, C4_F+90, C4_F+75, C4_F+60, C4_F+45, C4_F+30, C4_F+15,
  C4_F, C4_F-15, C4_F-30, C4_F-45, C4_F-60, C4_F-75, C4_F-90,
  C4_F-105, C4_F-120, C4_F-135, C4_F-150, C4_F-165, C4_F-180, C4_F-195,
]
