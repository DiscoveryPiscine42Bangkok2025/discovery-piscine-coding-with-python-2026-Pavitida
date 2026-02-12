def checkmate(board):
    rows = board.strip().split("\n")
    n = len(rows)

    # Validate square board
    if n == 0 or any(len(row) != n for row in rows):
        print("Error")
        return

    # Find King
    kings = [(r, c) for r in range(n) for c in range(n) if rows[r][c] == 'K']
    if len(kings) != 1:
        print("Error")
        return

    king = kings[0]

    if king_in_check(rows, king):
        print("Success")
    else:
        print("Fail")


# -----------------------------

def is_enemy(piece):
    return piece in "PRBQ"


def is_piece(piece):
    return piece in "KPRBQ"


def king_in_check(board, king):
    n = len(board)
    kr, kc = king

    # --- Pawn ---
    for dr in (-1, 1):
        for dc in (-1, 1):
            r, c = kr + dr, kc + dc
            if 0 <= r < n and 0 <= c < n:
                if board[r][c] == 'P':
                    return True

    # --- Bishop / Queen (diagonal) ---
    for dr, dc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = board[r][c]

            if is_enemy(piece):
                if piece in ('B', 'Q'):
                    return True
                break

            if is_piece(piece):  # other piece blocks
                break

            # otherwise empty square → continue
            r += dr
            c += dc

    # --- Rook / Queen (straight) ---
    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = board[r][c]

            if is_enemy(piece):
                if piece in ('R', 'Q'):
                    return True
                break

            if is_piece(piece):
                break

            r += dr
            c += dc

    return False
