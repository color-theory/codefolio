import { searchMatrix } from './SearchMatrix';

describe('searchMatrix', () => {
    it('should return true if the target is in the matrix', () => {
        const matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ];
        const target = 3;
        expect(searchMatrix(matrix, target)).toBe(true);
    });

    it('should return false if the target is not in the matrix', () => {
        const matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ];
        const target = 13;
        expect(searchMatrix(matrix, target)).toBe(false);
    });

    it('should return false if the matrix is empty', () => {
        const matrix: number[][] = [];
        const target = 0;
        expect(searchMatrix(matrix, target)).toBe(false);
    });

    it('should return false if the target is less than the first element', () => {
        const matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ];
        const target = 0;
        expect(searchMatrix(matrix, target)).toBe(false);
    });

    it('should return false if the target is greater than the last element', () => {
        const matrix = [[1, 3]];
        const target = 100;
        expect(searchMatrix(matrix, target)).toBe(false);
    });
});
