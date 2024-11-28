import { getConcatenation } from './ConcatenationOfArray';

describe('getConcatenation', () => {
    it('should return [1,2,1,1,2,1] when nums = [1,2,1]', () => {
        const nums = [1, 2, 1];
        const expected = [1, 2, 1, 1, 2, 1];
        expect(getConcatenation(nums)).toEqual(expected);
    });

    it('should return [1,3,2,1,1,3,2,1] when nums = [1,3,2]', () => {
        const nums = [1, 3, 2];
        const expected = [1, 3, 2, 1, 3, 2];
        expect(getConcatenation(nums)).toEqual(expected);
    });
});
