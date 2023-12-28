int atoi(char *num) {
    int res = 0;
    int i = 0;
    char minus = 0;
    if (num[i] == '-' || num[i] == '+') {
        if (num[i] == '-') {
            minus = 1;
        }
        ++i;
    }
    while (num[i] >= '0' && num[i] <= '9') {
        res = res * 10 + num[i] - '0';
        ++i;
    }
    return minus ? -res : res;
}

int main() {}