
public class Razcep {
	
	public static void main(String[] args){
		razcepi(3666);
	}

	public static void razcepi(int n){
		char op = '=';
		for (int d=2; d*d<=n; ++d){
			int e = 0;
			while (n % d == 0){
				n /= d;
				++e;
			}
			
			if (e > 0){
				String niz = " " + op + " " + d + "^" + e;
				System.out.print(niz);
				op = '*';
			}
		}
		
		if (n > 1){
			String niz = " " + op + " " + n;
			System.out.print(niz);
		}	
	}
}
