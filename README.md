# ChessUtils
Personal utilities for chess stuff

### rename.py

This utility renames the Event tags in a multi-game pgn file to "Puzzle 1", "Puzzle 2", etc. in sequential order. I wrote this utility to give names to the Workbooks created by [GLSmyth](https://chessmeanderings.wordpress.com/how-to-create-the-full-colle-zukertort-for-club-players-course-2/) in support of his Chessable course [Colle-Zukertort](https://www.chessable.com/course/325675) course on Chessable.com. In the first link above, GLSmyth shows how to combine the [Dealing with Anti-Colle Systems for Club Players](https://www.chessable.com/course/325675) and [The Colle-Zukertort for Club Players](https://www.chessable.com/course/390600) into a single course. On the Chessable Discussion forum for the Anti-Colle Systems course, GLSmyth kindly provides 4 Workbooks to be included in the course. I wanted the individual positions to have different names than the Chessable default, so I created this script to rename the Event tags for each of the positions in the 4 Workbooks (and the Original workbook for the main Colle-Zukertort course). This script renames each of the workbook files so the Event tags read "Puzzle 1", "Puzzle 2", etc so that those are the names given by Chessable.

Usage:

```
python3 rename.py file-in.pgn file-out.pgn
```
