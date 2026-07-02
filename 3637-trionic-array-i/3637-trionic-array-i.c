#include <stdbool.h>

bool isTrionic(int* nums, int numsSize) {
    // A trionic array must have at least 4 elements to satisfy 0 < p < q < n - 1
    if (numsSize < 4) {
        return false;
    }
    
    int p = 0;
    
    // Step 1: Find the end of the strictly increasing section
    while (p < numsSize - 1 && nums[p] < nums[p + 1]) {
        p++;
    }
    
    // If p hasn't moved, there is no initial increasing section
    if (p == 0) {
        return false;
    }
    
    // Step 2: Find the end of the strictly decreasing section
    int q = p;
    while (q < numsSize - 1 && nums[q] > nums[q + 1]) {
        q++;
    }
    
    // If q hasn't moved from p, there is no decreasing section.
    // If q reached the end, there is no final increasing section.
    if (q == p || q == numsSize - 1) {
        return false;
    }
    
    // Step 3: Verify the final strictly increasing section
    while (q < numsSize - 1 && nums[q] < nums[q + 1]) {
        q++;
    }
    
    // Step 4: Final validation - did we reach the exact end of the array?
    return q == numsSize - 1;
}