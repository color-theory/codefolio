/* https://leetcode.com/problems/valid-parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
 
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
*/

export const validateParens = (s: string) => {
    const openers = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    let opened = [];
    for (let i = 0; i < s.length; i++) {
        let nextChar = s[i];
        if (nextChar == '(' || nextChar == '{' || nextChar == '[') {
            opened.push(nextChar);
        } else if (nextChar == ')' || nextChar == '}' || nextChar == ']') {
            if (opened[opened.length - 1] == openers[nextChar]) {
                opened.pop();
            } else {
                return false;
            }
        } else {
            return false;
        }
    }

    return opened.length === 0;
};
