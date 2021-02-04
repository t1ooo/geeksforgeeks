/**
 * @param {number} V
 * @param {number[][]} adj
 * @returns {number[]}
 */
class Solution_Recursive {
  dfsOfGraph(V, adj) {
    const ret = new Set();
    ret.add("0");
    this.traversal("0", adj, ret);
    return [...ret];
  }
  traversal(i, adj, ret) {
    for (let x of adj[i]) {
      if (ret.has(x)) {
        continue;
      }
      ret.add(x);
      this.traversal(x, adj, ret);
    }
  }
}

/**
 * @param {number} V
 * @param {number[][]} adj
 * @returns {number[]}
 */
class Solution_Stack {
  dfsOfGraph(V, adj) {
    const ret = new Set();
    ret.add("0");
    const stack = [];
    stack.push(...adj[0].slice().reverse());
    while (stack.length > 0) {
      const i = stack.pop();
      if (ret.has(i)) {
        continue;
      }
      ret.add(i);
      stack.push(...adj[i].slice().reverse());
    }
    return [...ret];
  }
}
