/* Determine whether arguments can be added without overflow */
int tadd_ok(int x, int y) {
    int sum = x + y,
    neg_over = (x < 0 && y < 0 && sum >= 0),
    pos_over = (x > 0 && y > 0 && sum < 0);
    return !neg_over && !pos_over;
}

