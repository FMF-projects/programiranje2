
public class Odvod_polinoma {

	public static void main(String[] args){
		int[] p = {4,-1,2,0,1};
		izpisi(odvajaj(p, 2));
	}
	
	public static int[] odvajaj(int[] polinom, int n){
		for (int i = 1; i <= n; i++){
			polinom = odvod(polinom);
		}
		return polinom;
	}
	
	public static int[] odvod(int[] polinom){
		int dolzina = polinom.length;
		int [] odvod = new int[dolzina - 1];
		for (int i = 1; i <= dolzina - 1; i++){
			odvod[i - 1] = polinom[i] * i;
		}
		return odvod;
	}
	
	public static void izpisi(int[] polinom){
		System.out.print("{");
		for (int i = 0; i < polinom.length; i++){
			if (i == 0){
				System.out.print(polinom[i]);
			}else{
				System.out.print("," + polinom[i]);
			}
		}
		System.out.print("}");
	}

}
