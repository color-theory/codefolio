class LinkedListNode {
    public value: number;
    public next: LinkedListNode | null;
    public prev: LinkedListNode | null;
    constructor(
        prev: LinkedListNode | null,
        next: LinkedListNode | null,
        value: number
    ) {
        this.value = value;
        this.prev = prev;
        this.next = next;
    }
}

export class MyLinkedList {
    public head: LinkedListNode | null;
    public tail: LinkedListNode | null;
    public size: number;
    constructor() {
        this.size = 0;
        this.head = null;
        this.tail = null;
    }

    get(index: number): number {
        if (index < 0 || index > this.size - 1) return -1;
        let curr = this.head;
        let i = 0;
        while (curr && i < index) {
            curr = curr.next;
            i++;
        }
        return curr ? curr.value : -1;
    }

    addAtHead(val: number): void {
        const newHead = new LinkedListNode(null, this.head ?? null, val);
        if (this.head) {
            this.head.prev = newHead;
        }
        if (this.size == 0) {
            this.tail = newHead;
        }
        this.head = newHead;

        this.size++;
    }

    addAtTail(val: number): void {
        const newTail = new LinkedListNode(this.tail ?? null, null, val);
        if (this.tail) {
            this.tail.next = newTail;
        }
        if (this.size == 0) {
            this.head = newTail;
        }

        this.tail = newTail;
        this.size++;
    }

    addAtIndex(index: number, val: number): void {
        if (index == this.size) {
            this.addAtTail(val);
            return;
        } else if (index == 0) {
            this.addAtHead(val);
            return;
        } else if (index < 0 || index > this.size) {
            return;
        }
        let curr = this.head;
        let i = 0;
        while (curr && i < index) {
            curr = curr.next;
            i++;
        }
        let newNode = new LinkedListNode(curr!.prev, curr, val);
        curr!.prev!.next = newNode;
        curr!.prev = newNode;
        this.size++;
    }

    deleteAtIndex(index: number): void {
        if (index < 0 || index >= this.size) return;
        let curr = this.head;
        let i = 0;
        while (curr && i < index) {
            curr = curr.next;
            i++;
        }
        if (!curr) return;
        if (curr.prev && curr.next) {
            curr.prev.next = curr.next;
            curr.next.prev = curr.prev;
        } else if (curr.prev && !curr.next) {
            curr.prev.next = null;
            this.tail = curr.prev;
        } else if (!curr.prev && curr.next) {
            curr.next.prev = null;
            this.head = curr.next;
        } else {
            this.head = null;
            this.tail = null;
        }
        this.size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * var obj = new MyLinkedList()
 * var param_1 = obj.get(index)
 * obj.addAtHead(val)
 * obj.addAtTail(val)
 * obj.addAtIndex(index,val)
 * obj.deleteAtIndex(index)
 */
