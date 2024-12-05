import { sortColors } from './ColorSort';

describe('ColorSort', () => {
    it('should return [0,0,1,1,2,2] for [2,0,2,1,1,0]', () => {
        const colors = [2, 0, 2, 1, 1, 0];
        sortColors(colors);
        expect(colors).toStrictEqual([0, 0, 1, 1, 2, 2]);
    });

    it('should return [0,1,2] for [2,0,1]', () => {
        const colors = [2, 0, 1];
        sortColors(colors);
        expect(colors).toStrictEqual([0, 1, 2]);
    });

    it('should return [0,1,2] for [0,1,2]', () => {
        const colors = [0, 1, 2];
        sortColors(colors);
        expect(colors).toStrictEqual([0, 1, 2]);
    });

    it('should return [0,1,2] for [1,2,0]', () => {
        const colors = [1, 2, 0];
        sortColors(colors);
        expect(colors).toStrictEqual([0, 1, 2]);
    });

    it('should return [0,1,2] for [1,0,2]', () => {
        const colors = [1, 0, 2];
        sortColors(colors);
        expect(colors).toStrictEqual([0, 1, 2]);
    });

    it('should return [0,1,2] for [1,2,0]', () => {
        const colors = [1, 2, 0];
        sortColors(colors);
        expect(colors).toStrictEqual([0, 1, 2]);
    });

    it('should return [0,1,2] for [2,1,0]', () => {
        const colors = [2, 1, 0];
        sortColors(colors);
        expect(colors).toStrictEqual([0, 1, 2]);
    });

    it('should return [0,1,2] for [2,0,1]', () => {
        const colors = [2, 0, 1];
        sortColors(colors);
        expect(colors).toStrictEqual([0, 1, 2]);
    });
});
