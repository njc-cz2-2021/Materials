import socket
import json

with open ('./resources/GAME.TXT') as f:
    data = [x.strip() for x in f.readlines()]

def printgrid(grid):
    for row in grid:
        print(''.join(row))

def reveal_all(grid):
    return [''.join(row) for row in grid]

def hide_ships(grid):
    hidden = []
    for row in grid:
        hidden.append(''.join('.' if cell == 'X' else cell for cell in row))
    return hidden

def game_server(conn):
    grid = [list(row) for row in data]
    missiles = 5

    conn.sendall(json.dumps(hide_ships(grid)).encode())

    while missiles > 0:
        raw = conn.recv(4029).decode()
        x, y = json.loads(raw)

        if grid[y][x] == 'X':
            grid[y][x] = 'S'   
            result = "HIT"
        elif grid[y][x] == '.':
            grid[y][x] = '0'  
            result = "MISS"
        else:
            result = "ALREADY_SHOT"

        missiles -= 1
        print(f"u fired at ({x},{y}): {result}, missiles left: {missiles}")
        printgrid(grid)

        if missiles == 0:
            response = {
                "grid": reveal_all(grid),
                "result": result,
                "game_over": True
            }
        else:
            response = {
                "grid": hide_ships(grid),
                "result": result,
                "game_over": False
            }
        conn.sendall(json.dumps(response).encode())

    conn.close()
    print("Game over. Connection closed.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 11111))
    server.listen(1)
    print("Server waiting for player...")

    conn, addr = server.accept()
    print(f"Player connected from {addr}")
    game_server(conn)
    server.close()

main()