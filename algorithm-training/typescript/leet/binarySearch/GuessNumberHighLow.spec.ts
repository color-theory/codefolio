import { guessNumber } from './GuessNumberHighLow';

describe('guessNumber', () => {
    it('should return the number that was picked', () => {
        const n = 10;
        const pick = 6;
        expect(guessNumber(n)).toBe(pick);
    });
});
