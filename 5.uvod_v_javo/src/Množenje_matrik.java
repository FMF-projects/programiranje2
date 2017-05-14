
public class Množenje_matrik {

	public static void main(String[] args){
		double[][] a = {{2,0,0},{0,0,0}};
		double[][] b = {{1,0,0},{1,2,0},{1,0,0}};
		izpisi(zmnozi(a, b));
	}
	
	public static double[][] zmnozi(double[][] a, double[][] b){
		if (a[0].length != b.length){
			return null;
		}else{
			double[][] c = new double[a.length][b[0].length];
			for (int vrstica=0; vrstica < a.length; vrstica++){
				for (int stolpec=0; stolpec < b[0].length; stolpec++){
					double zmnozek = 0;
					for (int i=0; i < a[0].length; i++){
						double z = a[vrstica][i] * b[i][stolpec];
						zmnozek += z;
					}
					c[vrstica][stolpec] = zmnozek;	
				}
			}
		return c;	
		}
	}
	
	public static void izpisi(double[][] matrika){
		try
		{
			System.out.print("[");
			for (int i=0; i < matrika.length; i++){
				System.out.print("[");
				for (int j=0; j < matrika[0].length; j++){
					if (j != matrika[0].length - 1){
						System.out.print(matrika[i][j]);
						System.out.print(", ");
					}else{
						System.out.print(matrika[i][j]);
					}
				}
				if (i != matrika.length - 1){
					System.out.print("], ");
				}else{
					System.out.print("]");
				}	
			}
			System.out.print("]");
		}
		catch(NullPointerException e){
			System.out.print("Mnozenje matrik ni mogoce.]");
		}
	}
		
		
}

