#include <iostream>
#include <vector>


int partion(std::vector<int>& vec, int low, int high) {
	int pivot = vec[high];

	int i = low - 1;

	for (int j = low; j <= high - 1; ++j) {
		if (vec[j] <= pivot) {
			i++;
			std::swap(vec[i], vec[j]);
		}
	}

	std::swap(vec[i + 1], vec[high]);

	return i + 1;
}

void quick_sort(std::vector<int>& vec, int low, int high) {
	if (low < high) {
		int pi = partion(vec, low, high);

		quick_sort(vec, low, pi - 1);
		quick_sort(vec, pi + 1, high);
	}
}

int main() {
	srand(time(0));
	std::vector<int> vec = { 3, 1, 4, 2, 3 };

	quick_sort(vec, 0, vec.size() - 1);
	return 0;
}