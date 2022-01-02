def isValidChessBoard(arrangement):
    accepted_numb = ['1','2','3','4','5','6','7','8']
    accepted_alpha = ['a','b','c','d','e','f','g','h']
    pieces = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']
    for piece in arrangement:
        if piece[0] not in accepted_numb:
            return False
        elif piece[1] not in accepted_alpha:
            return False
    for piece in arrangement.values():
        if piece[0]!='w' and piece[0]!='b':
            return False
        elif piece[1:] not in pieces:
            return False
    return True
        
given_arrangement = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(given_arrangement))