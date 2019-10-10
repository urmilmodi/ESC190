#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int white = 1;
int black = -1;
int empty = 0;
int limit = 2147483647;

int render(int *board, int size);
int* genboard(int rows);
int bishopcontrol(int sidelength, int position, int direction);
int printarray(int *board, int size);
int* move(int* board, int rows, int player, int pos);
int* getneighbours(int *board, int rows, int pos);
int* GetPlayerPositions(int *board, int rows, int player);
int* GetPlayerLegalMoves(int *board, int rows, int player);
int rate(int *board, int size);
int GameOver(int *board, int size);
int* AlphaBeta(int *board, int rows, int player, int depth, int alpha, int beta, double countdown, int *Master);
int* reversiplayer(int *board, int rows, int player);
int Game();

int render(int *board, int rows) {
    if (board == NULL || rows < 0) {
        return 0;
    }
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < rows; j++) {
            if (j == 0) {
                if (board[i*rows + j] == empty) {
                    printf("| / |");

                } else if (board[i*rows + j] == white) {
                    printf("| W |");

                } else if (board[i*rows + j] == black) {
                    printf("| B |");
                }
            } else {
                if (board[i*rows + j] == empty) {
                    printf(" / |");

                } else if (board[i*rows + j] == white) {
                    printf(" W |");

                } else if (board[i*rows + j] == black) {
                    printf(" B |");
                }
            }
        }
        printf("    ");

        for (int j = 0; j < rows; j++) {
            if (j == 0) {
                if (i*rows + j < 10) {
                    printf("|  %d |", i*rows + j);
                
                } else {
                    printf("| %d |", i*rows + j);
                }
            } else {
                if (i*rows + j < 10) {
                    printf("  %d |", i*rows + j);
                
                } else {
                    printf(" %d |", i*rows + j);
                }
            }
        }
        printf("\n");
    }
    return 1;
}

// Returns non-empty Neighbours (indexes) of an index on the board
int* getneighbours(int* board, int rows, int pos) {
    if (board == NULL || pos < 0 || pos > rows*rows - 1) {
        printf("get neighbours issue");
        return NULL;
    }
    int *neighbours = (int *)malloc(9*sizeof(int));
    int k = 1;
    int max = (rows - 1)*rows - 1;
    if (pos % rows == 0) {

        if (pos < rows) {
            if (board[pos + 1] == empty) {
                neighbours[k] = pos + 1;
                k++;
            
            }
            if (board[pos + rows] == empty) {
                neighbours[k] = pos + rows;
                k++;

            }
            if (board[pos + rows + 1] == empty) {
                neighbours[k] = pos + rows + 1;
                k++;
            }
    
        } else if (pos > max) {
            if (board[pos + 1] == empty) {
                neighbours[k] = pos + 1;
                k++;
            
            }
            if (board[pos - rows] == empty) {
                neighbours[k] = pos - rows;
                k++;

            }
            if (board[pos - rows + 1] == empty) {
                neighbours[k] = pos - rows + 1;
                k++;
            }

        } else {
            if (board[pos + 1] == empty) {
                neighbours[k] = pos + 1;
                k++;
            
            }
            if (board[pos + rows] == empty) {
                neighbours[k] = pos + rows;
                k++;

            }
            if (board[pos + rows + 1] == empty) {
                neighbours[k] = pos + rows + 1;
                k++;
            
            }
            if (board[pos - rows] == empty) {
                neighbours[k] = pos - rows;
                k++;

            }
            if (board[pos - rows + 1] == empty) {
                neighbours[k] = pos - rows + 1;
                k++;
            }
        }
    
    } else if (pos % rows == rows - 1) {

        if (pos < rows) {
            if (board[pos - 1] == empty) {
                neighbours[k] = pos - 1;
                k++;
            
            }
            if (board[pos + rows] == empty) {
                neighbours[k] = pos + rows;
                k++;

            }
            if (board[pos + rows - 1] == empty) {
                neighbours[k] = pos + rows - 1;
                k++;
            }
    
        } else if (pos > max) {
            if (board[pos - 1] == empty) {
                neighbours[k] = pos - 1;
                k++;
            
            } 
            if (board[pos - rows] == empty) {
                neighbours[k] = pos - rows;
                k++;

            } 
            if (board[pos - rows - 1] == empty) {
                neighbours[k] = pos - rows - 1;
                k++;
            }

        } else {
            if (board[pos - 1] == empty) {
                neighbours[k] = pos - 1;
                k++;
            
            }
            if (board[pos - rows] == empty) {
                neighbours[k] = pos - rows;
                k++;

            }
            if (board[pos - rows - 1] == empty) {
                neighbours[k] = pos - rows - 1;
                k++;
            
            } 
            if (board[pos + rows] == empty) {
                neighbours[k] = pos + rows;
                k++;

            }
            if (board[pos + rows - 1] == empty) {
                neighbours[k] = pos + rows - 1;
                k++;
            }
        }
    
    } else if (pos < rows) {

        if (board[pos - 1] == empty) {
            neighbours[k] = pos - 1;
            k++;
            
        }
        if (board[pos + rows] == empty) {
            neighbours[k] = pos + rows;
            k++;

        }
        if (board[pos + rows - 1] == empty) {
            neighbours[k] = pos + rows - 1;
            k++;
        
        } 
        if (board[pos + rows + 1] == empty) {
            neighbours[k] = pos + rows + 1;
            k++;

        } 
        if (board[pos + 1] == empty) {
            neighbours[k] = pos + 1;
            k++;
        }
    
    } else if (pos > max) {

        if (board[pos - 1] == empty) {
            neighbours[k] = pos - 1;
            k++;
            
        }
        if (board[pos - rows] == empty) {
            neighbours[k] = pos - rows;
            k++;

        }
        if (board[pos - rows - 1] == empty) {
            neighbours[k] = pos - rows - 1;
            k++;
        
        }
        if (board[pos - rows + 1] == empty) {
            neighbours[k] = pos - rows + 1;
            k++;

        }
        if (board[pos + 1] == empty) {
            neighbours[k] = pos + 1;
            k++;
        }

    } else {

        if (board[pos - 1] == empty) {
            neighbours[k] = pos - 1;
            k++;
            
        }
        if (board[pos - rows] == empty) {
            neighbours[k] = pos - rows;
            k++;

        }
        if (board[pos - rows - 1] == empty) {
            neighbours[k] = pos - rows - 1;
            k++;
        
        }
        if (board[pos - rows + 1] == empty) {
            neighbours[k] = pos - rows + 1;
            k++;

        }
        if (board[pos + 1] == empty) {
            neighbours[k] = pos + 1;
            k++;
            
        }
        if (board[pos + rows] == empty) {
            neighbours[k] = pos + rows;
            k++;

        }
        if (board[pos + rows - 1] == empty) {
            neighbours[k] = pos + rows - 1;
            k++;
        
        }
        if (board[pos + rows + 1] == empty) {
            neighbours[k] = pos + rows + 1;
            k++;
        
        }
    }
    neighbours[0] = k;
    return neighbours;
}

int* move(int* board, int rows, int player, int pos) {
    if (board == NULL || (player != black && player != white) || pos < 0 || pos > rows*rows - 1 || board[pos] != empty) {
        printf("set move issue\n");
        render(board, rows);
        printarray(board, rows*rows);
        printf("player - %d, pos - %d, value - %d", player, pos, board[pos]);
        return board;
    }
    int size = rows*rows;
    int i = 0;
    int *newboard = (int *)malloc(sizeof(int)*size);
    for (i = 0; i < size; i++) {
        newboard[i] = board[i];
    }
    newboard[pos] = player;
    int adj = 1;
    for (adj = 1; adj < (pos % rows + 1) && newboard[pos + adj] != empty; adj++) {

        if (newboard[pos + adj] == player) {
            for (i = 1; i < adj; i++) {
                //if (newboard[pos + i] == empty) {break;}
                newboard[pos + i] = player;
            }
        }
    }
    for (adj = 1; adj < (rows - pos % rows) && newboard[pos - adj] != empty; adj++) {

        if (newboard[pos - adj] == player) {
            for (i = 1; i < adj; i++) {
                //if (newboard[pos - i] == empty) {break;}
                newboard[pos - i] = player;
            }
        }
    }
    for (adj = 1; adj < (floor(pos / rows) + 1) && newboard[pos - rows*adj] != empty; adj++) {

        if (newboard[pos - rows*adj] == player) {
            for (i = 1; i < adj; i++) {
                //if (newboard[pos - rows*i] == empty) {break;}
                newboard[pos - rows*i] = player;
            }
        }
    }
    for (adj = 1; adj < (rows - floor(pos / rows)) && newboard[pos + rows*adj] != empty; adj++) {

        if (newboard[pos + rows*adj] == player) {
            for (i = 1; i < adj; i++) {
                //if (newboard[pos + rows*i] == empty) {break;}
                newboard[pos + rows*i] = player;
            }
        }
    }
    for (adj = 1; adj < bishopcontrol(rows, pos, 0) && newboard[pos + (rows + 1)*adj] != empty; adj++) {

        if (newboard[pos + (rows + 1)*adj] == player) {
            for (i = 1; i < adj; i++) {
                if (newboard[pos + (rows + 1)*i] == empty) {break;}
                newboard[pos + (rows + 1)*i] = player;
            }
        }
    }
    for (adj = 1; adj < bishopcontrol(rows, pos, 1) && newboard[pos + (rows - 1)*adj] != empty; adj++) {

        if (newboard[pos + (rows - 1)*adj] == player) {
            for (i = 1; i < adj; i++) {
                if (newboard[pos + (rows - 1)*i] == empty) {break;}
                newboard[pos + (rows - 1)*i] = player;
            }
        }
    }
    for (adj = 1; adj < bishopcontrol(rows, pos, 2) && newboard[pos - (rows + 1)*adj] != empty; adj++) {

        if (newboard[pos - (rows + 1)*adj] == player) {
            for (i = 1; i < adj; i++) {
                if (newboard[pos - (rows + 1)*i] == empty) {break;}
                newboard[pos - (rows + 1)*i] = player;
            }
        }
    }
    for (adj = 1; adj < bishopcontrol(rows, pos, 3) && newboard[pos - (rows - 1)*adj] != empty; adj++) {

        if (newboard[pos - (rows - 1)*adj] == player) {
            for (i = 1; i < adj; i++) {
                if (newboard[pos - (rows - 1)*i] == empty) {break;}
                newboard[pos - (rows - 1)*i] = player;
            }
        }
    }
    return newboard;
}

// Diagonal Movement Algorithm
int bishopcontrol(int sidelength, int position, int direction) {
    
    // Right Down
    if (direction == 0) {
        for (int i = 0; i < sidelength - 1; i++) {
            if (position > (-1 + (sidelength + 1)*i) && position < (sidelength + sidelength*i)) {
                
                return sidelength - position % sidelength;
            }
        }
        return sidelength - floor(position / sidelength);
    }
    // Left Down
    else if (direction == 1) {
        for (int i = 0; i < sidelength - 1; i++) {
            if (position > (-1 + sidelength*i) && position < (sidelength + (sidelength - 1)*i)) {
                
                return 1 + position % sidelength;
            }
        }
        return sidelength - floor(position / sidelength);
    }
    // Left Up
    else if (direction == 2) {
        for (int i = 0; i < sidelength - 1; i++) {
            if (position > (-1 + (sidelength + 1)*i) && position < (sidelength + sidelength*i)) {
                
                return 1 + floor(position / sidelength);
            }
        }
        return 1 + position % sidelength;
    }
    // Right Up
    else if (direction == 3) {
        for (int i = 0; i < sidelength - 1; i++) {
            if (position > (-1 + sidelength*i) && position < (sidelength + (sidelength - 1)*i)) {
                
                return 1 + floor(position / sidelength);
            }
        }
        return sidelength - position % sidelength;
    }
    return 0;
}

