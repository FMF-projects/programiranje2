import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;

public class Predor {

	public static void main(String[] args) throws IOException {
		System.out.println(krsitelji("predor.txt", "krsitelji.txt"));
	}
	
	public static int krsitelji(String vhodna, String izhodna) throws IOException{
		
		DecimalFormatSymbols sym = new DecimalFormatSymbols();
		sym.setDecimalSeparator('.');
		DecimalFormat df = new DecimalFormat("0.00", sym);
		df.setRoundingMode(RoundingMode.HALF_UP);
		
		BufferedReader vhod = new BufferedReader(new FileReader(vhodna));
		PrintWriter izhod = new PrintWriter(new FileWriter(izhodna));
		
		int omejitev_hitrosti = 80; //v km/h
		double dolzina_predora = 622; //v m
		int stevilo_krsiteljev = 0;
		double najhitrejsi = 0;
		
		while (vhod.ready()){
			String vrstica = vhod.readLine().trim();
			if (vrstica.isEmpty()) continue;
			String[] besede = vrstica.split(" +"); //+ èe imamo veè presledkov
			double cas = Integer.parseInt(besede[1]) - Integer.parseInt(besede[0]);
			double povprecna_hitrost = dolzina_predora / cas * 3.6;
			if (povprecna_hitrost > omejitev_hitrosti){
				izhod.println(besede[2] + " " + df.format(povprecna_hitrost));
				stevilo_krsiteljev += 1;
			}
			if (povprecna_hitrost > najhitrejsi){
				najhitrejsi = povprecna_hitrost;
			}
		}
		System.out.println(najhitrejsi);
		vhod.close();
		izhod.close();
		return stevilo_krsiteljev;	
	}
	
	
}
