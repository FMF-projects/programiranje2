
public class Vse_se_zacne_z_ena {
	
	public static void main(String[] args){
		String niz = "11";
		izpisi(zaporedje(niz, 4));
	}
	
	public static String preberi_niz(String s){
		char str[] = s.toCharArray();
		String znak = String.valueOf(str[0]);
		int ponovitve = 0;
		String niz = "";
		for (char c:str){
			if (String.valueOf(c).equals(znak)){
				ponovitve += 1;
			}else{
				niz += String.valueOf(ponovitve) + znak;
				znak = String.valueOf(c);
				ponovitve = 1;
			}
		}
		niz += String.valueOf(ponovitve) + znak;
		return niz;
	}
	
	public static String[] zaporedje(String niz, int n){
		String[] zaporedje = new String[n];
		zaporedje[0] = niz;
		for (int i=1; i < n; i++){
			niz = preberi_niz(niz);
			zaporedje[i] = niz;
		}
		return zaporedje;
	}
	
	public static void izpisi(String[] zaporedje){
		System.out.print("{");
		for (int i = 0; i < zaporedje.length; i++){
			if (i == 0){
				System.out.print(zaporedje[i]);
			}else{
				System.out.print("," + zaporedje[i]);
			}
		}
		System.out.print("}");
	}		
}

