
public class Poudarjanje_znakov {

	public static void main(String[] args){
		poudari("Zadnja novica");
		poudari_izbrano("Zadnja *novica* danes!");
	}
	
	public static void poudari(String s){
		char str[] = s.toCharArray();
		for (char c: str){
			if (c == str[0]){
				System.out.print(Character.toUpperCase(c));
			}else{
				String niz = " " + Character.toUpperCase(c);
				System.out.print(niz);
			}		
		}
	}
	
	public static void poudari_izbrano(String s){
		char str[] = s.toCharArray();
		Boolean poudari = false;
		for (char c: str){
			if (String.valueOf(c).equals("*")){
				poudari = !poudari;
			}else{
				if (poudari == false){
					if (c == str[0]){
						System.out.print(c);
					}else{
						String niz = " " + c;
						System.out.print(niz);
					}
				}else{
					String niz = " " + Character.toUpperCase(c);
					System.out.print(niz);
				}
			}
		}
	}
}
