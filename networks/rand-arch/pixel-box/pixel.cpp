#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

const int COLOR_RANGE = 256;
const int COLOR_COUNT = pow(COLOR_RANGE, 3);

class Pixel
{
  public:
    Pixel() {}
    Pixel(int id)
    {
        red = (id / (int)pow(COLOR_RANGE, 2)) % COLOR_RANGE;
        green = (id / (int)pow(COLOR_RANGE, 1)) % COLOR_RANGE;
        blue = (id / (int)pow(COLOR_RANGE, 0)) % COLOR_RANGE;

        this->id = id;
    }
    Pixel(int r, int g, int b)
    {
        red = r;
        green = g;
        blue = b;

        id = red << 16 | green << 8 | blue;
    }

    int red;
    int green;
    int blue;
    int id;

    Pixel operator-(Pixel pixel)
    {
        return Pixel(red - pixel.red, green - pixel.green, blue - pixel.blue);
    }

    double l2Norm()
    {
        return sqrt(pow(red, 2) + pow(green, 2) + pow(blue, 2));
    }

    double distanceTo(Pixel pixel)
    {
        return (*this - pixel).l2Norm();
    }

    friend ostream &operator<<(ostream &stream, Pixel &obj)
    {
        return stream << setfill('0') << setw(6) << hex << obj.id;
    }
};

int main(int numArgs, char *args[])
{
    int step, newColorSpaceSize;

    if (numArgs < 2)
        step = 1;
    else if (numArgs != 2)
        cout << "Pass number indicating the number of colors" << endl;
    else
        step = COLOR_COUNT / (newColorSpaceSize = stoi(args[1]));

    ofstream newColors("/Users/tru/Workspace/surrep/production/data/colorBins" + to_string(newColorSpaceSize) + ".txt");

    Pixel colorSpace[newColorSpaceSize];


    for (int i = 0; i < newColorSpaceSize; i++)
      colorSpace[i] = Pixel(i * step);

    for (int i = 0; i < COLOR_COUNT; i++)
    {
        Pixel pixel = Pixel(i);
        int min_distance = INT32_MAX;
        int group = 0;

        for (int c = 0; c < newColorSpaceSize; c++)
        {
            int distance = pixel.distanceTo(colorSpace[c]);
            if (distance < min_distance)
            {
                group = c;
                min_distance = distance;
            }
        }

        newColors << group << '\n';
    }

    return 0;
}
