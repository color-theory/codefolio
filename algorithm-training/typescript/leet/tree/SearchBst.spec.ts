import { searchBST } from './SearchBst';

describe('SearchBst', () => {
    it('should return the subtree of the tree whose root node value is equal to the target', () => {
        const root = {
            val: 4,
            left: {
                val: 2,
                left: { val: 1, left: null, right: null },
                right: { val: 3, left: null, right: null }
            },
            right: {
                val: 7,
                left: null,
                right: null
            }
        };
        const target = 2;
        const expected = {
            val: 2,
            left: { val: 1, left: null, right: null },
            right: { val: 3, left: null, right: null }
        };
        expect(searchBST(root, target)).toEqual(expected);
    });

    it('should return null if the target is not in the tree', () => {
        const root = {
            val: 4,
            left: {
                val: 2,
                left: { val: 1, left: null, right: null },
                right: { val: 3, left: null, right: null }
            },
            right: {
                val: 7,
                left: null,
                right: null
            }
        };
        const target = 5;
        expect(searchBST(root, target)).toBeNull();
    });

    it('should return null if the tree is empty', () => {
        const root = null;
        const target = 0;
        expect(searchBST(root, target)).toBeNull();
    });
});
