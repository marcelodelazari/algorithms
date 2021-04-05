/**
 * Classe que implementa do Counting Sort vista em sala. Desta vez este
 * algoritmo deve satisfazer os seguintes requisitos:
 * - Alocar o tamanho minimo possivel para o array de contadores (C)
 * - Ser capaz de ordenar arrays contendo numeros negativos
 */
public class ExtendedCountingSort extends AbstractSorting<Integer> {

	@Override
	public void sort(Integer[] array, int leftIndex, int rightIndex) {
		if(leftIndex >= rightIndex || leftIndex >= array.length-1 || rightIndex <= 0) {
			return;
		}
		
		int[] ordenado = new int[rightIndex - leftIndex + 1];
		
		int maior = array[leftIndex];
		int menor = array[leftIndex];
		
		for(int i = leftIndex; i <= rightIndex; ++i) {
			if(array[i] > maior) {
				maior = array[i];
			}
			if(array[i] < menor) {
				menor = array[i];
			}
		}
		
		int[] freq = new int[1 + maior - menor];
		for(int i = leftIndex; i <= rightIndex; ++i) {
			freq[array[i] - menor] += 1;
		}
		
		for(int i = 1; i < freq.length; ++i) {
			freq[i] += freq[i - 1];
		}
		
		for(int i = rightIndex; i >= leftIndex; --i) {
			ordenado[freq[array[i] - menor] - 1] = array[i];
			--freq[array[i] - menor];
		}
		
		for(int i = leftIndex; i <= rightIndex; ++i) {
			array[i] = ordenado[i - leftIndex]; // Alterando o array original
		}
	}

}