int* GetPlayerPositions(int *board, int rows, int player) {
    if (board == NULL || (player != black && player != white)) {
        printf("player position issue");
        return NULL;
    }
    int size = rows*rows;
    int *positions = (int *)malloc(sizeof(int)*(size + 1)); // 0th Index represents the size, assumption of worst case
    int j = 1;
    for (int i = 0; i < size; i++) {
        if (board[i] == player) {
            positions[j] = i;
            j++;
        }
    }
    positions[0] = j;
    return positions;
}

int* GetPlayerLegalMoves(int *board, int rows, int player) {
    if (board == NULL || (player != black && player != white)) {
        printf("get moves issue");
        return NULL;
    }
    int size = rows*rows;
    int *moves = (int *)malloc(sizeof(int)*(size + 1)); // Algorithm to GetMoves is slow but works ¯\_(ツ)_/¯
    int *hash = (int *)malloc(size*sizeof(int)); // Hash ensures no repeating moves
    int i = 0, j = 0, k = 1;
    for (i = 0; i < size; i++) {
        hash[i] = 1;
    }
    for (i = 0; i < size; i++) {
        if (board[i] != empty) {
            int *neighbours = getneighbours(board, rows, i);
            for (j = 1; j < neighbours[0]; j++) {
                if (hash[neighbours[j]]) {
                    moves[k] = neighbours[j];
                    k++;
                    hash[neighbours[j]] = 0;
                }
            }
            free(neighbours);
        }
    }
    moves[0] = k;
    free(hash);
    return moves;
}

int* AlphaBeta(int *board, int rows, int player, int depth, int alpha, int beta, double countdown, int *Master) {

    // Return Value: {Board Rating, Move}
    clock_t start = clock();
    int *rv = (int *)malloc(2*sizeof(int));
    int size = rows*rows;
    if (depth == 0 || GameOver(board, size) || countdown <= 0) {
        if (countdown <= 0) {*Master = 1;}
        rv[0] = rate(board, size);
        rv[1] = -1;
        return rv;
    }
    int *moves = GetPlayerLegalMoves(board, rows, player);
    for (int j = 1; j < moves[0]; j++) {
        
        int newpos = moves[j];
        int *newboard = move(board, rows, player, newpos);

        if (player == white) {
            int *currentscore = AlphaBeta(newboard, rows, black, depth - 1, alpha, beta, countdown - ((double) (clock() - start)) / CLOCKS_PER_SEC, Master);
            if (currentscore[0] > alpha) {
                alpha = currentscore[0];
                rv[1] = newpos;
            }
            free(currentscore);
                
        } else if (player == black) {
            int *currentscore = AlphaBeta(newboard, rows, white, depth - 1, alpha, beta, countdown - ((double) (clock() - start)) / CLOCKS_PER_SEC, Master);
            if (currentscore[0] < beta) {
                beta = currentscore[0];
                rv[1] = newpos;
            }
            free(currentscore);
        }
        free(newboard);

        if (alpha >= beta) {
            break;
        }
    }
    free(moves);

    if (player == white) {
        rv[0] = alpha;
    
    } else if (player == black) {
        rv[0] = beta;
    }
    return rv;
}

int rate(int *board, int size) {
    int score = 0;
    int i = 0;
    for (i = 0; i < size; i++) {
        if (board[i] == white) {
            score++;

        } else if (board[i] == black) {
            score--;
        }
    }
    int rows = (int) sqrt(size);
    if (board[0] == white) {score++;}
    else if (board[0] == black) {score--;}
    if (board[rows] == white) {score++;}
    else if (board[rows] == black) {score--;}
    if (board[size - 1] == white) {score++;}
    else if (board[size - 1] == black) {score--;}
    if (board[size - rows] == white) {score++;}
    else if (board[size - rows] == black) {score--;}
    return score;
}

