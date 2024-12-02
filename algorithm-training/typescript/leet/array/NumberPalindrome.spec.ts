import { isPalindrome } from './NumberPalindrome';

describe('NumberPalindrome', () => {
    it('should return true for 121', () => {
        expect(isPalindrome(121)).toBe(true);
    });

    it('should return false for -121', () => {
        expect(isPalindrome(-121)).toBe(false);
    });

    it('should return false for 10', () => {
        expect(isPalindrome(10)).toBe(false);
    });

    it('should return false for 123', () => {
        expect(isPalindrome(123)).toBe(false);
    });
});
