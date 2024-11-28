import { removeDuplicates } from './RemoveDuplicatesFromSorted';

describe('RemoveDuplicatesFromSorted', () => {
    it('should return 5 when nums = [0,0,1,1,1,2,2,3,3,4]', () => {
        const nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
        const expected = 5;
        expect(removeDuplicates(nums)).toEqual(expected);
        expect(nums.slice(0, expected)).toEqual([0, 1, 2, 3, 4]);
    });

    it('should return 2 when nums = [1,1,2]', () => {
        const nums = [1, 1, 2];
        const expected = 2;
        expect(removeDuplicates(nums)).toEqual(expected);
        expect(nums.slice(0, expected)).toEqual([1, 2]);
    });
});
