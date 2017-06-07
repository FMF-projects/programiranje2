import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.fluent.Request;
import org.apache.http.client.utils.URIBuilder;

public class Http {

	public static void main(String[] args) throws ClientProtocolException, URISyntaxException, IOException {
		povezava();
		users();
		prijava("t");
		odjava("t");
	}
		
	public static void povezava(){	
		try {
        	String hello = Request.Get("http://chitchat.andrej.com")
                    			  .execute()
                                  .returnContent().asString();
        	System.out.println(hello);
        } catch (IOException e) {
        	e.printStackTrace();
        	}
	}
	
	public static void users(){
	try {
    	String uporabniki = Request.Get("http://chitchat.andrej.com/users")
                			  .execute()
                              .returnContent().asString();
    	System.out.println(uporabniki);
    } catch (IOException e) {
    	e.printStackTrace();
    	}	
	}
	
	public static void prijava(String ime) throws URISyntaxException, ClientProtocolException, IOException{
		URI uri = new URIBuilder("http://chitchat.andrej.com/users")
				.addParameter("username", ime)
				.build();
		
		String responseBody = Request.Post(uri)
									 .execute()
									 .returnContent()
									 .asString();
		System.out.println(responseBody);	
	}
	
	public static void odjava(String ime) throws URISyntaxException, ClientProtocolException, IOException{
		URI uri = new URIBuilder("http://chitchat.andrej.com/users")
				.addParameter("username", ime)
				.build();
		
		String responseBody = Request.Delete(uri)
									 .execute()
									 .returnContent()
									 .asString();
		System.out.println(responseBody);	
	}
}
