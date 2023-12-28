#include <stdio.h>

unsigned get_beats(unsigned source, unsigned start, unsigned n_pos) {
    return source >> start & ~(~0u << n_pos);
}

void reverse(char *source) {
    char buff;
    unsigned low = 0;
    unsigned high = 0;
    while (source[high] != '\0') {
        ++high;
    }
    high--;
    while (low < high) {
        buff = source[high];
        source[high] = source[low];
        source[low] = buff;
        ++low;
        --high;
    }
}

void unsigned_to_beats(unsigned beats, char *res) {
    unsigned i = 0;
    do {
        res[i++] = '0' + (beats & 1u);
    } while (beats >>= 1);
    res[i] = '\0';
    reverse(res);
}

unsigned beats_to_unsigned(char *source) {
    unsigned res = 0;
    unsigned i = 0;
    while (source[i] == '1' || source[i] == '0') {
        res = res << 1 | (source[i] == '1');
        ++i;
    }
    return res;
}
/* `get_beats': in this case returns
        3 bit positions started with
        3 beat_idx from `beats` (beat_idx are counted with zero value 0, 1, 2,
   3) */

int main() {
    char res_beats[100];

    unsigned beats = beats_to_unsigned("10101000");
    unsigned_to_beats(get_beats(beats, 3, 3), res_beats);
    printf("%s", res_beats);
}
