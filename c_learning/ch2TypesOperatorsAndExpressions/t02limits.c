#define CHAR_MIN -(1 << (sizeof(char) * 8 - 1))
#define CHAR_MAX (1 << (sizeof(char) * 8 - 1)) - 1
#define UCHAR_MAX 2 * MAX_CHAR + 1
#define INT_MIN -(1 << (sizeof(int) * 8 - 1))
#define INT_MAX (1ll << (sizeof(int) * 8 - 1)) - 1
#define UINT_MAX 2 * INT_MAX
