import { reverseListIterative } from './ReverseLinkedListIterative';

describe('ReverseLinkedListIterative', () => {
    it('should return null when head is null', () => {
        const head = null;
        const expected = null;
        const actual = reverseListIterative(head);
        expect(actual).toEqual(expected);
    });

    it('should return [5,4,3,2,1] when head is [1,2,3,4,5]', () => {
        const head = {
            val: 1,
            next: {
                val: 2,
                next: {
                    val: 3,
                    next: {
                        val: 4,
                        next: {
                            val: 5,
                            next: null
                        }
                    }
                }
            }
        };
        const expected = {
            val: 5,
            next: {
                val: 4,
                next: {
                    val: 3,
                    next: {
                        val: 2,
                        next: {
                            val: 1,
                            next: null
                        }
                    }
                }
            }
        };
        const actual = reverseListIterative(head);
        expect(actual).toEqual(expected);
    });

    it('should return [2,1] when head is [1,2]', () => {
        const head = {
            val: 1,
            next: {
                val: 2,
                next: null
            }
        };
        const expected = {
            val: 2,
            next: {
                val: 1,
                next: null
            }
        };
        const actual = reverseListIterative(head);
        expect(actual).toEqual(expected);
    });

    it('should return [] when head is []', () => {
        const head = null;
        const expected = null;
        const actual = reverseListIterative(head);
        expect(actual).toEqual(expected);
    });
});
