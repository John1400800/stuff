#include <stdio.h>
#include <stdlib.h>

#define ARRAYLENGTH 4

int binary_search(int *arr, int search, int high) {
    int mid_v;
    int mid_i;
    int low = 0;
    while ((mid_v = arr[mid_i = (low + high) / 2]) != search && low <= high) {
        if (mid_v > search) {
            high = mid_i - 1;
        } else {
            low = mid_i + 1;
        }
    }
    if (mid_v == search) {
        return mid_i;
    }
    return -1;
}

int main(void) {
    int arr[ARRAYLENGTH] = {1, 3, 4, 6};

    int searched_index =                          // NOTE: on a separate line
          binary_search(arr, ARRAYLENGTH - 1, 3); //       for clarity
         
    printf("%d", searched_index);
}
