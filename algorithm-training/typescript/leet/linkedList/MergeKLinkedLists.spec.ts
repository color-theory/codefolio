import { mergeKLists } from './MergeKLinkedLists';
describe('mergeKLists', () => {
    it('should return the correct merged linked list', () => {
        const lists = [
            {
                val: 1,
                next: {
                    val: 4,
                    next: {
                        val: 5,
                        next: null
                    }
                }
            },
            {
                val: 1,
                next: {
                    val: 3,
                    next: {
                        val: 4,
                        next: null
                    }
                }
            },
            {
                val: 2,
                next: {
                    val: 6,
                    next: null
                }
            }
        ];
        const result = mergeKLists(lists);
        const expected = {
            val: 1,
            next: {
                val: 1,
                next: {
                    val: 2,
                    next: {
                        val: 3,
                        next: {
                            val: 4,
                            next: {
                                val: 4,
                                next: {
                                    val: 5,
                                    next: {
                                        val: 6,
                                        next: null
                                    }
                                }
                            }
                        }
                    }
                }
            }
        };
        expect(result).toEqual(expected);
    });
    it('should return an empty linked list', () => {
        const result = mergeKLists([]);
        expect(result).toBeNull();
    });
});
