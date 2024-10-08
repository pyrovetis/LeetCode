/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function (functions) {
    return new Promise((resolve, reject) => {
        let results = [];
        let completed = 0;
        for (const [index, item] of functions.entries()) {
            item().then(result => {
                results[index] = result;
                completed++;
                if (completed === functions.length) resolve(results);
            }).catch(reject);
        }
    });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */