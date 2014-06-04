package next.wildgoose.framework;

import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import next.wildgoose.utility.Uri;

public interface View {
	public void show(HttpServletRequest request, HttpServletResponse response, Uri uri, Result resultData) throws ServletException, IOException;
}
