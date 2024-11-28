import { mergeLinkedListThirdList } from './MergeLinkedListThirdList';

describe('MergeLinkedListThirdList', () => {
    it('should return [1,1,2,3,4,4] when l1 = [1,2,4], l2 = [1,3,4]', () => {
        const l1 = { val: 1, next: { val: 2, next: { val: 4, next: null } } };
        const l2 = { val: 1, next: { val: 3, next: { val: 4, next: null } } };
        const expected = {
            val: 1,
            next: {
                val: 1,
                next: {
                    val: 2,
                    next: {
                        val: 3,
                        next: { val: 4, next: { val: 4, next: null } }
                    }
                }
            }
        };
        expect(mergeLinkedListThirdList(l1, l2)).toEqual(expected);
    });

    it('should return [1,2,3] when l1 = [1,2,3], l2 = []', () => {
        const l1 = { val: 1, next: { val: 2, next: { val: 3, next: null } } };
        const l2 = null;
        const expected = {
            val: 1,
            next: { val: 2, next: { val: 3, next: null } }
        };
        expect(mergeLinkedListThirdList(l1, l2)).toEqual(expected);
    });

    it('should return [1,2,3] when l1 = [], l2 = [1,2,3]', () => {
        const l1 = null;
        const l2 = { val: 1, next: { val: 2, next: { val: 3, next: null } } };
        const expected = {
            val: 1,
            next: { val: 2, next: { val: 3, next: null } }
        };
        expect(mergeLinkedListThirdList(l1, l2)).toEqual(expected);
    });

    it('should return [] when l1 = [], l2 = []', () => {
        const l1 = null;
        const l2 = null;
        const expected = null;
        expect(mergeLinkedListThirdList(l1, l2)).toEqual(expected);
    });
});
