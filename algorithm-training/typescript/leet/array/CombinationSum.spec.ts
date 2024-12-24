import { combinationSum } from './CombinationSum';
describe('CombinationSum', () => {
    it('should return the correct combinations', () => {
        const result = combinationSum([2, 3, 6, 7], 7);
        const expected = [[2, 2, 3], [7]];
        expect(result).toEqual(expected);
    });
    it('should return the correct combinations', () => {
        const result = combinationSum([2, 3, 5], 8);
        const expected = [
            [2, 2, 2, 2],
            [2, 3, 3],
            [3, 5]
        ];
        expect(result).toEqual(expected);
    });
    it('should return the correct combinations', () => {
        const result = combinationSum([2], 1);
        const expected: any = [];
        expect(result).toEqual(expected);
    });
});
