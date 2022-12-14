#include <iostream>

int main()
{
	int b{ };
	std::cin >> b;

    std::cout << (5 * b - 400) << '\n';

    int diff { b - 100 };
    if (diff == 0)
        std::cout << "0" << '\n';
    else if (diff > 0)
        std::cout << "-1" << '\n';
    else
        std::cout << "1" << '\n';
	return 0;
}