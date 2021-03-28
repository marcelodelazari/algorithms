import sorting.AbstractSorting;

/**
 * Merge sort is based on the divide-and-conquer paradigm. The algorithm
 * consists of recursively dividing the unsorted list in the middle, sorting
 * each sublist, and then merging them into one single sorted list. Notice that
 * if the list has length == 1, it is already sorted.
 */
public class MergeSort<T extends Comparable<T>> extends AbstractSorting<T> {

	@Override
	public void sort(T[] array, int leftIndex, int rightIndex) {
		if(leftIndex >= rightIndex || leftIndex >= array.length || rightIndex <= 0){
			return;
		}

		int middle = (leftIndex + rightIndex) / 2;
		sort(array, leftIndex, middle);
		sort(array, middle + 1, rightIndex);

		merge(array, leftIndex, middle, rightIndex);
	}

	private void merge(T[] array, int left, int middle, int right){

		T[] ans = (T[]) new Comparable[array.length];

		for(int i = left; i <= right; ++i){
			ans[i] = array[i];
		}

		int i = left;
		int j = middle + 1;
		int k = left;

		while(i <= middle && j <= right){

			if(array[i].compareTo(array[j]) < 0){
				ans[k] = array[i];
				++i;
			}
			else{
				ans[k] = array[j];
				++j;
			}
			++k;
		}

		while(i <= middle){
			ans[k] = array[i];
			++i;
			++k;
		}

		while(j <= right){
			ans[k] = array[j];
			++j;
			++k;
		}
		
		for(i = left; i <= right; ++i){
			array[i] = ans[i];
		}
	}
}
