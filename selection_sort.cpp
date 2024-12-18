#include <iostream>
using namespace std;
void selectionSort(int arr[], int n) {
     for (int i = 0; i < n - 1; i++) {
         int minIndex = i;
         for (int j = i + 1; j < n; j++) {
              if (arr[j] < arr[minIndex]) {
                  minIndex = j;
              }
         }
 
         int temp = arr[i];
         arr[i] = arr[minIndex];
         arr[minIndex] = temp;
              if (arr[j] < arr[minIndex]) {
                  minIndex = j;

 }

         if (minIndex !=i) {
             int temp = arr[i];
             arr[i] = arr[minIndex];
             arr[minIndex] = temp;
         }
     }
}

int main() {
    int arr[] = {64, 25, 15, 22, 11};
    int n = sizeof(arr) /sizeof(arr[0]);

    cout << "Original array:\n";
    for (int i = 0; i < n; i++)
         cout << arr[i] << " ";
    cout << endl;

    selectionSort(arr, n);

    cout << "Sorted array:\n";
    for (int i = 0; i < n; i++)
         cout << arr[i] << " ";
    cout << endl;

    return 0;
}