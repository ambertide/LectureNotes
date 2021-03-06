void mergesort(int n, int a[]) {
	int *aux = new int[n];
	for (int i = 0; i < n; ++i) {
		aux[i] = a[i]
	}
	mergesort_r(a, aux, 0, n-1);
	delete [] aux;
}

void mergesort_r(int a[], int b[], int l, int r) {
	if (r <= l) {
		return;
	}
	int m = (l + r)/2;
	mergesort_r(b, a, l, m);
	mergesort_r(b, a, m + 1, r);
	merge(a + l, m - l + 1, b + l, r - m, b + m, 1)
}
