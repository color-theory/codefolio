/**
 * https://leetcode.com/problems/first-bad-version
 * 
 * You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:
Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

/**
 * The knows API is defined in the parent class Relation.
 * isBadVersion(version: number): boolean {
 *     ...
 * };
 */

export const firstBad = (isBadVersion: any) => {
    return function (n: number): number {
        let left = 1;
        let right = n;
        let bad = 0;
        while (left <= right) {
            let ver = Math.floor((left + right) / 2);
            if (!isBadVersion(ver)) {
                left = ver + 1;
            } else {
                bad = ver;
                right = ver - 1;
            }
        }
        return bad;
    };
};

// The following code can break out of the loop when the first bad version is found, so the best case scenario is faster than the above solution,
// but the worst case scenario is slower. The above solution is more consistent.

// export const firstBad = (isBadVersion: any) => {

//     return function(n: number): number {
//         let left = 1;
//         let right = n;
//         while (left <= right){
//             let ver = Math.floor((left + right) / 2)
//             if(isBadVersion(ver)){
//                 if(!isBadVersion(ver - 1)){
//                     return ver;
//                 }else{
//                     right = ver - 1;
//                 }
//             }else{
//                 left = ver + 1;
//             }
//         }
//     };
// };
