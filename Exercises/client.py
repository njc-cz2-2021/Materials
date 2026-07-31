import socket
import json

def printgrid(grid):
    print("\n  0 1 2 3 4") 
    for i, row in enumerate(grid):
        print(f"{i} {' '.join(row)}")
    print()

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 11111))
    print("Connected to server!")

    raw = client.recv(4096).decode()
    grid = json.loads(raw)
    printgrid(grid)

    missiles = 5

    while missiles > 0:
        print(f"Missiles remaining: {missiles}")
        try:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
        except ValueError:
            print("Invalid input, enter numbers only.")
            continue

        client.sendall(json.dumps([x, y]).encode())

        raw = client.recv(4096).decode()
        response = json.loads(raw)

        print(f"\n>>> {response['result']} <<<")
        printgrid(response['grid'])

        missiles -= 1

        if response['game_over']:
            print("game over")
            break

    client.close()
    print("Disconnected.")

main()