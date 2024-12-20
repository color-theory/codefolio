import { hasPathSum } from './PathSumHasValue';
describe('PathSumHasValue', () => {
    it('should return true if the tree has a path sum equal to the target value', () => {
        const tree = {
            val: 5,
            left: {
                val: 4,
                left: {
                    val: 11,
                    left: { val: 7, left: null, right: null },
                    right: { val: 2, left: null, right: null }
                },
                right: null
            },
            right: {
                val: 8,
                left: { val: 13, left: null, right: null },
                right: {
                    val: 4,
                    left: null,
                    right: { val: 1, left: null, right: null }
                }
            }
        };
        const result = hasPathSum(tree, 22);
        expect(result).toBe(true);
    });
    it('should return false if the tree does not have a path sum equal to the target value', () => {
        const tree = {
            val: 1,
            left: {
                val: 2,
                left: null,
                right: null
            },
            right: null
        };
        const result = hasPathSum(tree, 1);
        expect(result).toBe(false);
    });
});
