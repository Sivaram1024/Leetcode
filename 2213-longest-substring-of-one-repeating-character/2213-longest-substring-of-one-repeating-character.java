class Solution {

    class Node {
        char l, r;
        int len, pre, suf, best;

        Node(char l, char r, int len, int pre, int suf, int best) {
            this.l = l;
            this.r = r;
            this.len = len;
            this.pre = pre;
            this.suf = suf;
            this.best = best;
        }
    }

    Node[] tree;

    public int[] longestRepeating(String s, String queryCharacters,
                                  int[] queryIndices) {

        int n = s.length();
        tree = new Node[4 * n];

        build(s, 1, 0, n - 1);

        int[] ans = new int[queryIndices.length];

        for (int i = 0; i < queryIndices.length; i++) {

            update(1, 0, n - 1,
                   queryIndices[i],
                   queryCharacters.charAt(i));

            ans[i] = tree[1].best;
        }

        return ans;
    }

    void build(String s, int node, int l, int r) {

        if (l == r) {
            char c = s.charAt(l);
            tree[node] = new Node(c, c, 1, 1, 1, 1);
            return;
        }

        int mid = (l + r) / 2;

        build(s, node * 2, l, mid);
        build(s, node * 2 + 1, mid + 1, r);

        tree[node] = merge(tree[node * 2],
                           tree[node * 2 + 1]);
    }

    void update(int node, int l, int r, int index, char c) {

        if (l == r) {
            tree[node] = new Node(c, c, 1, 1, 1, 1);
            return;
        }

        int mid = (l + r) / 2;

        if (index <= mid)
            update(node * 2, l, mid, index, c);
        else
            update(node * 2 + 1, mid + 1, r, index, c);

        tree[node] = merge(tree[node * 2],
                           tree[node * 2 + 1]);
    }

    Node merge(Node a, Node b) {

        int len = a.len + b.len;
        int pre = a.pre;
        int suf = b.suf;
        int best = Math.max(a.best, b.best);

        if (a.r == b.l) {

            best = Math.max(best, a.suf + b.pre);

            // Entire left segment is same character
            if (a.pre == a.len)
                pre = a.len + b.pre;

            // Entire right segment is same character
            if (b.suf == b.len)
                suf = a.suf + b.len;
        }

        return new Node(
            a.l,
            b.r,
            len,
            pre,
            suf,
            best
        );
    }
}