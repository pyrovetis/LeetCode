/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const result = [];

    for ([index, item] of arr.entries()) {
        result.push(fn(item, index));
    }

    return result;
};