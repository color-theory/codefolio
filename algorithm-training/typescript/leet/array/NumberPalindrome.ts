export function isPalindrome(x: number): boolean {
    const stringEquivalent = x.toString();
    let lIndex = 0;
    let rIndex = stringEquivalent.length - 1;

    while (lIndex < rIndex) {
        if (stringEquivalent[lIndex] !== stringEquivalent[rIndex]) return false;
        lIndex++;
        rIndex--;
    }
    return true;
}
