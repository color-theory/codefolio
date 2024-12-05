import { countStudents } from './HungryStudentsQueue';

describe('HungryStudentsQueue', () => {
    it('should return 0 for [1,1,0,0] and [0,1,0,1]', () => {
        expect(countStudents([1, 1, 0, 0], [0, 1, 0, 1])).toBe(0);
    });

    it('should return 3 for [1,1,1,0,0,1] and [1,0,0,0,1,1]', () => {
        expect(countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1])).toBe(3);
    });
});
