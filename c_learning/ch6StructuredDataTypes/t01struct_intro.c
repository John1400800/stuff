#include <math.h>
#include <stdio.h>

#define abs(n) ((n) < 0 ? -(n) : (n))
#define min(a, b) ((a) > (b) ? (a) : (b))
#define max(a, b) ((a) < (b) ? (a) : (b))
#define rect_area(rct)                                                         \
    ((abs((rct).pt1.x - (rct).pt2.x) * abs((rct).pt1.y - (rct).pt2.y)))
#define ptrinrect(pt, rct)                                                     \
    ((pt).x >= (rct).pt1.x && (pt).x < (rct).pt2.x &&                          \
     (pt).y >= (rct).pt1.y && (pt).y < (rct).pt2.y)
     

#ifdef _INC_STDIO
#define print_point(pt) printf("x=%d, y=%d\n", (pt).x, (pt).y)
#define print_rect(rct)                                                        \
    printf("x1=%d, y1=%d, x2=%d, y2=%d\n", (rct).pt1.x, (rct).pt1.y,           \
           (rct).pt2.x, (rct).pt2.y)
#endif

#ifdef _INC_MATH
#define dist_point(pt) sqrt((double)((pt).x * (pt).x + (pt).y * (pt).y))
#endif

struct point {
    int x;
    int y;
};

struct rect {
    struct point pt1;
    struct point pt2;
};

struct point makepoint(int x, int y) {
    struct point temp;
    temp.x = x;
    temp.y = y;
    return temp;
}

struct point addpoint(struct point p1, struct point p2) {
    p1.x += p2.x;
    p1.y += p2.y;
    return p1;
}

struct rect canonicrect(struct rect r) {
    struct rect temp;
    temp.pt1.x = min(r.pt1.x, r.pt2.x);
    temp.pt1.y = min(r.pt1.y, r.pt2.y);
    temp.pt2.x = max(r.pt1.x, r.pt2.x);
    temp.pt2.y = max(r.pt1.y, r.pt2.y);
    return temp;
}

int main(void) {
    struct point pt_lb = {-10, -10};
    struct point pt_rt = {10, 10};
    print_point(pt_lb);
    printf("%f\n", dist_point(pt_lb));

    // also init as
    // struct rect rct = {{x1, y1}, {x2, y2}}; // :)
    struct rect screen = {pt_lb, pt_rt};
    print_rect(screen);
    printf("%d", rect_area(screen));
}
