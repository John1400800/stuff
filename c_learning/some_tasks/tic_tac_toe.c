/*
** Tic Tac Toe
NOTEs
REWRITE: function to macro
ADD: field width more then 3 (checking digits)
*/

#include <stdio.h>

#define SPACE ' '
#define X 'X'
#define O 'O'

#define FIELD_SIZE 3
typedef char Field[FIELD_SIZE][FIELD_SIZE];

#define in_range(n, low, high) ((n) >= low && (n) <= high)
#define isdigit(c) ((c) >= '0' && (c) <= '9')

#define abs_to_x(abs, width) ((abs) % (width))
#define abs_to_y(abs, width) ((abs) / (width))

#define get_cell(abs_pos, field, width)                                        \
    ((field)[abs_to_y((abs_pos), (width))][abs_to_x((abs_pos), (width))])

#define set_cell(shape, abs_pos, width, field)                                 \
    (get_cell(abs_pos, field, width) = (shape))

#define field_cell_eq(req_val, abs_pos, width, field)                          \
    (get_cell(abs_pos, field, width) == (req_val))

void init_field(char shape, int width, char field[width][width]);
void drow_field(int width, char field[width][width]);
int victory_check(int width, char field[width][width]);
void get_num(int *res);

static Field field = {};

int main(void) {
    int who_win, abs_pos;
    char curr_shape;
    curr_shape = X;
    init_field(SPACE, FIELD_SIZE, field);

    while ((who_win = victory_check(FIELD_SIZE, field)) == SPACE) {
        drow_field(FIELD_SIZE, field);
        printf("%c step, enter pos(number from 0 to %d): ", curr_shape,
               FIELD_SIZE * FIELD_SIZE - 1);
        for (;;) { // enter and chaeck is valid pos
            get_num(&abs_pos);
            if (!in_range(abs_pos, 0, FIELD_SIZE * FIELD_SIZE - 1))
                printf("out of range, ");
            else if (!field_cell_eq(SPACE, abs_pos, FIELD_SIZE, field))
                printf("cell is occupied, ");
            else
                break;
            printf("try again: ");
        }
        set_cell(curr_shape, abs_pos, FIELD_SIZE, field);
        curr_shape = curr_shape == X ? O : X;
    }
    drow_field(FIELD_SIZE, field);
    if (who_win != SPACE)
        printf("%c win!\n", who_win);
    else
        printf("nobody's");
    return 0;
}

void init_field(char shape, int width, char field[width][width]) {
    int x_pos, y_pos;
    for (y_pos = 0; y_pos < width; ++y_pos)
        for (x_pos = 0; x_pos < width; ++x_pos)
            field[y_pos][x_pos] = shape;
}

void drow_field(int width, char field[width][width]) {
    int abs_pos, x_pos, y_pos;
    for (abs_pos = y_pos = 0; y_pos < width; ++y_pos)
        for (x_pos = 0; x_pos < width; ++x_pos, ++abs_pos)
            printf(x_pos == width - 1 ? "|%c|\n" : "|%c",
                   field[y_pos][x_pos] == ' ' ? '0' + abs_pos
                                              : field[y_pos][x_pos]);
}

void get_num(int *res) {
    int c, first_try, is_dig, isfirst_simbol;
    first_try = 1;
    do {
        if (!first_try)
            printf("incorrect input, try again: ");
        first_try = 0;

        for (*res = 0, isfirst_simbol = 1, is_dig = 1;
             (c = getchar()) != '\n';) {
            isfirst_simbol = 0;
            if (!isdigit(c) || !is_dig) {
                is_dig = 0;
                continue;
            }
            *res = *res * 10 + c - '0';
        }
    } while (!(is_dig && !isfirst_simbol));
}

int victory_check(int width, char field[width][width]) {
    int pos, x_pos, y_pos;
    for (pos = 1; pos < width; ++pos) // checking left to right diagonals
        if (field[pos - 1][pos - 1] != field[pos][pos])
            break;
    if (pos == width && field[pos - 1][pos - 1] != ' ')
        return field[pos - 1][pos - 1];
    for (pos = width - 1; pos > 0; --pos) { // checking right to left diagonals
        if (field[pos - 1][pos - 1] != field[pos][pos])
            break;
    }
    
    if (pos == 0 && field[pos][pos] != ' ')
        return field[pos - 1][pos - 1];
    for (y_pos = 0; y_pos < width; ++y_pos) { // checking coutours
        for (x_pos = 1; x_pos < width; ++x_pos)
            if (field[y_pos][x_pos - 1] != field[y_pos][x_pos])
                break;
        if (x_pos == width && field[y_pos][x_pos - 1] != ' ')
            return field[y_pos][x_pos - 1];
    }
    
    for (x_pos = 0; x_pos < width; ++x_pos) { // checking vertical
        for (y_pos = 1; y_pos < width; ++y_pos)
            if (field[y_pos - 1][x_pos] != field[y_pos][x_pos])
                break;
        if (y_pos == width && field[y_pos - 1][x_pos] != ' ')
            return field[y_pos - 1][x_pos];
    }
    return SPACE;
}
