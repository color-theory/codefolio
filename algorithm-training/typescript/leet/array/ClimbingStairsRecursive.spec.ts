import { climbStairs } from './ClimbingStairsRecursive';
describe('ClimbingStairsRecursive', () => {
    it('should return the correct number of ways to climb stairs', () => {
        expect(climbStairs(2)).toBe(2);
        expect(climbStairs(3)).toBe(3);
        expect(climbStairs(4)).toBe(5);
    });
});
