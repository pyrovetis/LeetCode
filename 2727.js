/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function (obj) {
    for (const item in obj) {
        return false;
    }
    return true;
};