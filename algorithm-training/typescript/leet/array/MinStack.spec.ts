import { MinStack } from './MinStack';

describe('MinStack', () => {
    it('should return 0 when push(0) and getMin()', () => {
        const stack = new MinStack();
        stack.push(0);
        expect(stack.getMin()).toEqual(0);
    });

    it('should return 0 when push(0), push(1), push(0) and getMin()', () => {
        const stack = new MinStack();
        stack.push(0);
        stack.push(1);
        stack.push(0);
        expect(stack.getMin()).toEqual(0);
    });

    it('should return -2 when push(-2), push(0), push(-3), getMin(), pop(), top(), getMin()', () => {
        const stack = new MinStack();
        stack.push(-2);
        stack.push(0);
        stack.push(-3);
        expect(stack.getMin()).toEqual(-3);
        stack.pop();
        expect(stack.top()).toEqual(0);
        expect(stack.getMin()).toEqual(-2);
    });
});
