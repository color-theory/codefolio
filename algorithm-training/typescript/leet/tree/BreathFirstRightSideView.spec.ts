import { rightSideView } from './BreadthFirstRightSideView';
describe('rightSideView', () => {
    it('should return the correct right side view of the tree', () => {
        const tree = {
            val: 1,
            left: {
                val: 2,
                left: null,
                right: {
                    val: 5,
                    left: null,
                    right: null
                }
            },
            right: {
                val: 3,
                left: null,
                right: {
                    val: 4,
                    left: null,
                    right: null
                }
            }
        };
        const result = rightSideView(tree);
        const expected = [1, 3, 4];
        expect(result).toEqual(expected);
    });
});
