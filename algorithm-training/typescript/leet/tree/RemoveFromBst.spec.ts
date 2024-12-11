import { removeNode } from './RemoveFromBst';

describe('RemoveFromBst', () => {
    it('should return the root of the tree after the deletion', () => {
        const root = {
            val: 5,
            left: {
                val: 3,
                left: {
                    val: 2,
                    left: { val: 1, left: null, right: null },
                    right: null
                },
                right: { val: 4, left: null, right: null }
            },
            right: {
                val: 6,
                left: null,
                right: {
                    val: 7,
                    left: null,
                    right: null
                }
            }
        };
        const key = 3;
        const expected = {
            val: 5,
            left: {
                val: 4,
                left: {
                    val: 2,
                    left: { val: 1, left: null, right: null },
                    right: null
                },
                right: null
            },
            right: {
                val: 6,
                left: null,
                right: {
                    val: 7,
                    left: null,
                    right: null
                }
            }
        };
        expect(removeNode(root, key)).toEqual(expected);
    });
});
