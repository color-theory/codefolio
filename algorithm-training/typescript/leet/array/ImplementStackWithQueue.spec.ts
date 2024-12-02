import { MyStack } from './ImplementStackWithQueue';

describe('ImplementStackWithQueue', function () {
    it('should work for case 1', function () {
        const stack = new MyStack();
        stack.push(1);
        stack.push(2);
        expect(stack.top()).toBe(2);
        expect(stack.pop()).toBe(2);
        expect(stack.empty()).toBe(false);
    });
    it('should work for case 2', function () {
        const stack = new MyStack();
        stack.push(1);
        stack.push(2);
        stack.pop();
        stack.push(3);
        expect(stack.top()).toBe(3);
        expect(stack.pop()).toBe(3);
        expect(stack.empty()).toBe(false);
    });
    it('should work for case 3', function () {
        const stack = new MyStack();
        stack.push(1);
        stack.push(2);
        stack.pop();
        stack.pop();
        expect(stack.empty()).toBe(true);
    });
});
