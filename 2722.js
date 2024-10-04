/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
    const result = new Map();
    const mergedArray = arr1.concat(arr2);
    for (const item of mergedArray) {
        result.set(item.id, {...result.get(item.id), ...item});
    }
    return Array.from(result.values()).sort((a, b) => a.id - b.id);
};