import { kthSmallest } from './KthSmallestValue';
describe('KthSmallestValue', () => {
    it('should return the kth smallest value in the tree', () => {
        const root = {
            val: 3,
            left: {
                val: 1,
                left: null,
                right: {
                    val: 2,
                    left: null,
                    right: null
                }
            },
            right: {
                val: 4,
                left: null,
                right: null
            }
        };
        const k = 1;
        const expected = 1;
        expect(kthSmallest(root, k)).toEqual(expected);
    });
});
