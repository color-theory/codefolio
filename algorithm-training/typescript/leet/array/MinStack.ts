/*
https://leetcode.com/problems/min-stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
*/

export class MinStack {
    public stack: number[] = [];
    public mins: number[] = [];

    constructor() {}

    push(val: number): void {
        if (this.mins.length == 0 || val <= this.mins[this.mins.length - 1]) {
            this.mins.push(val);
        }
        this.stack.push(val);
    }

    pop(): void {
        const removed = this.stack.pop();
        if (removed == this.mins[this.mins.length - 1]) {
            this.mins.pop();
        }
    }

    top(): number {
        return this.stack[this.stack.length - 1];
    }

    getMin(): number {
        return this.mins[this.mins.length - 1];
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
