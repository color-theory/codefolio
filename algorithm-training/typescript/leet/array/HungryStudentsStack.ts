class StudentNode {
    public preference: number;
    public next: StudentNode | null;
    constructor(pref: number | undefined, next: StudentNode | null) {
        this.preference = pref ?? 0;
        this.next = next;
    }
}

export function countStudents(
    students: number[],
    sandwiches: number[]
): number {
    let head: StudentNode | null = null;
    let tail: StudentNode | null = null;
    let prevHead: StudentNode | null;
    let count = students.length;
    while (students.length > 0) {
        prevHead = head;
        head = new StudentNode(students.pop(), prevHead);
        if (!tail) {
            tail = head;
        }
    }

    let sandwichStack = [];
    while (sandwiches.length > 0) {
        sandwichStack.push(sandwiches.pop());
    }

    let prevCount;
    do {
        prevCount = count;
        for (let i = 0; i < prevCount; i++) {
            if (
                head &&
                head.preference == sandwichStack[sandwichStack.length - 1]
            ) {
                head = head.next;
                sandwichStack.pop();
                count--;
            } else {
                if (tail) {
                    tail.next = head;
                    tail = head;
                    head = head!.next;
                    tail!.next = null;
                }
            }
        }
    } while (prevCount > count);
    return count;
}
