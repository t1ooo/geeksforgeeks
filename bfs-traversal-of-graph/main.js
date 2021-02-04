/**
 * @param {number} V
 * @param {number[][]} adj
 * @returns {number[]}
 */
class Solution {
  bfsOfGraph(V, adj) {
    const ret = new Set();
    const queue = [0];
    ret.add(0);
    while (queue.length > 0) {
      const i = queue.shift();
      for (let x of adj[i]) {
        if (ret.has(x)) {
          continue;
        }
        ret.add(x);
        queue.push(x);
      }
    }
    return [...ret];
  }
}
