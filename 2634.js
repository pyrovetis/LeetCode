/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const result = [];

    for([index, item] of arr.entries()) {
        if(fn(item, index)) {result.push(item)}
    }

    return result;
};