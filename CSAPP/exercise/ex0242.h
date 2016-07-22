int div16 (int x) {
    int k = 4,
        fk = (x >> 31) & 0xf;
    return (x + fk) >> k;
}
