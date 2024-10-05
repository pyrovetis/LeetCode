/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function (obj) {
    if (obj === null) return;
    if (Array.isArray(obj)) return obj.filter(Boolean).map(compactObject);
    if (typeof obj !== 'object') return obj;

    const result = {};
    for (const key in obj) {
        const value = compactObject(obj[key]);
        if (value) result[key] = value;
    }
    return result;
};