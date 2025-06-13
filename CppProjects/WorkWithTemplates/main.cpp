#include <iostream>
#include <vector>

template <typename T>
const T& Max(const T& x, const T& y) {
    if (x < y) return y;

    return x;
}

template <typename T>
const std::vector<T>& Max(const std::vector<T>& v1, const std::vector<T>& v2) {
    if (v1.size() > v2.size()) return v1;
    if (v1.size() < v2.size()) return v2;
    if (v1 > v2) return v1;
    return v2;
}

struct Point {
    double x {};
    double y {};
    double z {};

    const bool operator<(const Point& rhs) const {
        if (x != rhs.x) return x < rhs.x;
        if (y != rhs.y) return y < rhs.y;
        return z < rhs.z;
    }
};

int main() {
    constexpr Point p1 {0, 0, 1}, p2;
    const Point p = Max(p1, p2);
    std::cout << p.x << " " << p.y << ' ' << p.z << '\n';

    std::cout << Max<double>(3.14, 2);
    return 0;
}