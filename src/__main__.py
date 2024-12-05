from enum import Enum

COLLUMNS = ["a", "b", "c", "d", "e", "f", "g", "h"]
COLLUMN_TO_INDEX = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}

class ChessColor(Enum):
    BLACK = 0
    WHITE = 1

    def into_str(self):
        return "black" if self == ChessColor.BLACK else "white"

class PieceType(Enum):
    PAWN = 1
    BISHOP = 3
    KNIGHT = 3
    ROOK = 5
    QUEEN = 9
    # TODO make this bignum once i find smth im lazy
    KING = 10^10

class Piece:
    def __init__(self, piece_type, piece_color):
        assert isinstance(piece_type, PieceType)
        assert isinstance(piece_color, ChessColor)

        self.piece_type = piece_type
        self.piece_color = piece_color

    def into_str(self):
        if self.piece_color == ChessColor.BLACK:
            match self.piece_type:
                case PieceType.PAWN:
                    return "♙"
                case PieceType.BISHOP:
                    return "♗"
                case PieceType.KNIGHT:
                    return "♘"
                case PieceType.ROOK:
                    return "♖"
                case PieceType.QUEEN:
                    return "♕"
                case PieceType.KING:
                    return "♔"

        match self.piece_type:
            case PieceType.PAWN:
                return "♟"
            case PieceType.BISHOP:
                return "♝"
            case PieceType.KNIGHT:
                return "♞"
            case PieceType.ROOK:
                return "♜"
            case PieceType.QUEEN:
                return "♛"
            case PieceType.KING:
                return "♚"

class Position:
    def __init__(self, row, collumn):
        assert row >= 0 and row < 8
        assert collumn >= 0 and collumn < 8

        self.row = row
        self.collumn = collumn

    @staticmethod
    def from_str(str: str):
        assert len(str) == 2
        str = str.lower()

        row = int(str[1]) - 1
        collumn = COLLUMN_TO_INDEX[str[0:1]]

        assert row >= 0 and row < 8
        assert collumn >= 0 and collumn < 8

        return Position(row, collumn)

def piece_from_position(board, piece_position, color):
    assert isinstance(piece_position, Position)

    row = board[piece_position.row]

    if len(row) < piece_position.collumn:
        return None

    piece = row[piece_position.collumn]
    return piece if isinstance(piece, Piece) and (not isinstance(color, ChessColor) or piece.piece_color == color) else None

def is_valid_move(board, piece_position, to_position):
    assert isinstance(piece_position, Position)
    assert isinstance(to_position, Position)

    return True

def is_checkmate(board, current_color):
    assert isinstance(current_color, ChessColor)

    return False

def render_board(board):
    output = ""

    for index, row in enumerate(board):
        padding_collumn = ""
        piece_collumn = ""

        for collumn in range(8):
            piece = None
            if len(row) >= collumn + 1:
                piece = row[collumn]

            fill = "░" if (index % 2 and collumn % 2) or (index % 2 == 0 and collumn % 2 == 0) else "█"
            padding_collumn += fill * 4

            if piece == None:
                piece_collumn += fill * 4
                continue

            piece_collumn += f"{fill * 3}{piece.into_str()}"

        output += f"  {padding_collumn}\n{index + 1} {piece_collumn}\n"

    collumn_labels = ""
    for col in COLLUMNS:
        collumn_labels += "   " + col.upper()

    output += f"  {collumn_labels}\n"
    print(output)

if __name__ == "__main__":
    board = [
        # row 1
        [
            Piece(PieceType.ROOK, ChessColor.BLACK),
            Piece(PieceType.KNIGHT, ChessColor.BLACK),
            Piece(PieceType.BISHOP, ChessColor.BLACK),
            Piece(PieceType.QUEEN, ChessColor.BLACK),
            Piece(PieceType.KING, ChessColor.BLACK),
            Piece(PieceType.BISHOP, ChessColor.BLACK),
            Piece(PieceType.KNIGHT, ChessColor.BLACK),
            Piece(PieceType.ROOK, ChessColor.BLACK)
        ],
        # row 2
        [
            Piece(PieceType.PAWN, ChessColor.BLACK),
            Piece(PieceType.PAWN, ChessColor.BLACK),
            Piece(PieceType.PAWN, ChessColor.BLACK),
            Piece(PieceType.PAWN, ChessColor.BLACK),
            Piece(PieceType.PAWN, ChessColor.BLACK),
            Piece(PieceType.PAWN, ChessColor.BLACK),
            Piece(PieceType.PAWN, ChessColor.BLACK),
            Piece(PieceType.PAWN, ChessColor.BLACK),
        ],
        # row 3
        [],
        # row 4
        [],
        # row 5
        [],
        # row 6
        [],
        # row 7
        [
            Piece(PieceType.PAWN, ChessColor.WHITE),
            Piece(PieceType.PAWN, ChessColor.WHITE),
            Piece(PieceType.PAWN, ChessColor.WHITE),
            Piece(PieceType.PAWN, ChessColor.WHITE),
            Piece(PieceType.PAWN, ChessColor.WHITE),
            Piece(PieceType.PAWN, ChessColor.WHITE),
            Piece(PieceType.PAWN, ChessColor.WHITE),
            Piece(PieceType.PAWN, ChessColor.WHITE),
        ],
        # row 8
        [
            Piece(PieceType.ROOK, ChessColor.WHITE),
            Piece(PieceType.KNIGHT, ChessColor.WHITE),
            Piece(PieceType.BISHOP, ChessColor.WHITE),
            Piece(PieceType.KING, ChessColor.WHITE),
            Piece(PieceType.QUEEN, ChessColor.WHITE),
            Piece(PieceType.BISHOP, ChessColor.WHITE),
            Piece(PieceType.KNIGHT, ChessColor.WHITE),
            Piece(PieceType.ROOK, ChessColor.WHITE)
        ]
    ]

    current_turn = ChessColor.WHITE
    turn_count = 1

    print("chess by bill nguyen class of '2028 as supporting demo for AP Computer Science A")
    while not is_checkmate(board, current_turn):
        print("\n" * 8)

        print(f"turn no. {turn_count}")
        render_board(board)
        print(f"now {current_turn.into_str()}"'s turn')

        piece_position = None
        target_piece = None

        # TODO check for no possible moves
        while target_piece == None:
            piece_position = Position.from_str(input("input piece (eg. a1) to move: "))
            target_piece = piece_from_position(board, piece_position, current_turn)

            if not target_piece:
                print("invalid piece")
            else:
                break

        move_to = Position.from_str(input("input position (eg. a1) to move piece: "))

        print(target_piece.piece_type, target_piece.piece_color)
        print(move_to.row, move_to.collumn)

        current_turn = ChessColor.BLACK if current_turn == ChessColor.WHITE else ChessColor.WHITE
        turn_count += 1

    print(board)
