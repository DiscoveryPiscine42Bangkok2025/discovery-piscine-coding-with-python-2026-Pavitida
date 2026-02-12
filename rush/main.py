from checkmate import checkmate

def main():
    board1 = """R.K.
....
....
...."""
    print("Example 1 (Rook check):")
    checkmate(board1)

    board2 = """....
.K..
..B.
...."""
    print("\nExample 2 (Bishop check):")
    checkmate(board2)

    board3 = """Q...
.K..
....
...."""
    print("\nExample 3 (Queen check):")
    checkmate(board3)

    board4 = """....
PK..
....
...."""
    print("\nExample 4 (Pawn check):")
    checkmate(board4)

    board5 = """....
.K..
.R..
...."""
    print("\nExample 5 (Vertical Rook check):")
    checkmate(board5)

    board6 = """R...
.K..
..P.
...."""
    print("\nExample 6 (Mixed pieces):")
    checkmate(board6)


if __name__ == "__main__":
    main()
