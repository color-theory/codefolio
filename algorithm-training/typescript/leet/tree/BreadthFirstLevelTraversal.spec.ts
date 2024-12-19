import { levelOrder } from './BreadthFirstLevelTraversal';

describe('BreadthFirstLevelTraversal', () => {
    it('should return the correct level order traversal', () => {
        const tree = {
            val: 3,
            left: { val: 9, left: null, right: null },
            right: {
                val: 20,
                left: { val: 15, left: null, right: null },
                right: { val: 7, left: null, right: null }
            }
        };
        const result = levelOrder(tree);
        const expected = [[3], [9, 20], [15, 7]];
        expect(result).toEqual(expected);
    });
});
