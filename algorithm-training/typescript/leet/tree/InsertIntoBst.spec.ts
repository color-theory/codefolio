import { insertIntoBST } from './InsertIntoBst';
describe('InsertIntoBst', () => {
    it('should return the root of the tree after the insertion', () => {
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
        const val = 5;
        const expected = {
            val: 4,
            left: {
                val: 2,
                left: { val: 1, left: null, right: null },
                right: { val: 3, left: null, right: null }
            },
            right: {
                val: 7,
                left: {
                    val: 5,
                    left: null,
                    right: null
                },
                right: null
            }
        };
        expect(insertIntoBST(root, val)).toEqual(expected);
    });
    it('should return the root of the tree after the insertion', () => {
        const root = null;
        const val = 5;
        const expected = {
            val: 5,
            left: null,
            right: null
        };
        expect(insertIntoBST(root, val)).toEqual(expected);
    });
});
