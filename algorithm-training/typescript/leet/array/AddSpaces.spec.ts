import { addSpaces } from './AddSpaces';

describe('AddSpaces', () => {
    it('should return "a b c" for "abc", [1,2]', () => {
        expect(addSpaces('abc', [1, 2])).toBe('a b c');
    });
    it('should return " s p a c i n g" for "spacing", [0,1,2,3,4,5,6]', () => {
        expect(addSpaces('spacing', [0, 1, 2, 3, 4, 5, 6])).toBe(
            ' s p a c i n g'
        );
    });
});
