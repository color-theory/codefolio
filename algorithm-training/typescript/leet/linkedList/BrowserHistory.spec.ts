import { BrowserHistory } from './BrowserHistory';

describe('BrowserHistory', () => {
    it('should return leetcode.com when visit leetcode.com', () => {
        const browserHistory = new BrowserHistory('leetcode.com');
        browserHistory.visit('leetcode.com');
        expect(browserHistory.back(1)).toEqual('leetcode.com');
        expect(browserHistory.forward(1)).toEqual('leetcode.com');
    });

    it('should return google.com when visit google.com, visit facebook.com, visit youtube.com, back(1), back(1), forward(1), visit linkedin.com, forward(2), back(2)', () => {
        const browserHistory = new BrowserHistory('google.com');
        browserHistory.visit('google.com');
        browserHistory.visit('facebook.com');
        browserHistory.visit('youtube.com');
        expect(browserHistory.back(1)).toEqual('facebook.com');
        expect(browserHistory.back(1)).toEqual('google.com');
        expect(browserHistory.forward(1)).toEqual('facebook.com');
        browserHistory.visit('linkedin.com');
        expect(browserHistory.forward(2)).toEqual('linkedin.com');
        expect(browserHistory.back(2)).toEqual('google.com');
    });
});
