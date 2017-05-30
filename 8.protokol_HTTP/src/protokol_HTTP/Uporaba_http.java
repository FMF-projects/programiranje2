package protokol_HTTP;

import java.io.IOException;

import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.omg.CORBA.Request;

public class Uporaba_http {

	public static void main(String[] args) {
        try {
        	String url = "http://chitchat.andrej.com";
        	
        	HttpClient client = HttpClientBuilder.create().build();
        	HttpGet request = new HttpGet(url);
        	HttpResponse response = client.execute(request);
        	
        	
        	System.out.println(arg0);
        	
        	}

	}

}
