def checkmate(board):
    rows = board.strip().split("\n")
    n = len(rows)

    if any(len(row) != n for row in rows):
        print("Error")
        return

    king = None
    for r in range(n):
        for c in range(n):
            if rows[r][c] == 'K':
                king = (r, c)
                break
        if king:
            break

    if not king:
        print("Error")
        return

    if king_in_check(rows, king):
        print("Success")
    else:
        print("Fail")


def king_in_check(board, king):
    n = len(board)
    kr, kc = king

    for dc in (-1, 1):
        r, c = kr - 1, kc + dc
        if 0 <= r < n and 0 <= c < n and board[r][c] == 'P':
            return True

    for dr, dc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = board[r][c]
            if piece != '.':
                if piece in ('B', 'Q'):
                    return True
                break
            r += dr
            c += dc

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        r, c = kr + dr, kc + dc
        while 0 <= r < n and 0 <= c < n:
            piece = board[r][c]
            if piece != '.':
                if piece in ('R', 'Q'):
                    return True
                break
            r += dr
            c += dc

    return False
