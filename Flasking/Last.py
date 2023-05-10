# import requests
# 
# url = "http://localhost/files/git/tensorflowjs/ChessboardFenTensorflowJs-master/saveFile.php"
# 
# payload={}
# files=[
#   ('image',('Screenshot 2023-04-14 005228.png',open('/C:/Users/Paresh/Pictures/Screenshots/Screenshot 2023-04-14 005228.png','rb'),'image/png'))]
# headers = {}
# 
# response = requests.request("POST", url, headers=headers, data=payload, files=files)
# # 
# print(response.text)

import re
str="""
01 
“When you see a good move, look for a better one”

(Emanuel Lasker)

 

 02

“Nothing excites jaded Grandmasters more than a theoretical novelty”

(Dominic Lawson)

 

 03

“The Pin is mightier than the sword”

(Fred Reinfeld)

 

 04

“We cannot resist the fascination of sacrifice, since a passion for

sacrifices is part of a Chessplayer’s nature”

(Rudolf Spielman)

 

 05

“All I want to do, ever, is just play Chess”

(Bobby Fischer)

 

 06

“A win by an unsound combination, however showy,

fills me with artistic horror”

(Wilhelm Steinitz)

 

 07

“The chessboard is the world, the pieces are the phenomena of the

Universe, the rules of the game are what we call the laws of Nature

and the player on the other side is hidden from us”

(Thomas Huxley)

 

 08

“Adequate compensation for a sacrifice is having a sound combination leading to a winning position; adequate compensation for a blunder is

having your opponent snatch defeat from the jaws of victory”

(Bruce A. Moon)

 

 09“Strategy requires thought, tactics require observation”

(Max Euwe)

10“I don’t believe in psychology. I believe in good moves”

(Bobby Fischer)

11“Modern Chess is too much concerned with things like

Pawn structure. Forget it, Checkmate ends the game”

(Nigel Short)

12“Life is a kind of Chess, with struggle, competition, good and ill events”

(Benjamin Franklin)

13“Even the laziest King flees wildly in the face of a double check!”

(Aaron Nimzowitsch)

14“Combinations have always been the most intriguing aspect of Chess.

The masters look for them, the public applauds them, the critics

praise them. It is because combinations are possible that Chess

is more than a lifeless mathematical exercise. They are the

poetry of the game; they are to Chess what melody is to

music. They represent the triumph of mind over matter”

(Reuben Fine)

15“I give 98 percent of my mental energy to Chess”

Others give only 2 percent

(Bobby Fischer)

16“Chess is a fairy tale of 1001 blunders”

(Savielly Tartakower)

17“Chess is no whit inferior to the violin, and we have a

large number of professional violinists”

(Mikhail Botvinnik)

18“Only the player with the initiative has the right to attack”

(Wilhelm Steinitz)

19“The winner of the game is the player who makes the next-to-last mistake”

(Savielly Tartakover)

 20“Your body has to be in top condition. Your Chess deteriorates

as your body does. You can’t separate body from mind”

(Bobby Fischer)

 21“Of Chess it has been said that life is not long

enough for it, but that is the fault of life, not Chess”

(William Ewart Napier)

 22“I have added these principles to the law: get the Knights

into action before both Bishops are developed”

(Emanuel Lasker)

 23“Life is like a game of Chess, changing with each move”

(Chinese proverb)

 24“You cannot play at Chess if you are kind-hearted”

(French Proverb)

 25“Its just you and your opponent at the board

and you’re trying to prove something”

(Bobby Fischer)

 26“It is the aim of the modern school, not to treat every position

according to one general law, but according to

the principle inherent in the position”

(Richard Reti)

 27“The Pawns are the soul of the game”

(Francois Andre Danican Philidor)

 28“In order to improve your game, you must study the endgame before

everything else, for whereas the endings can be studied and

mastered by themselves, the middle game and the opening

must be studied in relation to the endgame”

(Jose Raul Capablanca)

 29“Without error there can be no brilliancy”

(Emanuel Lasker)

 30“Chess is like war on a board”

(Bobby Fischer)

 31“Chess is played with the mind and not with the hands!”

(Renaud and Kahn)

 32“Chess is mental torture”

(Garry Kasparov)

 33“Many have become Chess Masters,

no one has become the Master of Chess”

(Siegbert Tarrasch)

 34“The most important feature of the Chess position is the activity of the

pieces. This is absolutely fundamental in all phases of the game:

Opening, Middlegame and especially Endgame. The primary

constraint on a piece’s activity is the Pawn structure”

(Michael Stean)

 35“You have to have the fighting spirit. You have

to force moves and take chances”

(Bobby Fischer)

 36“Could we look into the head of a Chess player,

we should see there a whole world of feelings,

images, ideas, emotion and passion”

(Alfred Binet)

 37“Openings teach you openings. Endgames teach you chess!”

(Stephan Gerzadowicz)

 38“My style is somewhere between that of Tal and Petrosian”

(Reshevsky)

 39“Play the opening like a book, the middle game like

a magician, and the endgame like a machine”

(Spielmann)

 40“That’s what Chess is all about. One day you give your

opponent a lesson, the next day he gives you one”

(Bobby Fischer)

 41“Some part of a mistake is always correct”

(Savielly Tartakover)

 42“Methodical thinking is of more use in Chess than inspiration”

(C. J. S. Purdy)

 43“When in doubt... play Chess!”

(Tevis)

 44“Who is your opponent tonight,

tonight I am playing against the Black pieces”

(Akiba Rubinstein)

 45“I like the moment when I break a man’s ego”

(Bobby Fischer)

 46“Excellence at Chess is one mark of a scheming mind”

(Sir Arthur Conan Doyle)

 47“A bad day of Chess is better than any good day at work”

(Anonymous)

 48“Chess is the art of analysis”

(Mikhail Botvinnik)

 49“The mistakes are there, waiting to be made”

(Savielly Tartakower)

 50“There are tough players and nice guys, and I’m a tough player”

(Bobby Fischer)

 51“After black’s reply to 1.e4 with 1..e5, leaves him

always trying to get into the game”

(Howard Staunton)

 52“A player surprised is half beaten”

(Proverb) 

 53“A passed Pawn increases in strength as the number

of pieces on the board diminishes”

(Capablanca)

 54“The essence of Chess is thinking about what Chess is”

(David Bronstein) 

 55“I am the best player in the world and I am here to prove it”

(Bobby Fischer)

 56“Chess is a forcing house where the fruits of

character can ripen more fully than in life”

(Edward Morgan Foster)

 57“Half the variations which are calculated in a tournament game

turn out to be completely superfluous. Unfortunately, no one

knows in advance which half”

(Jan Tinman)

 58“Chess is as much a mystery as women”

(Purdy)

 59“Good positions don’t win games, good moves do”

(Gerald Abrahams)

 60“If I win a tournament, I win it by myself.

I do the playing. Nobody helps me”

(Bobby Fischer)

 61“What would Chess be without silly mistakes?”

(Kurt Richter)

 62“Before the endgame, the Gods have placed the middle game”

(Siegbert Tarrasch)

 63“Chess was Capablanca’s mother tongue”

(Reti)

 64“Alekhine is a poet who creates a work of art out of something

that would hardly inspire another man to

send home a picture post card”

(Max Euwe)

 65“Don’t even mention losing to me. I can’t stand to think of it”

(Bobby Fischer)

 66“During a Chess competition a Chessmaster should be a

combination of a beast of prey and a monk”

(Alexander Alekhine)

 67“No one ever won a game by resigning”

(Saviely Tartakower)

 68“The defensive power of a pinned piece is only imaginary”

(Aaron Nimzovich)

 69“When the Chess game is over, the Pawn and

the King go back to the same box”

(Irish saying)

 70“A strong memory, concentration, imagination, and a strong will

is required to become a great Chess player”

(Bobby Fischer)

 71“Every Chess master was once a beginner”

(Chernev)

 72“One doesn’t have to play well, it’s

enough to play better than your opponent”

(Siegbert Tarrasch)

 73“Chess is above all, a fight!”

(Emanuel Lasker)

 74“Discovered check is the dive bomber of the Chessboard”

(Reuben Fine)

 75“I know people who have all the will in the world,

but still can’t play good Chess”

(Bobby Fischer)

 76“A Chess game is a dialogue, a conversation between a player and his opponent. Each move by the opponent may contain threats or be a

blunder, but a player cannot defend against threats or take

advantage of blunders if he does not first ask himself:

What is my opponent planning after each move?”

(Bruce A. Moon)

 77“The hardest game to win is a won game”

(Emanuel Lasker)

 78“The most powerful weapon in Chess is to have the next move”

(David Bronstein)

 79“He who fears an isolated Queen’s Pawn should give up Chess”

(Siegbert Tarrasch)

 80“Different people feel differently about resigning”

(Bobby Fischer)

 81“Chess is not like life... it has rules!”

(Mark Pasternak)

 82“Why must I lose to this idiot?”

(Aron Nimzovich)

 83“It’s always better to sacrifice your opponent’s men”

(Savielly Tartakover)

 84“To avoid losing a piece, many a person has lost the game”

(Savielly Tartakover)

 85“All that matters on the Chessboard is good moves”

(Bobby Fischer)

 86“Help your pieces so they can help you”

(Paul Morphy)

 87“In a gambit you give up a Pawn for the sake of getting a lost game”

(Samuel Standige Boden)

 88“It is not enough to be a good player... you must also play well”

(Siegbert Tarrasch)

 89“A sacrifice is best refuted by accepting it”

(Wilhelm Steinitz)

 90“Tactics flow from a superior position”

(Bobby Fischer)

 91“Later, I began to succeed in decisive games. Perhaps

because I realized a very simple truth: not only

was I worried, but also my opponent”

(Mikhail Tal)

 92“Chess is life”

(Bobby Fischer)

 93“Chess is a beautiful mistress”

(Bent Larsen)

 94“Some sacrifices are sound; the rest are mine”

(Mikhail Tal)

 95

“Best by test: 1. e4”

(Bobby Fischer)

 

 96“A bad plan is better than none at all”

(Frank Marshall)

 97

“Chess books should be used as we use glasses: to assist

the sight, although some players make use of them as if

they thought they conferred sight”

(Jose Raul Capablanca)

 

 98“There are two types of sacrifices: correct ones and mine”

(Mikhail Tal)

 99

“Morphy was probably the greatest genius of them all”

(Bobby Fischer)

 

 100“My opponents make good moves too. Sometimes

I don’t take these things into consideration”

(Bobby Fischer)

 101“The combination player thinks forward; he starts from

the given position, and tries the forceful moves in his mind”

(Emanuel Lasker)

 102

“A Chess game is divided into three stages: the first, when you hope

you have the advantage, the second when you believe you have an

advantage, and the third... when you know you’re going to lose!”

(Savielly Tartakower)

 

 103

“Chess demands total concentration”

(Bobby Fischer)

 

 104

“Chess, like love, like music, has the power to make people happy”

(Siegbert Tarrasch)

 

 105

“All my games are real”

(Bobby Fischer)

 

106

“Chess is everything: art, science and sport”

(Anatoly Karpov)

 

107

“Chess is the art which expresses the science of logic”

(Mikhail Botvinnik)

 

108

“Not all artists are Chess players, but all Chess players are artists”

(Marcel Duchamp)

 

109

“Chess is imagination”

(David Bronstein)

 

110

“I’m not afraid of Spassky. The world knows I’m the best”

You don’t need a match to prove it

(Bobby Fischer)

 

111

“If cunning alone were needed to excel, women”

would be the best Chess players

(Albin)

 

112

“Chess is thirty to forty percent psychology. You don’t have this

when you play a computer. I can’t confuse it”

(Judith Polgar)

 

113

“On the chessboard, lies and hypocrisy do not survive long”

(Emanuel Lasker)

 

114

“Chess is war over the board. The object is to crush the opponents mind”

(Bobby Fischer)

 

115

“The passed Pawn is a criminal, who should be kept under lock and key. 

Mild measures, such as police surveillance, are not sufficient”

(Aaron Nimzovich)

 

116

“Chess holds its master in its own bonds, shackling the mind and brain

so that the inner freedom of the very strongest must suffer”

(Albert Einstein)

 

117

“Human affairs are like a Chess game: only those who do not

take it seriously can be called good players”

(Hung Tzu Ch’eng)

 

118

“The blunders are all there on the board, waiting to be made”

(Savielly Tartakover)

 

119

“Via the squares on the chessboard, the Indians explain the movement of

time and the age, the higher influences which control the world and

the ties which link Chess with the human soul”

(Al-Masudi)

 

120

“It is no time to be playing Chess when the house is on fire”

(Italian Proverb)

 

121

“You sit at the board and suddenly your heart leaps. Your hand trembles to pick up the piece and move it.  But what Chess teaches you is that you

must sit there calmly and think about whether its really a good idea

and whether there are other better ideas”

(Stanley Kubrick)

 

122

“Daring ideas are like Chess men moved forward. They

may be beaten, but they may start a winning game”

(Johann Wolfgang von Goethe)

 

123

“Of all my Russian books, the defense contains and diffuses the

greatest ’warmth’ which may seem odd seeing how 

supremely abstract Chess is supposed to be”

(Vladimir Nabokov)

 

124

“For surely of all the drugs in the world, Chess must be

the most permanently pleasurable”

(Assiac)

 

125

“A thorough understanding of the typical mating continuations makes

the most complicated sacrificial combinations leading up to them

not only not difficult, but almost a matter of course”

(Siegbert Tarrasch)

 

126

“Chess problems demand from the composer the same virtues that

characterize all worthwhile art: originality, invention, conciseness, 

harmony, complexity, and splendid insincerity”

(Vladimir Nabokov)

 

127

“Personally, I rather look forward to a computer program winning the

world Chess Championship. Humanity needs a lesson in humility”

(Richard Dawkings)

 

128

“The boy (then a 12 year old boy named Anatoly Karpov) doesn’t have a

clue about Chess, and there’s no future at all for him in this profession”

(Mikhail Botvinnik)

 

129

“As one by one I mowed them down, my superiority

soon became apparent”

(Jose Capablanca)

 

130

“Though most people love to look at the games of the great attacking masters, some of the most successful players in history have been the

quiet positional players. They slowly grind you down by taking away your space, tying up your pieces, and leaving you with virtually nothing to do!”

(Yasser Seirawan)

 

131

“Chess is ruthless: you’ve got to be prepared to kill people

(Nigel Short)

 

132

“There must have been a time when men were demigods,

or they could not have invented Chess”

(Gustav Schenk)

 

133

“Chess is really ninety nine percent calculation”

(Soltis)

 

134

“Chess is the gymnasium of the mind”

(Blaise Pascal)

 

135

“The game of Chess is not merely an idle amusement; several very

valuable qualities of the mind are to be acquired and strengthened by

it, so as to become habits ready on all occasions; for life is a kind of Chess”

(Benjamin Franklin)

 

136

“Winning isn’t everything... but losing is nothing”

(Mednis)

 

137

“Only sissies Castle”

(Rob Sillars)

 

138

“Look at Garry Kasparov. After he loses, invariably he wins the

next game. He just kills the next guy. That’s something

that we have to learn to be able to do”

(Maurice Ashley)

 

139

“There just isn’t enough televised Chess ”

(David Letterman)

 

140

“Avoid the crowd. Do your own thinking independently.

Be the Chess player, not the Chess piece”

(Ralph Charell)

 

141

“Chess is a terrible game. If you have no center, your opponent

has a freer position. If you do have a center, then you

really have something to worry about!”

(Siegbert Tarrasch)

 """
k=[]
quotes=str.split('“')[1::2]
for i in quotes:
    j = i.replace('\n','').replace(')',' ').split('(')
    j[1]=re.sub(r'[0-9]',' ',j[1])

    k.append({"quote":j[0],"author":j[1].strip()})

print(k)

