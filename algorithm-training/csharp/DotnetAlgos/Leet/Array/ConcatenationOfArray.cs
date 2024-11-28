/*
https://leetcode.com/problems/concatenation-of-array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Specifically, ans is the concatenation of two nums arrays.
Return the array ans.
*/

namespace DotnetAlgos.Leet.Array;

public class ConcatenationOfArray
{
    public int[] GetConcatenation(int[] nums)
    {
        int length = nums.Length;
        int[] ans = new int[length * 2];

        for (int i = 0; i < length; i++)
        {
            ans[i] = nums[i];
            ans[i + length] = nums[i];
        }

        return ans;
    }
}