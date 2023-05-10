**Project Report for PC641 MSc (IT)**

**Project Internship (2023)**

<img src="media/image1.png" style="width:3.1in;height:2.98727in" />

**Student Details:**

Name: Kabir Kanjani

Batch MSc IT 21-23

Student ID: 202112025

**Internship Details:**

On campus Project : PDF2Tactics

**Mentor**

Prof Rahul Muthu.

**Introduction.**

Chess is quite a popular game played across the world by millions of
people. For some, it’s just a hobby, for others; it’s everything.
Everyone knows the basics of chess but after a certain level, most chess
players need resources to improve. Most chess players rely on chess
books for that. There are more chess books than books on any other sport
that cannot be true nowadays***.***

Chess is one of the oldest sports to exist and continues to be one of
the favorite games for many around the world. Chess books also pass the
test of time because the first chess book to be ever written was in 1471
– The Göttingen manuscript is the first book to deal solely with chess.
1474 – William Caxton publishes The Game and Player of Chesse, the first
chess book in English and still chess players use those for practice.

Chess books contain various puzzles, chess positions, strategies, and
much more, which is quite helpful for other players and help to improve
quite quickly for budding young players.

**Birth of the Idea:**

I had a chess tournament in December 2022 and I was preparing for it
since Mid-October, I quite heavily relied on chess books for practice,
Chess books are quite expensive for hardcover so I used Chess Pdfs to
practice while e practicing it was quite a tiresome task to look at a
puzzle, write all the candidate moves and then after completing the
exercise, look if your moves are accurate or not.

That’s when I first thought of the idea, I thought it would be great if
there was some program that would take a pdf as input and convert all
the chess games to playable chess boards.

That’s when it all started.

<img src="media/image2.png" style="width:6.5in;height:3.14514in" />

**Context Diagram**

<img src="media/image3.png" style="width:5.625in;height:7.05in" />

**Scope Statement**

**1. Project Goals & Objectives**

-   The goal of the project is to create a website where users/players
    can pass a pdf as input and get all the chess puzzles, games as
    playable chessboards to improve their pattern recognition and
    practice their skills.

### **2. Project Requirements**

-   Prerequisite Knowledge.

    -   Chess

        -   Chess books

        -   Chess Fen

        -   Stockfish

        -   Move Validation

    -   Python

        -   Core Python

        -   Computer Vision

        -   Flask

        -   Libraries and Api

        -   ML Models

    -   React

        -   Basics of React

        -   Fetch Api

        -   React Chessboard

        -   Various React Packages

    -   JavaScript & Ajax

        -   Basics of JavaScript

        -   Ajax Api calls.

    -   

-   Project Constraints

    -   Chess PDFs with multiple chessboards won't work due to detection
        issues, multiple chessboards cause ambiguity and therefore won't
        provide the desired results.

    -   The system is built on modern day chess boards, so chessboards
        with traditional chess pieces and pattern might work but won't
        provide accurate results.

**Use Case**

-   User can Login.

-   User can register.

-   User can store PDFs into DB.

-   User can store positions.

-   Users can upload Chess PDFs.

-   User can Solve Tactics from the Chess PDF

-   Users can Select the desired Puzzle.

-   User can retry for Invalid Move.

-   Website will respond with the Correct Move for the move played.

**Design Contribution**

The Website consists of the following pages:

1)Login Page/ Signup Page

<img src="media/image2.png" style="width:6.5in;height:3.14514in" />

2\) Dashboard

<img src="media/image4.png" style="width:6.5in;height:3.16875in" />

3\) PDF2Tactics -> File Upload Page

<img src="media/image5.png" style="width:6.5in;height:3.16528in" />

4\) Loading Page

<img src="media/image6.png" style="width:6.5in;height:3.2125in" />

5\) Tactics Solving Page

<img src="media/image7.png" style="width:6.5in;height:3.14861in" />

6\) Invalid Move

<img src="media/image8.png" style="width:6.5in;height:3.16875in" />

7\) Valid Move

<img src="media/image9.png" style="width:6.5in;height:3.15694in" />

**Programming Contribution**

Frontend React Code Repo:
<https://github.com/KabirKanjani/ChessProject/tree/main/ChessPDF>

Python Flask Code Repo:
<https://github.com/KabirKanjani/ChessProject/tree/main/Flasking>

Chessboard to Fen Repo:
<https://github.com/KabirKanjani/ChessProject/tree/main/TensorflowJs>

**Tools, Technologies, APIs and Libraries used**

-   **Tools**

    -   Visual Studio Code

    -   PyCharm

    -   Notepad++

-   **Technologies**

    -   React

    -   Python

    -   Flask

    -   JavaScript

    -   Ajax

-   **APIs**

    -   Rest API

        -   Fetch APIs

        -   Ajax APIs

        -   Request APIs (Python)

-   **Libraries**

    -   MaterialUI

    -   Antd

    -   PDF2Image

    -   Flask

    -   OpenCV-Python

    -   Request

    -   React Chessboard

    -   Chess.js

    -   Stockfish

    -   TensorFlow

    -   Canvas

**Testing Strategies and Reports.**

1.  Invalid Login

> <img src="media/image10.png" style="width:6.5in;height:3.15764in" />

2.  Valid Login

> <img src="media/image11.png" style="width:6.5in;height:3.19236in" />

3.  Valid Move

<img src="media/image12.png" style="width:6.5in;height:3.15694in" />

4.  Invalid Move

<img src="media/image13.png" style="width:6.5in;height:3.16875in" />

5.  Invalid File Format (other than
    PDF)-<img src="media/image14.png" style="width:6.5in;height:3.15833in" />

**9. Any Innovative contribution if has been made**

1.  Converting PDF to Image

    -   Converting PDFs is quite a simple task with preinstalled
        > libraries provided in python, but when it comes to chess PDFs,
        > they can range from almost 200-500 pages usually which might
        > take like 15-20 minutes just to convert into high quality
        > images.

    -   Tried reducing the DPI i.e., Dots per Inch, referring to the
        > number of ink droplets and printer will produce per inch while
        > printing an image but because of the reduced quality of images
        > the detection techniques doesn’t work accurately.

    -   Tried various other libraries and methods but none of them
        > provided the required results. Finally, after a lot of
        > research and testing, found a way, which was convert images in
        > batches rather than all at once. So now we are converting
        > images in batch of 20 images at once and moving as per
        > requirement, thus creating the illusion of asynchronous
        > conversion.

2.  Chessboard Detection

-   Chessboard detection using OpenCV, for someone new to computer
    vision and ML, it was quite a task to learn how it works. At first,
    I tried detecting a square object in image for detecting a
    chessboard but it didn’t work as expected because the chessboard
    consists of squares so the OpenCV will detect the inner squares too
    which made it quite difficult.

-   Came across Chessboard Detection Corner method in OpenCV which takes
    arguments to detect concurrent squares together and group them,
    while it was quite amazing method on its own but because of the
    difference between the outer border of the board and the border
    between the squares of the board, it won’t detect the entire board
    together.

-   Played around with the method and made some adjustments to detect
    the boards.

**10. Lessons learnt**

-   Technologies

    -   React

    -   Flask

    -   Python

    -   JavaScript

    -   Ajax.

-   The longer you stay with your problems, the easier it becomes.

-   If you build something you genuinely want it wont look like much
    work rather fun.