int GameOver(int *board, int size) {
    for (int i = 0; i < size; i++) {
        if (board[i] == empty) {
            return 0;
        }
    }
    return 1;
}

// Return Value: {1 or 0 to represent Success, Move as an Index}
int* reversiplayer(int *board, int rows, int player) {
    double countdown = 9.9/10;
    double timetaken = 0;
    clock_t start, end;
    int *active = NULL;
    int *rv = (int *)malloc(2*sizeof(int));
    int depth = 1;
    int Master = 0;
    for (depth = 1; depth < 15 && countdown > 0; depth++) {
        start = clock();
        free(active);
        active = NULL;
        active = AlphaBeta(board, rows, player, depth, -limit, limit, countdown, &Master);
        end = clock();
        timetaken = ((double) (end - start)) / CLOCKS_PER_SEC;
        countdown -= timetaken;
        if (active[1] != -1 && Master == 0) {
            rv[0] = active[0];
            rv[1] = active[1];
            printf("Depth - %d, Time Left - %f, Move - %d\n", depth, countdown, rv[1]);

        } else {break;}
        if (rv[0] == limit || rv[0] == -limit) {break;}
    }
    rv[0] = 1;
    printf("Final Depth - %d\n", depth - 2);
    return rv;
}

int* genboard(int rows) {
    if (rows % 2 == 1) {
        rows++;
    }
    int size = rows*rows;
    int *board = (int *)malloc(size*sizeof(int));
    for (int i = 0; i < size; i++) {
        board[i] = empty;
    }
    int value = rows/2 - 1;
    board[value*rows + value] = white;
    board[rows*(value + 1) + value + 1] = white;
    board[value*rows + value + 1] = black;
    board[rows*(value + 1) + value] = black;
    return board;
}

int printarray(int *array, int size) {
    if (size == 0) { // 0th Index represents the size
        printf("Running Dynamic Size\n");
        printf("{");
        for (int i = 1; i < array[0]; i++) {
            if (i != size - 1) {printf("%d, ", array[i]);}
            else {printf("%d", array[i]);}
        }
        printf("}");
        printf("\n");
        return 0;
    }
    printf("{");
    for (int i = 0; i < size; i++) {
        if (i != size - 1) {printf("%d, ", array[i]);}
        else {printf("%d", array[i]);}
    }
    printf("}");
    printf("\n");
    return 0;
}

int Game() {
    // Plays Against Itself
    int rows = 0;
    printf("Enter row, or col size: ");
    scanf("%d", &rows);
    rows = 8;
    int Turn = 1;
    int score = 0;
    int *board = genboard(rows);
    render(board, rows);
    printf("\n");
    while (!GameOver(board, rows*rows)) {
        clock_t start;
        start = clock();
        int *playermove = reversiplayer(board, rows, Turn);
        printf("Time Taken: %f\n", ((double) (clock() - start)) / CLOCKS_PER_SEC);
        if (playermove[0] == 1) {
            int *newboard = move(board, rows, Turn, playermove[1]);
            free(playermove);
            free(board);
            board = newboard;
        } else {break;}
        render(board, rows);
        printarray(board, rows*rows);
        score = rate(board, rows*rows);
        printf("Score: %d\n", score);
        printf("\n");
        if (Turn == 1) {Turn = -1;}
        else {Turn = 1;}
    }
    if (score > 0) {printf("White Won!\n");}
    else {printf("Black Won!\n");}
    return 0;
}

int main(void) { 
    clock_t start;
    start = clock();
    Game();
    printf("%f\n", ((double) (clock() - start)) / CLOCKS_PER_SEC);
    return 0;
}
