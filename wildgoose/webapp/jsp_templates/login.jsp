<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions"%>

<div class="error-container">
<form class="form-container" name="login">
	<div class="input input-column">
		<ul class="input-column-box">
			<li class="input-query-entry">
				<input type="email" id="email" name="email" placeholder="이메일을 입력하세요" data-check="true"/>
			</li>
			<li class="input-error-label">
				<label for="email" class="form-msg msg-email"></label>
			</li>
		</ul>
	</div>
	
	<div class="input input-column">
		<ul class="input-column-box">
			<li class="input-query-entry">
				<input type="password" id="password" name="password" placeholder="비밀번호를 입력하세요" data-check="true"/>
			</li>
			<li class="input-error-label">
				<label for="password" class="form-msg msg-password"></label>
			</li>
		</ul>
	</div>
	
	<div class="input-column">
		<span id="result-msg"></span>
	</div>

	<button type="button" name="submit" class="disable">로그인하기</button>
</form>
</div>