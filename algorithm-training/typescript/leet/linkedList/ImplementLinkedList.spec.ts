import { MyLinkedList } from './ImplementLinkedList';

describe('MyLinkedList', () => {
    it('should return 0 when get(0) and addAtHead(0)', () => {
        const linkedList = new MyLinkedList();
        linkedList.addAtHead(0);
        expect(linkedList.get(0)).toEqual(0);
    });

    it('should return 1 when get(0) and addAtTail(1)', () => {
        const linkedList = new MyLinkedList();
        linkedList.addAtTail(1);
        expect(linkedList.get(0)).toEqual(1);
    });

    it('should return 2 when get(0) and addAtTail(1) and addAtTail(2)', () => {
        const linkedList = new MyLinkedList();
        linkedList.addAtTail(1);
        linkedList.addAtTail(2);
        expect(linkedList.get(0)).toEqual(1);
        expect(linkedList.get(1)).toEqual(2);
    });

    it('should return 1 when get(0) and addAtHead(1)', () => {
        const linkedList = new MyLinkedList();
        linkedList.addAtHead(1);
        expect(linkedList.get(0)).toEqual(1);
    });

    it('should return 1 when get(0) and addAtHead(1) and addAtHead(2)', () => {
        const linkedList = new MyLinkedList();
        linkedList.addAtHead(1);
        linkedList.addAtHead(2);
        expect(linkedList.get(0)).toEqual(2);
        expect(linkedList.get(1)).toEqual(1);
    });

    it('should return 1 when get(0) and addAtHead(1) and addAtHead(2) and addAtHead(3)', () => {
        const linkedList = new MyLinkedList();
        linkedList.addAtHead(1);
        linkedList.addAtHead(2);
        linkedList.addAtHead(3);
        expect(linkedList.get(0)).toEqual(3);
        expect(linkedList.get(1)).toEqual(2);
        expect(linkedList.get(2)).toEqual(1);
    });

    it('should return -1 when index is out of bounds', () => {
        const linkedList = new MyLinkedList();
        expect(linkedList.get(0)).toEqual(-1);
    });

    it('should return -1 when index is out of bounds', () => {
        const linkedList = new MyLinkedList();
        linkedList.addAtHead(1);
        expect(linkedList.get(1)).toEqual(-1);
    });
});
