
public class Collatzovo_zaporedje {

	public static void main(String[] args){
		System.out.println(dolzina(12));
		System.out.println(najvecji_clen(6));
		izpis(6);
	}
	
	public static int dolzina(int n){
		if (n == 1){
			return 1;
		}
		int stevec = 0;
		while (n != 1){
			if (n % 2 == 0){ 
				stevec++;
				n = n / 2;
			}else{
				n = n * 3 + 1;
				stevec++;
			}
		}	
		stevec++;
		return stevec;
	}	

	public static int najvecji_clen(int n){
		if (n == 1){
			return 1;
		}
		int najvecji = n;
		while (n != 1){
			if (n % 2 == 0){ 
				n = n / 2;
				if (n > najvecji){
					najvecji = n;
				}
			}else{
				n = n * 3 + 1;
				if (n > najvecji){
					najvecji = n;
				}
			}

		}
		return najvecji;
	}
	
	public static void izpis(int n){
		if (n==1){
			System.out.println(n);
		}
	
		System.out.println(n);
		
		while (n!=1){
			if (n % 2 == 0){ 
				n = n / 2;
				System.out.println(n);
			}else{
				n = n * 3 + 1;
				System.out.println(n);
				}
		}
	}
}

