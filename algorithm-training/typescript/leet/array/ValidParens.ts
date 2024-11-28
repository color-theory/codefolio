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
