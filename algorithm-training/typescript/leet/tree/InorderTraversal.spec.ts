import { inorderTraversal } from './InorderTraversal';

describe('InorderTraversal', () => {
    it('should return the inorder traversal of the tree', () => {
        const root = {
            val: 1,
            left: null,
            right: {
                val: 2,
                left: { val: 3, left: null, right: null },
                right: null
            }
        };
        const expected = [1, 3, 2];
        expect(inorderTraversal(root)).toEqual(expected);
    });
});
