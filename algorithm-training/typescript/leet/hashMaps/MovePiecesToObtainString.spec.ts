import { canChange } from './MovePiecesToObtainString';

describe('canChange', () => {
    it('should return true when valid', () => {
        expect(canChange('R__LR_R_L', '_RL__RRL_')).toEqual(true);
    });

    it('should return false when invalid', () => {
        expect(canChange('LR__R_R_L', '_RL__RRL_')).toEqual(false);
    });
});
