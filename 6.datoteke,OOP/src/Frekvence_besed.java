import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*; //* da ne dodaja vsakega .util posebej

import javafx.util.Pair;

public class Frekvence_besed {

	public static void main(String[] args) throws IOException {
		System.out.println(frekvence_besed("Hisa_Marije_pomocnice.txt", "spreglej.txt"));

	}

	public static Map<String, Integer> pojavitve_besed(String vhodna, Set<String> mnozica) throws IOException{
		
		BufferedReader vhod = new BufferedReader( new FileReader(vhodna));
		Map<String, Integer> slovar_besed = new HashMap<String, Integer>();
		while (vhod.ready()){
			String vrstica = vhod.readLine().trim().toLowerCase();
			if (vrstica.isEmpty()) continue;
			StringTokenizer st = new StringTokenizer(vrstica, " .,;!?()[]-\"'+");
			while(st.hasMoreTokens()){
				String beseda = st.nextToken();
				if (mnozica.contains(beseda)) continue;		
				if (slovar_besed.containsKey(beseda)){
					int pojavitve = slovar_besed.get(beseda);
					slovar_besed.put(beseda, pojavitve + 1);
				}else{
					slovar_besed.put(beseda, 1);
				}
			}
		}
		return slovar_besed;
	}
	
	public static Set<String> ne_stej_besed(String vhodna) throws IOException{
		BufferedReader vhod = new BufferedReader( new FileReader(vhodna));
		Set<String> besede = new HashSet<String>();
		while (vhod.ready()){
			String beseda = vhod.readLine().trim().toLowerCase();
			if (beseda.isEmpty()) continue;
			if (besede.contains(beseda) == false){
				besede.add(beseda);
			}
		}
		return besede;
	}
	
	public static Vector<String> vektor(Map<String, Integer> slovar){
		Vector<String> besede = new Vector();
		int max = 0;
		for (String beseda : slovar.keySet()){
			int vrednost = slovar.get(beseda);
			if (vrednost > max){
				max = vrednost;
			}
		}
		for (int i=max; i >= 1; i--){
			for (String b : slovar.keySet()){
				if (slovar.get(b) == i){
					besede.add(b);
				}
			}
		}
		return besede;
	}
	
	public static List<String> frekvence_besed(String datoteka, String spreglej) throws IOException{
		Set<String> spreglej_besede = ne_stej_besed(spreglej);
		Map<String, Integer> slovar_besed = pojavitve_besed("Hisa_Marije_pomocnice.txt", spreglej_besede);
		Vector<String> vektor_besed = vektor(slovar_besed);
		
		List<String> besede = new ArrayList<String>();
		for (String beseda : vektor_besed){
			besede.add("(" + beseda + ":" + String.valueOf(slovar_besed.get(beseda)) + ")" );
		}
		return besede;
	}
}


