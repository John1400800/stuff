unsigned str_len(const char *s) {
    unsigned i = 0;
    while (s[i] != '\0') {
        ++i;
    }
    return i;
}
