class TetrisKickTable:
    def __init__(self):
        self.kick_table = {
            'I': [
                [(0, 0), (0, -2), (0, 1)],  # 0 -> 90
                [(0, 0), (0, -1), (0, 2)],  # 90 -> 180
                [(0, 0), (0, 2), (0, -1)],  # 180 -> 270
                [(0, 0), (0, 1), (0, -2)],  # 270 -> 0
            ],
            'L': [
                [(0, 0), (0, -1), (1, 0)],  # 0 -> 90
                [(0, 0), (1, 0), (-1, 0)],  # 90 -> 180
                [(0, 0), (0, 1), (1, 0)],   # 180 -> 270
                [(0, 0), (1, 0), (-1, 0)],  # 270 -> 0
            ],
            'J': [
                [(0, 0), (0, -1), (-1, 0)],  # 0 -> 90
                [(0, 0), (1, 0), (-1, 0)],   # 90 -> 180
                [(0, 0), (0, 1), (-1, 0)],    # 180 -> 270
                [(0, 0), (1, 0), (-1, 0)],    # 270 -> 0
            ],
            'T': [
                [(0, 0), (0, -1), (1, 0)],  # 0 -> 90
                [(0, 0), (1, 0), (-1, 0)],  # 90 -> 180
                [(0, 0), (0, 1), (1, 0)],   # 180 -> 270
                [(0, 0), (1, 0), (-1, 0)],  # 270 -> 0
            ],
          #이 밑으로 회전 없음
            'O': [
                [(0, 0), (0, 0), (0, 0)],  
                [(0, 0), (0, 0), (0, 0)],
                [(0, 0), (0, 0), (0, 0)],
                [(0, 0), (0, 0), (0, 0)],
            ],
            'S': [
                [(0, 0), (0, 0), (0, 0)],
                [(0, 0), (0, 0), (0, 0)],
                [(0, 0), (0, 0), (0, 0)],
                [(0, 0), (0, 0), (0, 0)],
            ],
            'Z': [
                [(0, 0), (0, 0), (0, 0)],
                [(0, 0), (0, 0), (0, 0)],
                [(0, 0), (0, 0), (0, 0)],
                [(0, 0), (0, 0), (0, 0)],
            ],
        }

    def get_kick_moves(self, tetromino, from_rotation, to_rotation):
        if tetromino in self.kick_table:
            return self.kick_table[tetromino][(from_rotation % 4)][1:]
        return []

def main():
    kick_table = TetrisKickTable()
    mino = input("미노 모양 입력 (L, J, S, Z, O, T, I): ").strip().upper()
    mlist = ['L', 'J', 'S', 'Z', 'O', 'T', 'I']
    fr = input("미노 상태 입력 (0, 1, 2, 3): ").strip()
    from_rotation = ['0', '1', '2', '3']
    tr = input("미노 회전 입력 (0, 1, 2, 3): ").strip()
    to_rotation = ['0', '1', '2', '3']
  
    try:
        fr = int(fr)
        tr = int(tr)
    except ValueError:
        print("회전 입력은 숫자여야 합니다.")
        return

    if mino in mlist and str(fr) in from_rotation and str(tr) in to_rotation:
        moves = kick_table.get_kick_moves(mino, fr, tr)
        print(f"{mino} 킥: {moves}")
    else:
        print("잘못된 값이 지정되었습니다. 다시 시작해주세요.")

if __name__ == "__main__":
    main()
