import { firstBad } from './FirstBadVersion';

describe('firstBad', () => {
    it('should return the first bad version', () => {
        const isBadVersion = (version: number) => version >= 4;
        const n = 5;
        expect(firstBad(isBadVersion)(n)).toBe(4);
    });

    it('should return the first bad version', () => {
        const isBadVersion = (version: number) => version >= 1;
        const n = 1;
        expect(firstBad(isBadVersion)(n)).toBe(1);
    });

    it('should return the first bad version', () => {
        const isBadVersion = (version: number) => version >= 1;
        const n = 2;
        expect(firstBad(isBadVersion)(n)).toBe(1);
    });
});
