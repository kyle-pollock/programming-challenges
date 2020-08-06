#include <stdio.h>

#define NMAX 13
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

int count;

void backtrack(int a[], int k, int n, int tallest, int p, int r, int left_most, int right_most) {
  if (p < 0 || r < 0) { return; }
  if (k == n) { count++; return; }

  int low = MAX((p-1),(0));
  int high = MIN((n - r + 1),(n));

  int i;
  for (i = low; i < high; i++) {
    if (a[i] != 0) {
      continue;
    }
    a[i] = tallest;
    if (tallest == n) {
      backtrack(a, k + 1, n, tallest - 1, p - 1, r - 1, i, i);
    }
    else if (i < left_most) {
      backtrack(a, k + 1, n, tallest - 1, p - 1, r, i, right_most);
    }
    else if (i > right_most) {
      backtrack(a, k + 1, n, tallest - 1, p, r - 1, left_most, i);
    }
    else {
      backtrack(a, k + 1, n, tallest - 1, p, r, left_most, right_most);
    }
    a[i] = 0;
  }
}

/*
 Not sure if backtracking is the best way to go about this problem. This
 C implementation is significantly faster than my python solution however
 the UVa judge will say this is too slow and I am out of ideas on how I
 can prune it further.  So I used this program to pre-compute the hard
 n=13 instances and that passed.
 */
int main() {
  int cases, n, p, r, i, j;
  int a[NMAX];

  scanf("%d", &cases);
  for (i = 0; i < cases; i++) {
    scanf("%d %d %d", &n, &p, &r);

    if (p == 0 || r == 0) {
      printf("%d\n", 0);
      continue;
    }

    for (j=0; j<n; j++) { a[j] = 0; }
    count = 0;
    backtrack(a, 0, n, n, p, r, -1, -1);
    printf("%d\n", count);
  }

  return 0;
}
