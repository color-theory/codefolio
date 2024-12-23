import { subsets } from './Subsets';
describe('Subsets', () => {
    it('should return the correct subsets', () => {
        const result = subsets([1, 2, 3]);
        const expected = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]];
        expect(result).toEqual(expected);
    });
    it('should return the correct subsets', () => {
        const result = subsets([0]);
        const expected = [[], [0]];
        expect(result).toEqual(expected);
    });
});
