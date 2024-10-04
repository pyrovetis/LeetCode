/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function (fn) {
    const result = new Map();
    for (let item of this) {
        const key = fn(item);
        if (!result.has(key)) result.set(key, []);
        result.get(key).push(item);
    }
    return Object.fromEntries(result);
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */