import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.*; //* da ne dodaja vsakega .util posebej

public class Frekvence_besed {

	public static void main(String[] args) throws IOException {
		Set<String> spreglej_besede = ne_stej_besed("spreglej.txt");
		System.out.println(pojavitve_besed("Hisa_Marije_pomocnice.txt", spreglej_besede));

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
}

