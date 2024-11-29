class Page {
    public url: string;
    public next: Page | null;
    public prev: Page | null;
    constructor(url: string) {
        this.url = url;
        this.prev = null;
        this.next = null;
    }
}

export class BrowserHistory {
    public homepage: string;
    public currentPage: Page;
    constructor(homepage: string) {
        this.homepage = homepage;
        this.currentPage = new Page(homepage);
    }

    visit(url: string): void {
        let curr = this.currentPage;
        this.currentPage.next = new Page(url);
        this.currentPage = this.currentPage.next;
        this.currentPage.prev = curr;
    }

    back(steps: number): string {
        let i = 0;
        while (this.currentPage.prev && i < steps) {
            this.currentPage = this.currentPage.prev;
            i++;
        }
        return this.currentPage.url;
    }

    forward(steps: number): string {
        let i = 0;
        while (this.currentPage.next && i < steps) {
            this.currentPage = this.currentPage.next;
            i++;
        }
        return this.currentPage.url;
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * var obj = new BrowserHistory(homepage)
 * obj.visit(url)
 * var param_2 = obj.back(steps)
 * var param_3 = obj.forward(steps)
 */
