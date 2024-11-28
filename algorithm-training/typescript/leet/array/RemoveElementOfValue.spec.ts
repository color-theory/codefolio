import { removeElement } from './RemoveElementOfValue';

describe('RemoveElementOfValue', () => {
    it('should return 5 when nums = [0,0,1,1,1,2,2,3,3,4] and val = 1', () => {
        const nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
        const val = 1;
        const expected = 7;
        expect(removeElement(nums, val)).toEqual(expected);
        expect(nums.slice(0, expected)).toEqual([0, 0, 2, 2, 3, 3, 4]);
    });

    it('should return 2 when nums = [1,1,2] and val = 2', () => {
        const nums = [1, 1, 2];
        const val = 2;
        const expected = 2;
        expect(removeElement(nums, val)).toEqual(expected);
        expect(nums.slice(0, expected)).toEqual([1, 1]);
    });
});
