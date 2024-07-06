import { test, expect } from "@jest/globals";
import { getURLsFromHTML, normalizeURL } from "./crawl.js";

test('normalizeURL should remove protocol and trailing slash', () => {
    const testCases = [
        { input: 'https://blog.boot.dev/path/', expected: 'blog.boot.dev/path' },
        { input: 'https://blog.boot.dev/path/', expected: 'blog.boot.dev/path'},
        { input: 'http://blog.boot.dev/path/', expected: 'blog.boot.dev/path'},
        { input: 'http://blog.boot.dev/path?query=123', expected: 'blog.boot.dev/path'},
        { input: 'http://blog.boot.dev/path#fragment', expected: 'blog.boot.dev/path'}
    ];

    testCases.forEach(({ input, expected }) => {
        expect(normalizeURL(input)).toBe(expected);
    });
});

test('getURLsFromHTML should return a list of all link URLs', () => {
    const testCases = [
        {   inputURL: 'https://blog.boot.dev',
            inputBody: '<html><body><a href="https://blog.boot.dev"><span>Go to Boot.dev</span></a></body></html>',
            expected: ['https://blog.boot.dev/']
        },
        {   inputURL: 'https://blog.boot.dev',
            inputBody: '<html><body><a href="path/one"><span>Boot.dev></span></a></body></html>',
            expected: [ 'https://blog.boot.dev/path/one' ]
        },
        {
            inputBody: '<html><body><a href="https://example.com"><span>External</span></a></body></html>',
            inputURL: 'https://blog.boot.dev',
            expected: ['https://example.com/']
        },
        {
            inputBody: `
                <html>
                    <body>
                        <a href="/path1"><span>Link 1</span></a>
                        <a href="https://blog.boot.dev/path2"><span>Link 2</span></a>
                        <a href="https://example.com/path3"><span>Link 3</span></a>
                        <a href="/path4"><span>Link 4</span></a>
                    </body>
                </html>`,
            inputURL: 'https://blog.boot.dev',
            expected: [
                'https://blog.boot.dev/path1',
                'https://blog.boot.dev/path2',
                'https://example.com/path3',
                'https://blog.boot.dev/path4'
            ]
        }
    ];

    testCases.forEach(({ inputURL, inputBody, expected }) => {
        const actual = getURLsFromHTML(inputBody, inputURL);
        expect(actual).toStrictEqual(expected);
    });
});
