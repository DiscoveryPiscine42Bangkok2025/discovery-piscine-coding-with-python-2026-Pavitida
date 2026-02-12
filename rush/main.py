from checkmate import checkmate
import io
import sys


def run_test(name, board, expected):
    captured_output = io.StringIO()
    sys.stdout = captured_output

    checkmate(board)

    sys.stdout = sys.__stdout__
    result = captured_output.getvalue().strip()
    status = "PASS" if result == expected else "FAIL"

    print(f"{name:<22} Expected: {expected:<7} Got: {result:<7} {status}")


def main():
    print("\nCHECKMATE TEST SUITE\n")

    run_test("Not square board", """R...
.K.....
..P.
....""", "Error")

    run_test("No King", """R...
....
..P.
....""", "Error")

    run_test("Multiple Kings", """K...
.K..
....
....""", "Error")

    run_test("Bishop blocked", """B...
.P..
..K.
....""", "Fail")

    run_test("Rook blocked", """R.P.
.K..
....
....""", "Fail")

    run_test("Queen diagonal long", """Q...
....
....
...K""", "Success")

    run_test("Pawn check", """....
..P.
.K..
....""", "Success")

    run_test("Random characters", """A..R
.ZK.
..T.
....""", "Success")

    run_test("2x2 board", """.K
R.""", "Success")

    run_test("King corner", """K...
....
....
...Q""", "Success")

    print("\nEND OF TESTS\n")


if __name__ == "__main__":
    main()