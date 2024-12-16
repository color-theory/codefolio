import { buildTree } from './ReconstructTree';

describe('ReconstructTree', () => {
    it('should return the correct tree', () => {
        const preorder = [3, 9, 20, 15, 7];
        const inorder = [9, 3, 15, 20, 7];
        const result = buildTree(preorder, inorder);
        const expected = {
            val: 3,
            left: { val: 9, left: null, right: null },
            right: {
                val: 20,
                left: { val: 15, left: null, right: null },
                right: { val: 7, left: null, right: null }
            }
        };
        expect(result).toEqual(expected);
    });
});
