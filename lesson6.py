from chess import are_queens_attacking

def main():
    # Пример расстановки 8 ферзей (координаты от 1 до 8)
    queens = [
        (1, 5),
        (2, 8),
        (3, 2),
        (4, 4),
        (5, 1),
        (6, 3),
        (7, 7),
        (8, 6)
    ]
    
    if are_queens_attacking(queens):
        print("Ферзи не бьют друг друга.")
    else:
        print("Ферзи бьют друг друга.")

if __name__ == "__main__":
    main()
