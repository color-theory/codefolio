export const binarySearch = (nums: number[], target: number): number => {
    if (nums.length == 1) {
        if (nums[0] == target) {
            return 0;
        } else {
            return -1;
        }
    }
    let L = 0;
    let R = nums.length - 1;
    let mid = 0;

    while (L <= R) {
        mid = Math.floor(R + L / 2);
        if (nums[mid] < target) {
            L = mid + 1;
        } else if (nums[mid] > target) {
            R = mid - 1;
        } else {
            return mid;
        }
    }
    return -1;
};
