import csv

# Replace this variable with your full dataset string
text = """RANK
ADP
PROJ
1
player-headshot
J. Daniels
WAS
QB-1
Bye: 12
2.7
ADP
$21
$ VALUE
Unlock
PROJ
2
player-headshot
L. Jackson
BAL
QB-2
Bye: 7
3.6
ADP
$24
$ VALUE
Unlock
PROJ
3
player-headshot
J. Allen
BUF
QB-3
Bye: 7
1.8
ADP
$21
$ VALUE
Unlock
PROJ
4
player-headshot
J. Hurts
PHI
QB-4
Bye: 9
7.2
ADP
$17
$ VALUE
Unlock
PROJ
5
player-headshot
J. Burrow
CIN
QB-5
Bye: 10
5.9
ADP
$16
$ VALUE
Unlock
PROJ
6
player-headshot
P. Mahomes
KC
QB-6
Bye: 10
14.8
ADP
$10
$ VALUE
Unlock
PROJ
7
player-headshot
B. Nix
DEN
QB-7
Bye: 12
23.1
ADP
$3
$ VALUE
Unlock
PROJ
8
player-headshot
C. Williams
CHI
QB-8
Bye: 5
22.6
ADP
$5
$ VALUE
Unlock
PROJ
9
player-headshot
J. Chase
CIN
WR-1
Bye: 10
4.1
ADP
$59
$ VALUE
Unlock
PROJ
10
player-headshot
B. Robinson
ATL
RB-1
Bye: 5
8.2
ADP
$57
$ VALUE
Unlock
PROJ
11
player-headshot
J. Gibbs
DET
RB-2
Bye: 8
10.8
ADP
$55
$ VALUE
Unlock
PROJ
12
player-headshot
M. Nabers
NYG
WR-2
Bye: 14
11.4
ADP
$44
$ VALUE
Unlock
PROJ
13
player-headshot
B. Purdy
SF
QB-9
Bye: 14
51.6
ADP
$3
$ VALUE
Unlock
PROJ
14
player-headshot
J. Jefferson
MIN
WR-3
Bye: 6
5.8
ADP
$56
$ VALUE
Unlock
PROJ
15
player-headshot
B. Thomas Jr.
JAX
WR-4
Bye: 8
16.3
ADP
$41
$ VALUE
Unlock
PROJ
16
player-headshot
P. Nacua
LAR
WR-5
Bye: 8
17.5
ADP
$45
$ VALUE
Unlock
PROJ
17
player-headshot
C. Stroud
HOU
QB-10
Bye: 6
29.7
ADP
$3
$ VALUE
Unlock
PROJ
18
player-headshot
J. Herbert
LAC
QB-11
Bye: 12
25.8
ADP
$2
$ VALUE
Unlock
PROJ
19
player-headshot
J. McCarthy
MIN
QB-12
Bye: 6
55.1
ADP
$1
$ VALUE
Unlock
PROJ
20
player-headshot
B. Mayfield
TB
QB-13
Bye: 9
47.5
ADP
$6
$ VALUE
Unlock
PROJ
21
A. Jeanty
LV
RB-3
Bye: 8
13.3
ADP
$44
$ VALUE
Unlock
PROJ
22
player-headshot
B. Bowers
LV
TE-1
Bye: 8
9.9
ADP
$32
$ VALUE
Unlock
PROJ
23
player-headshot
C. Lamb
DAL
WR-6
Bye: 10
11.9
ADP
$54
$ VALUE
Unlock
PROJ
24
player-headshot
A. St. Brown
DET
WR-7
Bye: 8
15.6
ADP
$42
$ VALUE
Unlock
PROJ
25
player-headshot
D. London
ATL
WR-8
Bye: 5
21.7
ADP
$41
$ VALUE
Unlock
PROJ
26
player-headshot
J. Love
GB
QB-14
Bye: 5
40.5
ADP
$2
$ VALUE
Unlock
PROJ
27
player-headshot
N. Collins
HOU
WR-9
Bye: 6
20.3
ADP
$40
$ VALUE
Unlock
PROJ
28
player-headshot
L. McConkey
LAC
WR-10
Bye: 12
23.2
ADP
$37
$ VALUE
Unlock
PROJ
29
player-headshot
K. Murray
ARI
QB-15
Bye: 8
46.5
ADP
$3
$ VALUE
Unlock
PROJ
30
player-headshot
D. Maye
NE
QB-16
Bye: 14
29.3
ADP
$1
$ VALUE
Unlock
PROJ
31
player-headshot
D. Achane
MIA
RB-4
Bye: 12
28.8
ADP
$38
$ VALUE
Unlock
PROJ
32
player-headshot
T. Lawrence
JAX
QB-17
Bye: 8
63.5
ADP
$3
$ VALUE
Unlock
PROJ
33
player-headshot
T. McBride
ARI
TE-2
Bye: 8
19.7
ADP
$25
$ VALUE
Unlock
PROJ
34
player-headshot
B. Irving
TB
RB-5
Bye: 9
31.4
ADP
$38
$ VALUE
Unlock
PROJ
35
player-headshot
M. Harrison Jr.
ARI
WR-11
Bye: 8
27.0
ADP
$27
$ VALUE
Unlock
PROJ
36
player-headshot
J. Goff
DET
QB-18
Bye: 8
65.8
ADP
$2
$ VALUE
Unlock
PROJ
37
player-headshot
J. Fields
NYJ
QB-19
Bye: 9
86.5
ADP
$2
$ VALUE
Unlock
PROJ
38
O. Hampton
LAC
RB-6
Bye: 12
26.7
ADP
$17
$ VALUE
Unlock
PROJ
39
player-headshot
J. Smith-Njigba
SEA
WR-12
Bye: 8
32.6
ADP
$31
$ VALUE
Unlock
PROJ
40
player-headshot
G. Wilson
NYJ
WR-13
Bye: 9
34.4
ADP
$34
$ VALUE
Unlock
PROJ
41
player-headshot
M. Penix Jr.
ATL
QB-20
Bye: 5
68.3
ADP
$1
$ VALUE
Unlock
PROJ
42
player-headshot
A. Brown
PHI
WR-14
Bye: 9
33.1
ADP
$34
$ VALUE
Unlock
PROJ
43
T. McMillan
CAR
WR-15
Bye: 14
37.6
ADP
$18
$ VALUE
Unlock
PROJ
44
player-headshot
T. Higgins
CIN
WR-16
Bye: 10
44.4
ADP
$33
$ VALUE
Unlock
PROJ
45
player-headshot
S. Barkley
PHI
RB-7
Bye: 9
17.5
ADP
$56
$ VALUE
Unlock
PROJ
46
T. Hunter
JAX
WR-17
Bye: 8
35.5
ADP
$7
$ VALUE
Unlock
PROJ
47
player-headshot
K. Walker III
SEA
RB-8
Bye: 8
64.7
ADP
$21
$ VALUE
Unlock
PROJ
48
player-headshot
B. Hall
NYJ
RB-9
Bye: 9
35.5
ADP
$32
$ VALUE
Unlock
PROJ
49
player-headshot
C. Brown
CIN
RB-10
Bye: 10
53.2
ADP
$35
$ VALUE
Unlock
PROJ
50
C. Ward
TEN
QB-21
Bye: 10
N/A
ADP
$1
$ VALUE
Unlock
PROJ
51
player-headshot
J. Taylor
IND
RB-11
Bye: 11
38.0
ADP
$34
$ VALUE
Unlock
PROJ
52
player-headshot
J. Cook
BUF
RB-12
Bye: 7
52.8
ADP
$23
$ VALUE
Unlock
PROJ
53
player-headshot
D. Smith
PHI
WR-18
Bye: 9
57.7
ADP
$25
$ VALUE
Unlock
PROJ
54
player-headshot
K. Williams
LAR
RB-13
Bye: 8
41.7
ADP
$29
$ VALUE
Unlock
PROJ
55
player-headshot
R. Rice
KC
WR-19
Bye: 10
43.5
ADP
$28
$ VALUE
Unlock
PROJ
56
J. Dart
NYG
QB-22
Bye: 14
98.6
ADP
N/A
$ VALUE
Unlock
PROJ
57
player-headshot
R. Odunze
CHI
WR-20
Bye: 5
56.5
ADP
$8
$ VALUE
Unlock
PROJ
58
player-headshot
T. Tagovailoa
MIA
QB-23
Bye: 12
105.3
ADP
$1
$ VALUE
Unlock
PROJ
59
player-headshot
B. Young
CAR
QB-24
Bye: 14
81.6
ADP
N/A
$ VALUE
Unlock
PROJ
60
player-headshot
X. Worthy
KC
WR-21
Bye: 10
59.4
ADP
$23
$ VALUE
Unlock
PROJ
61
player-headshot
J. Williams
DET
WR-22
Bye: 8
78.0
ADP
$22
$ VALUE
Unlock
PROJ
62
player-headshot
S. LaPorta
DET
TE-3
Bye: 8
39.4
ADP
$10
$ VALUE
Unlock
PROJ
63
player-headshot
Z. Flowers
BAL
WR-23
Bye: 7
65.7
ADP
$19
$ VALUE
Unlock
PROJ
64
T. Shough
NO
QB-25
Bye: 11
149.9
ADP
N/A
$ VALUE
Unlock
PROJ
65
player-headshot
J. Jacobs
GB
RB-14
Bye: 5
47.9
ADP
$36
$ VALUE
Unlock
PROJ
66
player-headshot
D. Prescott
DAL
QB-26
Bye: 10
76.1
ADP
$7
$ VALUE
Unlock
PROJ
67
player-headshot
J. Addison
MIN
WR-24
Bye: 6
75.5
ADP
$13
$ VALUE
Unlock
PROJ
68
player-headshot
D. Moore
CHI
WR-25
Bye: 5
71.3
ADP
$24
$ VALUE
Unlock
PROJ
69
player-headshot
A. Richardson
IND
QB-27
Bye: 11
119.1
ADP
N/A
$ VALUE
Unlock
PROJ
70
player-headshot
C. Olave
NO
WR-26
Bye: 11
77.4
ADP
$12
$ VALUE
Unlock
PROJ
71
player-headshot
J. Waddle
MIA
WR-27
Bye: 12
85.4
ADP
$16
$ VALUE
Unlock
PROJ
72
C. Loveland
CHI
TE-4
Bye: 5
68.6
ADP
$1
$ VALUE
Unlock
PROJ
73
player-headshot
D. Metcalf
PIT
WR-28
Bye: 5
74.5
ADP
$24
$ VALUE
Unlock
PROJ
74
player-headshot
G. Kittle
SF
TE-5
Bye: 14
61.3
ADP
$16
$ VALUE
Unlock
PROJ
75
player-headshot
T. McLaurin
WAS
WR-29
Bye: 12
61.4
ADP
$31
$ VALUE
Unlock
PROJ
76
player-headshot
T. Hockenson
MIN
TE-6
Bye: 6
73.5
ADP
$8
$ VALUE
Unlock
PROJ
77
player-headshot
C. McCaffrey
SF
RB-15
Bye: 14
45.1
ADP
$43
$ VALUE
Unlock
PROJ
78
T. Henderson
NE
RB-16
Bye: 14
42.0
ADP
$15
$ VALUE
Unlock
PROJ
79
player-headshot
C. Hubbard
CAR
RB-17
Bye: 14
71.6
ADP
$23
$ VALUE
Unlock
PROJ
80
player-headshot
R. Pearsall
SF
WR-30
Bye: 14
97.9
ADP
$12
$ VALUE
Unlock
PROJ
81
E. Egbuka
TB
WR-31
Bye: 9
70.4
ADP
$3
$ VALUE
Unlock
PROJ
82
T. Warren
IND
TE-7
Bye: 11
58.4
ADP
$3
$ VALUE
Unlock
PROJ
83
player-headshot
G. Pickens
DAL
WR-32
Bye: 10
79.7
ADP
$18
$ VALUE
Unlock
PROJ
84
R. Harvey
DEN
RB-18
Bye: 12
62.4
ADP
$23
$ VALUE
Unlock
PROJ
85
Q. Judkins
CLE
RB-19
Bye: 9
50.0
ADP
$10
$ VALUE
Unlock
PROJ
86
M. Golden
GB
WR-33
Bye: 5
83.3
ADP
$4
$ VALUE
Unlock
PROJ
87
K. Johnson
PIT
RB-20
Bye: 5
67.3
ADP
$9
$ VALUE
Unlock
PROJ
88
player-headshot
T. Kraft
GB
TE-8
Bye: 5
104.2
ADP
$4
$ VALUE
Unlock
PROJ
89
C. Skattebo
NYG
RB-21
Bye: 14
91.6
ADP
$4
$ VALUE
Unlock
PROJ
90
player-headshot
D. Henry
BAL
RB-22
Bye: 7
49.6
ADP
$43
$ VALUE
Unlock
PROJ
91
player-headshot
D. Swift
CHI
RB-23
Bye: 5
99.6
ADP
$8
$ VALUE
Unlock
PROJ
92
player-headshot
D. Kincaid
BUF
TE-9
Bye: 7
92.6
ADP
$2
$ VALUE
Unlock
PROJ
93
player-headshot
D. Montgomery
DET
RB-24
Bye: 8
88.6
ADP
$12
$ VALUE
Unlock
PROJ
94
player-headshot
J. Jennings
SF
WR-34
Bye: 14
135.9
ADP
$13
$ VALUE
Unlock
PROJ
95
J. Milroe
SEA
QB-28
Bye: 8
142.2
ADP
N/A
$ VALUE
Unlock
PROJ
96
player-headshot
T. Hill
MIA
WR-35
Bye: 12
80.7
ADP
$32
$ VALUE
Unlock
PROJ
97
player-headshot
J. Jeudy
CLE
WR-36
Bye: 9
89.9
ADP
$19
$ VALUE
Unlock
PROJ
98
player-headshot
D. Njoku
CLE
TE-10
Bye: 9
116.8
ADP
$5
$ VALUE
Unlock
PROJ
99
player-headshot
S. Darnold
SEA
QB-29
Bye: 8
113.6
ADP
N/A
$ VALUE
Unlock
PROJ
100
player-headshot
I. Pacheco
KC
RB-25
Bye: 10
89.7
ADP
$9
$ VALUE
Unlock
PROJ
101
L. Burden III
CHI
WR-37
Bye: 5
N/A
ADP
$3
$ VALUE
Unlock
PROJ
102
player-headshot
K. Shakir
BUF
WR-38
Bye: 7
112.8
ADP
$10
$ VALUE
Unlock
PROJ
103
player-headshot
M. Andrews
BAL
TE-11
Bye: 7
100.1
ADP
$6
$ VALUE
Unlock
PROJ
104
player-headshot
J. Downs
IND
WR-39
Bye: 11
107.2
ADP
$5
$ VALUE
Unlock
PROJ
105
player-headshot
A. Kamara
NO
RB-26
Bye: 11
83.7
ADP
$18
$ VALUE
Unlock
PROJ
106
player-headshot
J. Mixon
HOU
RB-27
Bye: 6
79.0
ADP
$13
$ VALUE
Unlock
PROJ
107
player-headshot
B. Robinson
WAS
RB-28
Bye: 12
103.1
ADP
$6
$ VALUE
Unlock
PROJ
108
player-headshot
J. Mason
MIN
RB-29
Bye: 6
148.5
ADP
$4
$ VALUE
Unlock
PROJ
109
D. Sampson
CLE
RB-30
Bye: 9
160.1
ADP
$2
$ VALUE
Unlock
PROJ
110
player-headshot
T. Spears
TEN
RB-31
Bye: 10
143.8
ADP
$3
$ VALUE
Unlock
PROJ
111
player-headshot
C. Sutton
DEN
WR-40
Bye: 12
97.0
ADP
$19
$ VALUE
Unlock
PROJ
112
player-headshot
M. Evans
TB
WR-41
Bye: 9
87.2
ADP
$24
$ VALUE
Unlock
PROJ
113
player-headshot
J. Warren
PIT
RB-32
Bye: 5
136.9
ADP
$5
$ VALUE
Unlock
PROJ
114
player-headshot
J. Meyers
LV
WR-42
Bye: 8
125.4
ADP
$7
$ VALUE
Unlock
PROJ
115
player-headshot
T. Tracy
NYG
RB-33
Bye: 14
113.8
ADP
$4
$ VALUE
Unlock
PROJ
116
player-headshot
G. Smith
LV
QB-30
Bye: 8
127.9
ADP
N/A
$ VALUE
Unlock
PROJ
117
player-headshot
D. Adams
LAR
WR-43
Bye: 8
94.3
ADP
$25
$ VALUE
Unlock
PROJ
118
player-headshot
D. Samuel
WAS
WR-44
Bye: 12
131.9
ADP
$10
$ VALUE
Unlock
PROJ
119
player-headshot
J. Conner
ARI
RB-34
Bye: 8
101.1
ADP
$12
$ VALUE
Unlock
PROJ
120
player-headshot
C. Godwin
TB
WR-45
Bye: 9
111.9
ADP
$16
$ VALUE
Unlock
PROJ
121
player-headshot
E. Engram
DEN
TE-12
Bye: 12
134.2
ADP
$8
$ VALUE
Unlock
PROJ
122
player-headshot
M. Mims Jr.
DEN
WR-46
Bye: 12
151.8
ADP
$2
$ VALUE
Unlock
PROJ
123
player-headshot
A. Jones
MIN
RB-35
Bye: 6
121.3
ADP
$11
$ VALUE
Unlock
PROJ
124
player-headshot
J. Reed
GB
WR-47
Bye: 5
107.4
ADP
$8
$ VALUE
Unlock
PROJ
125
player-headshot
D. Mooney
ATL
WR-48
Bye: 5
146.9
ADP
$4
$ VALUE
Unlock
PROJ
126
player-headshot
T. Pollard
TEN
RB-36
Bye: 10
115.1
ADP
$10
$ VALUE
Unlock
PROJ
127
player-headshot
R. Stevenson
NE
RB-37
Bye: 14
149.6
ADP
$3
$ VALUE
Unlock
PROJ
128
player-headshot
B. Aiyuk
SF
WR-49
Bye: 14
95.9
ADP
$4
$ VALUE
Unlock
PROJ
129
player-headshot
M. Pittman Jr.
IND
WR-50
Bye: 11
133.8
ADP
$6
$ VALUE
Unlock
PROJ
130
B. Tuten
JAX
RB-38
Bye: 8
128.1
ADP
$3
$ VALUE
Unlock
PROJ
131
player-headshot
C. Ridley
TEN
WR-51
Bye: 10
124.9
ADP
$16
$ VALUE
Unlock
PROJ
132
player-headshot
B. Allen
NYJ
RB-39
Bye: 9
167.8
ADP
$2
$ VALUE
Unlock
PROJ
133
E. Arroyo
SEA
TE-13
Bye: 8
167.2
ADP
N/A
$ VALUE
Unlock
PROJ
134
player-headshot
J. Williams
DAL
RB-40
Bye: 10
145.8
ADP
$4
$ VALUE
Unlock
PROJ
135
J. Higgins
HOU
WR-52
Bye: 6
93.7
ADP
$2
$ VALUE
Unlock
PROJ
136
player-headshot
Z. Charbonnet
SEA
RB-41
Bye: 8
117.9
ADP
$4
$ VALUE
Unlock
PROJ
137
player-headshot
T. Bigsby
JAX
RB-42
Bye: 8
157.2
ADP
$2
$ VALUE
Unlock
PROJ
138
player-headshot
D. Jones
IND
QB-31
Bye: 11
195.0
ADP
N/A
$ VALUE
Unlock
PROJ
139
player-headshot
K. Coleman
BUF
WR-53
Bye: 7
118.5
ADP
$4
$ VALUE
Unlock
PROJ
140
player-headshot
J. Dobbins
DEN
RB-43
Bye: 12
165.5
ADP
$1
$ VALUE
Unlock
PROJ
141
player-headshot
D. Douglas
NE
WR-54
Bye: 14
202.1
ADP
$1
$ VALUE
Unlock
PROJ
142
player-headshot
T. Benson
ARI
RB-44
Bye: 8
123.0
ADP
$3
$ VALUE
Unlock
PROJ
143
player-headshot
T. Etienne Jr.
JAX
RB-45
Bye: 8
N/A
ADP
$6
$ VALUE
Unlock
PROJ
144
player-headshot
K. Pitts
ATL
TE-14
Bye: 5
109.5
ADP
$2
$ VALUE
Unlock
PROJ
145
player-headshot
R. Johnson
CHI
RB-46
Bye: 5
203.5
ADP
$2
$ VALUE
Unlock
PROJ
146
player-headshot
J. Ford
CLE
RB-47
Bye: 9
209.5
ADP
$1
$ VALUE
Unlock
PROJ
147
player-headshot
R. Wilson
NYG
QB-32
Bye: 14
175.3
ADP
N/A
$ VALUE
Unlock
PROJ
148
player-headshot
M. Stafford
LAR
QB-33
Bye: 8
130.3
ADP
$1
$ VALUE
Unlock
PROJ
149
player-headshot
J. Ferguson
DAL
TE-15
Bye: 10
137.2
ADP
$2
$ VALUE
Unlock
PROJ
150
T. Harris
LAC
WR-55
Bye: 12
106.9
ADP
$4
$ VALUE
Unlock
PROJ
151
player-headshot
T. Allgeier
ATL
RB-48
Bye: 5
177.3
ADP
$2
$ VALUE
Unlock
PROJ
152
player-headshot
J. McMillan
TB
WR-56
Bye: 9
147.7
ADP
$2
$ VALUE
Unlock
PROJ
153
player-headshot
D. Goedert
PHI
TE-16
Bye: 9
163.8
ADP
$3
$ VALUE
Unlock
PROJ
154
player-headshot
S. Rattler
NO
QB-34
Bye: 11
244.9
ADP
N/A
$ VALUE
Unlock
PROJ
155
player-headshot
K. Mitchell
BAL
RB-49
Bye: 7
233.9
ADP
$2
$ VALUE
Unlock
PROJ
156
player-headshot
K. Pickett
CLE
QB-35
Bye: 9
287.7
ADP
N/A
$ VALUE
Unlock
PROJ
157
J. Blue
DAL
RB-50
Bye: 10
141.6
ADP
$3
$ VALUE
Unlock
PROJ
158
player-headshot
I. Likely
BAL
TE-17
Bye: 7
125.8
ADP
$3
$ VALUE
Unlock
PROJ
159
T. Ferguson
LAR
TE-18
Bye: 8
159.4
ADP
N/A
$ VALUE
Unlock
PROJ
160
K. Williams
NE
WR-57
Bye: 14
131.2
ADP
$3
$ VALUE
Unlock
PROJ
161
player-headshot
R. Shaheed
NO
WR-58
Bye: 11
155.3
ADP
$2
$ VALUE
Unlock
PROJ
162
player-headshot
Z. Wilson
MIA
QB-36
Bye: 12
292.8
ADP
N/A
$ VALUE
Unlock
PROJ
163
player-headshot
J. Wright
MIA
RB-51
Bye: 12
170.7
ADP
$2
$ VALUE
Unlock
PROJ
164
player-headshot
R. Doubs
GB
WR-59
Bye: 5
197.6
ADP
$1
$ VALUE
Unlock
PROJ
165
player-headshot
T. Kelce
KC
TE-19
Bye: 10
119.5
ADP
$8
$ VALUE
Unlock
PROJ
166
player-headshot
I. Guerendo
SF
RB-52
Bye: 14
161.9
ADP
$3
$ VALUE
Unlock
PROJ
167
player-headshot
C. Tillman
CLE
WR-60
Bye: 9
171.8
ADP
$3
$ VALUE
Unlock
PROJ
168
player-headshot
Q. Johnston
LAC
WR-61
Bye: 12
184.8
ADP
$1
$ VALUE
Unlock
PROJ
169
player-headshot
R. Bateman
BAL
WR-62
Bye: 7
164.4
ADP
$2
$ VALUE
Unlock
PROJ
170
player-headshot
C. Kupp
SEA
WR-63
Bye: 8
139.7
ADP
$5
$ VALUE
Unlock
PROJ
171
player-headshot
S. Diggs
NE
WR-64
Bye: 14
143.2
ADP
$6
$ VALUE
Unlock
PROJ
172
player-headshot
R. Davis
BUF
RB-53
Bye: 7
169.7
ADP
$4
$ VALUE
Unlock
PROJ
173
player-headshot
M. Lloyd
GB
RB-54
Bye: 5
199.1
ADP
$2
$ VALUE
Unlock
PROJ
174
player-headshot
X. Legette
CAR
WR-65
Bye: 14
156.0
ADP
$1
$ VALUE
Unlock
PROJ
175
M. Taylor
NYJ
TE-20
Bye: 9
138.0
ADP
N/A
$ VALUE
Unlock
PROJ
176
player-headshot
C. Kirk
HOU
WR-66
Bye: 6
182.8
ADP
$3
$ VALUE
Unlock
PROJ
177
player-headshot
C. Okonkwo
TEN
TE-21
Bye: 10
N/A
ADP
N/A
$ VALUE
Unlock
PROJ
178
player-headshot
N. Harris
LAC
RB-55
Bye: 12
134.7
ADP
$4
$ VALUE
Unlock
PROJ
179
player-headshot
T. Dell
HOU
WR-67
Bye: 6
194.6
ADP
N/A
$ VALUE
Unlock
PROJ
180
player-headshot
B. Strange
JAX
TE-22
Bye: 8
173.1
ADP
$2
$ VALUE
Unlock
PROJ
181
P. Bryant
DEN
WR-68
Bye: 12
176.6
ADP
$1
$ VALUE
Unlock
PROJ
182
player-headshot
W. Robinson
NYG
WR-69
Bye: 14
178.1
ADP
$2
$ VALUE
Unlock
PROJ
183
J. Bech
LV
WR-70
Bye: 8
122.1
ADP
$1
$ VALUE
Unlock
PROJ
184
player-headshot
R. White
TB
RB-56
Bye: 9
158.6
ADP
$3
$ VALUE
Unlock
PROJ
185
player-headshot
M. Wilson
ARI
WR-71
Bye: 8
241.8
ADP
$1
$ VALUE
Unlock
PROJ
186
player-headshot
A. Rodgers
PIT
QB-37
Bye: 5
181.8
ADP
$1
$ VALUE
Unlock
PROJ
187
player-headshot
T. Atwell
LAR
WR-72
Bye: 8
291.3
ADP
N/A
$ VALUE
Unlock
PROJ
188
player-headshot
M. Brown
KC
WR-73
Bye: 10
N/A
ADP
$2
$ VALUE
Unlock
PROJ
189
H. Fannin Jr.
CLE
TE-23
Bye: 9
174.7
ADP
N/A
$ VALUE
Unlock
PROJ
190
J. Hunter
LAR
RB-57
Bye: 8
189.5
ADP
$1
$ VALUE
Unlock
PROJ
191
player-headshot
A. Mitchell
IND
WR-74
Bye: 11
193.6
ADP
$1
$ VALUE
Unlock
PROJ
192
player-headshot
C. Austin III
PIT
WR-75
Bye: 5
N/A
ADP
$1
$ VALUE
Unlock
PROJ
193
player-headshot
B. Corum
LAR
RB-58
Bye: 8
179.5
ADP
$1
$ VALUE
Unlock
PROJ
194
player-headshot
J. Palmer
BUF
WR-76
Bye: 7
219.2
ADP
$1
$ VALUE
Unlock
PROJ
195
player-headshot
I. Davis
NYJ
RB-59
Bye: 9
262.3
ADP
N/A
$ VALUE
Unlock
PROJ
196
player-headshot
A. Pierce
IND
WR-77
Bye: 11
221.3
ADP
$1
$ VALUE
Unlock
PROJ
197
player-headshot
J. Flacco
CLE
QB-38
Bye: 9
245.9
ADP
N/A
$ VALUE
Unlock
PROJ
198
J. Noel
HOU
WR-78
Bye: 6
153.8
ADP
$2
$ VALUE
Unlock
PROJ
199
J. Royals
KC
WR-79
Bye: 10
172.7
ADP
$1
$ VALUE
Unlock
PROJ
200
T. Brooks
CIN
RB-60
Bye: 10
223.1
ADP
$1
$ VALUE
Unlock
PROJ
201
player-headshot
P. Freiermuth
PIT
TE-24
Bye: 5
154.0
ADP
$2
$ VALUE
Unlock
PROJ
202
J. Croskey-Merritt
WAS
RB-61
Bye: 12
231.3
ADP
$1
$ VALUE
Unlock
PROJ
203
player-headshot
K. Cousins
ATL
QB-39
Bye: 5
235.3
ADP
N/A
$ VALUE
Unlock
PROJ
204
player-headshot
T. Taylor
NYJ
QB-40
Bye: 9
377.9
ADP
N/A
$ VALUE
Unlock
PROJ
205
player-headshot
N. Chubb
HOU
RB-62
Bye: 6
214.2
ADP
$2
$ VALUE
Unlock
PROJ
206
D. Thornton Jr.
LV
WR-80
Bye: 8
232.2
ADP
N/A
$ VALUE
Unlock
PROJ
207
player-headshot
C. Watson
GB
WR-81
Bye: 5
251.2
ADP
N/A
$ VALUE
Unlock
PROJ
208
player-headshot
R. Dowdle
CAR
RB-63
Bye: 14
190.8
ADP
$2
$ VALUE
Unlock
PROJ
209
player-headshot
D. Brown
JAX
WR-82
Bye: 8
266.5
ADP
$1
$ VALUE
Unlock
PROJ
210
D. Giddens
IND
RB-64
Bye: 11
188.5
ADP
$1
$ VALUE
Unlock
PROJ
211
K. Monangai
CHI
RB-65
Bye: 5
218.8
ADP
N/A
$ VALUE
Unlock
PROJ
212
player-headshot
M. Sanders
DAL
RB-66
Bye: 10
265.4
ADP
N/A
$ VALUE
Unlock
PROJ
213
player-headshot
J. Milton III
DAL
QB-41
Bye: 10
N/A
ADP
N/A
$ VALUE
Unlock
PROJ
214
player-headshot
E. Mitchell
KC
RB-67
Bye: 10
283.2
ADP
N/A
$ VALUE
Unlock
PROJ
215
player-headshot
J. Brooks
CAR
RB-68
Bye: 14
185.8
ADP
N/A
$ VALUE
Unlock
PROJ
216
player-headshot
J. Sanders
CAR
TE-25
Bye: 14
187.2
ADP
N/A
$ VALUE
Unlock
PROJ
217
E. Ayomanor
TEN
WR-83
Bye: 10
179.1
ADP
$1
$ VALUE
Unlock
PROJ
218
D. Gabriel
CLE
QB-42
Bye: 9
226.7
ADP
N/A
$ VALUE
Unlock
PROJ
219
player-headshot
M. Rudolph
PIT
QB-43
Bye: 5
305.9
ADP
N/A
$ VALUE
Unlock
PROJ
220
player-headshot
A. Ekeler
WAS
RB-69
Bye: 12
207.8
ADP
$2
$ VALUE
Unlock
PROJ
221
S. Sanders
CLE
QB-44
Bye: 9
152.3
ADP
N/A
$ VALUE
Unlock
PROJ
222
player-headshot
T. Johnson
NYG
TE-26
Bye: 14
201.2
ADP
N/A
$ VALUE
Unlock
PROJ
223
player-headshot
C. Otton
TB
TE-27
Bye: 9
161.3
ADP
$1
$ VALUE
Unlock
PROJ
224
player-headshot
J. Winston
NYG
QB-45
Bye: 14
293.8
ADP
N/A
$ VALUE
Unlock
PROJ
225
player-headshot
M. Gesicki
CIN
TE-28
Bye: 10
215.5
ADP
$1
$ VALUE
Unlock
PROJ
226
T. Etienne
CAR
RB-70
Bye: 14
200.1
ADP
$1
$ VALUE
Unlock
PROJ
227
player-headshot
R. Wilson
PIT
WR-84
Bye: 5
209.0
ADP
N/A
$ VALUE
Unlock
PROJ
228
O. Gadsden II
LAC
TE-29
Bye: 12
N/A
ADP
N/A
$ VALUE
Unlock
PROJ
229
player-headshot
H. Henry
NE
TE-30
Bye: 14
203.0
ADP
$2
$ VALUE
Unlock
PROJ
230
player-headshot
M. Jones
SF
QB-46
Bye: 14
299.7
ADP
N/A
$ VALUE
Unlock
PROJ
231
player-headshot
W. Shipley
PHI
RB-71
Bye: 9
233.9
ADP
$2
$ VALUE
Unlock
PROJ
232
player-headshot
K. Miller
NO
RB-72
Bye: 11
229.8
ADP
$1
$ VALUE
Unlock
PROJ
233
player-headshot
M. Mariota
WAS
QB-47
Bye: 12
381.6
ADP
N/A
$ VALUE
Unlock
PROJ
234
player-headshot
A. Iosivas
CIN
WR-85
Bye: 10
247.1
ADP
$2
$ VALUE
Unlock
PROJ
235
J. Coker
CAR
WR-86
Bye: 14
183.6
ADP
$1
$ VALUE
Unlock
PROJ
236
player-headshot
S. Howell
MIN
QB-48
Bye: 6
281.0
ADP
N/A
$ VALUE
Unlock
PROJ
237
player-headshot
J. Smith
PIT
TE-31
Bye: 5
129.3
ADP
$5
$ VALUE
Unlock
PROJ
238
player-headshot
D. Waller
MIA
TE-32
Bye: 12
N/A
ADP
N/A
$ VALUE
Unlock
PROJ
239
player-headshot
M. Mayer
LV
TE-33
Bye: 8
256.1
ADP
N/A
$ VALUE
Unlock
PROJ
240
D. Neal
NO
RB-73
Bye: 11
166.9
ADP
$1
$ VALUE
Unlock
PROJ
241
player-headshot
J. Johnson
NO
TE-34
Bye: 11
259.7
ADP
$1
$ VALUE
Unlock
PROJ
242
player-headshot
T. Lockett
TEN
WR-87
Bye: 10
271.8
ADP
N/A
$ VALUE
Unlock
PROJ
243
player-headshot
J. Tolbert
DAL
WR-88
Bye: 10
297.4
ADP
$1
$ VALUE
Unlock
PROJ
244
player-headshot
C. Akers
NO
RB-74
Bye: 11
319.7
ADP
N/A
$ VALUE
Unlock
PROJ
245
player-headshot
D. Slayton
NYG
WR-89
Bye: 14
281.4
ADP
$1
$ VALUE
Unlock
PROJ
246
player-headshot
D. Wicks
GB
WR-90
Bye: 5
236.2
ADP
$1
$ VALUE
Unlock
PROJ
247
player-headshot
C. Kmet
CHI
TE-35
Bye: 5
212.6
ADP
$1
$ VALUE
Unlock
PROJ
248
player-headshot
M. Willis
GB
QB-49
Bye: 5
316.3
ADP
N/A
$ VALUE
Unlock
PROJ
249
player-headshot
N. Gray
KC
TE-36
Bye: 10
227.4
ADP
$1
$ VALUE
Unlock
PROJ
250
player-headshot
D. Johnson
CLE
WR-91
Bye: 9
269.4
ADP
$1
$ VALUE
Unlock
PROJ
251
J. James
SF
RB-75
Bye: 14
196.2
ADP
$1
$ VALUE
Unlock
PROJ
252
player-headshot
D. Schultz
HOU
TE-37
Bye: 6
224.8
ADP
N/A
$ VALUE
Unlock
PROJ
253
player-headshot
P. Washington
JAX
WR-92
Bye: 8
309.4
ADP
N/A
$ VALUE
Unlock
PROJ
254
player-headshot
T. Tucker
LV
WR-93
Bye: 8
303.4
ADP
N/A
$ VALUE
Unlock
PROJ
255
player-headshot
D. Vele
DEN
WR-94
Bye: 12
313.5
ADP
$1
$ VALUE
Unlock
PROJ
256
player-headshot
R. Mostert
LV
RB-76
Bye: 8
287.0
ADP
$1
$ VALUE
Unlock
PROJ
257
player-headshot
A. Thielen
CAR
WR-95
Bye: 14
225.1
ADP
$1
$ VALUE
Unlock
PROJ
258
player-headshot
T. Conklin
LAC
TE-38
Bye: 12
289.7
ADP
N/A
$ VALUE
Unlock
PROJ
259
player-headshot
J. Whittington
LAR
WR-96
Bye: 8
239.8
ADP
N/A
$ VALUE
Unlock
PROJ
260
player-headshot
J. Garoppolo
LAR
QB-50
Bye: 8
379.0
ADP
N/A
$ VALUE
Unlock
PROJ
261
player-headshot
A. Dillon
PHI
RB-77
Bye: 9
284.8
ADP
N/A
$ VALUE
Unlock
PROJ
262
player-headshot
J. Browning
CIN
QB-51
Bye: 10
326.5
ADP
N/A
$ VALUE
Unlock
PROJ
263
player-headshot
Z. Ertz
WAS
TE-39
Bye: 12
215.4
ADP
$1
$ VALUE
Unlock
PROJ
264
player-headshot
J. Nailor
MIN
WR-97
Bye: 6
314.7
ADP
N/A
$ VALUE
Unlock
PROJ
265
player-headshot
G. Minshew
KC
QB-52
Bye: 10
340.9
ADP
N/A
$ VALUE
Unlock
PROJ
266
player-headshot
D. Hopkins
BAL
WR-98
Bye: 7
243.0
ADP
$2
$ VALUE
Unlock
PROJ
267
S. Williams
GB
WR-99
Bye: 5
239.4
ADP
N/A
$ VALUE
Unlock
PROJ
268
player-headshot
K. Herbert
IND
RB-78
Bye: 11
299.5
ADP
$1
$ VALUE
Unlock
PROJ
269
player-headshot
T. Higbee
LAR
TE-40
Bye: 8
294.0
ADP
N/A
$ VALUE
Unlock
PROJ
270
player-headshot
J. Brissett
ARI
QB-53
Bye: 8
424.5
ADP
N/A
$ VALUE
Unlock
PROJ
271
player-headshot
R. McCloud III
ATL
WR-100
Bye: 5
N/A
ADP
N/A
$ VALUE
Unlock
PROJ
272
C. Dike
TEN
WR-101
Bye: 10
253.8
ADP
N/A
$ VALUE
Unlock
PROJ
273
I. TeSlaa
DET
WR-102
Bye: 8
205.2
ADP
N/A
$ VALUE
Unlock
PROJ
274
player-headshot
S. Tucker
TB
RB-79
Bye: 9
263.9
ADP
$1
$ VALUE
Unlock
PROJ
275
player-headshot
K. Hunt
KC
RB-80
Bye: 10
252.0
ADP
$1
$ VALUE
Unlock
PROJ
276
player-headshot
J. Reynolds
NYJ
WR-103
Bye: 9
412.0
ADP
N/A
$ VALUE
Unlock
PROJ
277
A. Smith
NYJ
WR-104
Bye: 9
263.1
ADP
N/A
$ VALUE
Unlock
PROJ
278
player-headshot
N. Brown
WAS
WR-105
Bye: 12
419.5
ADP
N/A
$ VALUE
Unlock
PROJ
279
player-headshot
J. Hill
BAL
RB-81
Bye: 7
250.3
ADP
$2
$ VALUE
Unlock
PROJ
280
player-headshot
A. Estime
DEN
RB-82
Bye: 12
237.5
ADP
$1
$ VALUE
Unlock
PROJ
281
O. Gordon II
MIA
RB-83
Bye: 12
N/A
ADP
$1
$ VALUE
Unlock
PROJ
282
player-headshot
D. Mills
HOU
QB-54
Bye: 6
680.8
ADP
N/A
$ VALUE
Unlock
PROJ
283
player-headshot
C. Rush
BAL
QB-55
Bye: 7
413.3
ADP
N/A
$ VALUE
Unlock
PROJ
284
T. Felton
MIN
WR-106
Bye: 6
238.8
ADP
N/A
$ VALUE
Unlock
PROJ
285
W. Marks
HOU
RB-84
Bye: 6
206.9
ADP
$2
$ VALUE
Unlock
PROJ
286
player-headshot
J. McLaughlin
DEN
RB-85
Bye: 12
268.6
ADP
N/A
$ VALUE
Unlock
PROJ
287
player-headshot
T. Franklin
DEN
WR-107
Bye: 12
221.9
ADP
N/A
$ VALUE
Unlock
PROJ
288
player-headshot
S. McCormick
LV
RB-86
Bye: 8
662.6
ADP
N/A
$ VALUE
Unlock
PROJ
289
B. Smith
KC
RB-87
Bye: 10
211.5
ADP
$2
$ VALUE
Unlock
PROJ
290
J. Lane
WAS
WR-108
Bye: 12
245.6
ADP
N/A
$ VALUE
Unlock
PROJ
291
player-headshot
J. Dotson
PHI
WR-109
Bye: 9
330.5
ADP
N/A
$ VALUE
Unlock
PROJ
292
K. McCord
PHI
QB-56
Bye: 9
329.8
ADP
N/A
$ VALUE
Unlock
PROJ
293
player-headshot
A. O'Connell
LV
QB-57
Bye: 8
346.6
ADP
N/A
$ VALUE
Unlock
PROJ
294
player-headshot
K. Gainwell
PIT
RB-88
Bye: 5
341.3
ADP
N/A
$ VALUE
Unlock
PROJ
295
player-headshot
A. Gibson
NE
RB-89
Bye: 14
335.5
ADP
N/A
$ VALUE
Unlock
PROJ
296
R. Leonard
IND
QB-58
Bye: 11
269.7
ADP
N/A
$ VALUE
Unlock
PROJ
297
W. Howard
PIT
QB-59
Bye: 5
185.6
ADP
N/A
$ VALUE
Unlock
PROJ
298
player-headshot
M. Trubisky
BUF
QB-60
Bye: 7
N/A
ADP
N/A
$ VALUE
Unlock
PROJ
299
player-headshot
E. Moore
BUF
WR-110
Bye: 7
261.1
ADP
$1
$ VALUE
Unlock
PROJ
300
player-headshot
J. Burton
CIN
WR-111
Bye: 10
272.3
ADP
N/A
$ VALUE
Unlock
PROJ
301
D. Martinez
SEA
RB-90
Bye: 8
248.7
ADP
N/A
$ VALUE
Unlock
PROJ
302
player-headshot
A. Dalton
CAR
QB-61
Bye: 14
416.8
ADP
N/A
$ VALUE
Unlock
PROJ
303
K. Mullings
TEN
RB-91
Bye: 10
286.1
ADP
N/A
$ VALUE
Unlock
PROJ
304
player-headshot
T. Chandler
MIN
RB-92
Bye: 6
422.9
ADP
N/A
$ VALUE
Unlock
PROJ
305
player-headshot
M. Valdes-Scantling
SEA
WR-112
Bye: 8
323.2
ADP
N/A
$ VALUE
Unlock
PROJ
306
player-headshot
K. Turpin
DAL
WR-113
Bye: 10
373.2
ADP
N/A
$ VALUE
Unlock
PROJ
307
player-headshot
K. Trask
TB
QB-62
Bye: 9
494.0
ADP
N/A
$ VALUE
Unlock
PROJ
308
player-headshot
N. Westbrook-Ikhine
MIA
WR-114
Bye: 12
321.1
ADP
$1
$ VALUE
Unlock
PROJ
309
player-headshot
G. Dortch
ARI
WR-115
Bye: 8
386.8
ADP
N/A
$ VALUE
Unlock
PROJ
310
player-headshot
J. Hyatt
NYG
WR-116
Bye: 14
317.3
ADP
N/A
$ VALUE
Unlock
PROJ
311
K. Lambert-Smith
LAC
WR-117
Bye: 12
279.4
ADP
N/A
$ VALUE
Unlock
PROJ
312
T. Horton
SEA
WR-118
Bye: 8
213.1
ADP
N/A
$ VALUE
Unlock
PROJ
313
player-headshot
D. Singletary
NYG
RB-93
Bye: 14
305.9
ADP
N/A
$ VALUE
Unlock
PROJ
314
player-headshot
T. Patrick
DET
WR-119
Bye: 8
491.0
ADP
N/A
$ VALUE
Unlock
PROJ
315
player-headshot
B. Cooks
NO
WR-120
Bye: 11
338.4
ADP
N/A
$ VALUE
Unlock
PROJ
316
player-headshot
C. Rodriguez Jr.
WAS
RB-94
Bye: 12
N/A
ADP
N/A
$ VALUE
Unlock
PROJ
317
player-headshot
A. Mattison
MIA
RB-95
Bye: 12
345.5
ADP
N/A
$ VALUE
Unlock
PROJ
318
player-headshot
R. Moore
MIN
WR-121
Bye: 6
428.6
ADP
N/A
$ VALUE
Unlock
PROJ
319
player-headshot
J. Polk
NE
WR-122
Bye: 14
275.7
ADP
N/A
$ VALUE
Unlock
PROJ
320
player-headshot
M. Washington
MIA
WR-123
Bye: 12
260.6
ADP
N/A
$ VALUE
Unlock
PROJ
"""  # Use the full text from your dataset here

# Clean lines and remove unwanted fields
lines = [
    line.strip()
    for line in text.splitlines()
    if line.strip()
    and not line.startswith("player-headshot")
    and "$ VALUE" not in line
    and "Unlock" not in line
]

rows = []
i = 0
while i < len(lines):
    if lines[i].isdigit():  # Detect a Rank row
        rank = int(lines[i])
        player = lines[i + 1]
        team = lines[i + 2]
        pos_full = lines[i + 3]
        bye = lines[i + 4].replace("Bye: ", "")
        proj = lines[i + 5]
        adp = lines[i + 7] if i + 7 < len(lines) else ""

        # Split position and position rank
        if "-" in pos_full:
            position, pos_rank = pos_full.split("-", 1)
        else:
            position, pos_rank = pos_full, ""

        rows.append([rank, player, team, position, pos_rank, bye, proj, adp])
        i += 8  # Move to next player block
    else:
        i += 1

# Write to CSV
output_path = "data/pff_ranks.csv"
with open(output_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Rank", "Player", "Team", "Position", "Position Rank", "Bye", "Proj", "ADP"])
    writer.writerows(rows)

print(f"CSV file saved to {output_path}")
