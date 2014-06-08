package next.wildgoose.backcontroller;

import javax.servlet.ServletContext;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpSession;

import next.wildgoose.dao.SignDAO;
import next.wildgoose.dto.AccountResult;
import next.wildgoose.dto.SimpleResult;
import next.wildgoose.framework.BackController;
import next.wildgoose.framework.Result;
import next.wildgoose.utility.Constants;
import next.wildgoose.utility.SHA256;
import next.wildgoose.utility.Uri;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class SessionController implements BackController {
	private static final Logger LOGGER = LoggerFactory.getLogger(SessionController.class.getName());

	@Override
	public Result execute(HttpServletRequest request) {
		Result result = null;
		Uri uri = new Uri(request);
		String method = request.getMethod();
		
		if (uri.check(1, null)) {
			if ("POST".equals(method)) {
				result = login(request);
			} else if ("DELETE".equals(method)) {
				result = logout(request);
			}
		}
//		else if (uri.check(1, "search")) {
//			if ("POST".equals(method)) {
//				result = login(request);
//			}
//		}
		
		return result;
	}

	private SimpleResult login(HttpServletRequest request) {
		SimpleResult simpleResult = new SimpleResult();
		String email = request.getParameter("email");
		String hashedPassword = request.getParameter("password");
		LOGGER.debug("email: " + email + ", passw: " + hashedPassword);
		ServletContext context = request.getServletContext();
		SignDAO signDao = (SignDAO) context.getAttribute("SignDAO");
		
		HttpSession session = request.getSession();
		String randNum = (String) session.getAttribute("randNum");
		LOGGER.debug(randNum);
		
		String accountPw = signDao.findAccount(email);
		LOGGER.debug(accountPw + randNum);
		LOGGER.debug(SHA256.testSHA256(accountPw + randNum));
		if (accountPw == null) {
			// 가입되지 않은 아이디입니다. 다시 확인해주세요.
			return simpleResult;
		}
		// H(db_password+random)
		if(SHA256.testSHA256(accountPw + randNum).equals(hashedPassword)){
			simpleResult.setStatus(200);
			simpleResult.setMessage("getting user authentication succeed");
			simpleResult.setData("userId", email);
			session.setAttribute("userId", email);
			session.setMaxInactiveInterval(Constants.SESSION_EXPIRING_TIME);

		} else {
			simpleResult.setMessage("getting user authentication failed");
		}
		return simpleResult;
	}

	private SimpleResult logout(HttpServletRequest request) {
		HttpSession session = request.getSession();
		session.removeAttribute("userId");
		
		SimpleResult simpleResult = new SimpleResult();
		simpleResult.setStatus(200);
	    simpleResult.setMessage("removing user authentication succeed");
		return simpleResult;
	}
}
