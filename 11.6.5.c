#include <stdio.h>
#include <string.h>
#include <limits.h>

#define MAXCUTS 50

int memo[MAXCUTS+1][MAXCUTS+1];
int cuts[MAXCUTS+1];

int min_cost(int L, int R, int i, int j) {
  if (memo[i][j] != -1) {
    return memo[i][j];
  }
  if (i == j) {
    memo[i][j] = 0;
    return 0;
  }

  int min = INT_MAX;
  int k, cost;

  for (k = i; k < j; k++) {
    cost = (R - L) + min_cost(L, cuts[k], i, k) + min_cost(cuts[k], R, k + 1, j);
    if (cost < min) {
      min = cost;
    }
  }

  memo[i][j] = min;
  return min;
}

int main() {
  int stick_length, num_cuts, i, j;

  while((scanf("%d", &stick_length) != EOF) && stick_length != 0) {
    scanf("%d", &num_cuts);
    for (i = 0; i < num_cuts; i++){
      scanf("%d", &cuts[i]);
    }
    for (i = 0; i < MAXCUTS; i++) {
      for (j = 0; j < MAXCUTS; j++) {
        memo[i][j] = -1;
      }
    }
    printf("The minimum cutting is %d.\n", min_cost(0, stick_length, 0, num_cuts));
  }

  return 0;
}
