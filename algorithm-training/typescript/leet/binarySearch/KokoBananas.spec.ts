import { minEatingSpeed } from './KokoBananas';

describe('KokoBananas', () => {
    it('should return the minimum integer k such that she can eat all the bananas within h hours', () => {
        expect(minEatingSpeed([3, 6, 7, 11], 8)).toBe(4);
        expect(minEatingSpeed([30, 11, 23, 4, 20], 5)).toBe(30);
        expect(minEatingSpeed([30, 11, 23, 4, 20], 6)).toBe(23);
    });
});
