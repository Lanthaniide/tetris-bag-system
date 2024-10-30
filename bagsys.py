import random

def generate_bag():
    tetrominoes = ['I', 'J', 'L', 'O', 'S', 'T', 'Z'] #미노 순서(아무렇게나 해도 됨)
    random.shuffle(tetrominoes) #섞음
    return tetrominoes

def main():
    while True:
        bag = generate_bag() #1가방 생성
        for i in range(7): #순서대로 가방 출력
            input(f"다음 미노: {bag[i]}")

if __name__ == "__main__":
    main()
