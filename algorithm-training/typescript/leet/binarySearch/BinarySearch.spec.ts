import { binarySearch } from './BinarySearch';

describe('binarySearch', () => {
    it('should return 4', () => {
        expect(binarySearch([-1, 0, 3, 5, 9, 12], 9)).toBe(4);
    });

    it('should return -1', () => {
        expect(binarySearch([-1, 0, 3, 5, 9, 12], 2)).toBe(-1);
    });
});
