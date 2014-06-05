<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-zoom=1, user-scalable=no">
<link type="text/css" rel="stylesheet" href="/stylesheet/base.css" />
<!-- <link type="text/css" rel="stylesheet" href="/stylesheet/basic_layout.css" /> -->

<!-- <link type="text/css" rel="stylesheet" href="/stylesheet/card.css" /> -->
<link type="text/css" rel="stylesheet" href="/stylesheet/signup.css" />


<title>Wildgoose</title>

<div class="wrap">
	<header class="header"></header>
	<div class="container">
		<div class="card card-login">
			<form class="form-container">
				<div class="card-section card-section-profile">
					<div class="profile-circle">
						<div class="profile-circle-photo"><img src="/image/logo.png" alt="photo" class="profile-photo"/></div>
					</div>
					
				</div>
				<div class="card-section card-section-email">
					<input class="input" type="email" id="email" name="email" placeholder="이메일" />
					<label for="name" class="form-msg msg-email"></label>
				</div>
				<div class="card-section card-section-password">
					<input class="input" type="password" id="password" name="password" placeholder="비밀번호" data-check="true"/>
					<label for="password" class="form-msg msg-password"></label>
				</div>
				<div class="card-section card-section-confirm">
					<input class="input" type="password" id="confirm" name="confirm" placeholder="다시입력" data-check="true"/>
					<label for="confirm" class="form-msg msg-password"></label>
				</div>
				<div class="card-section card-section-submit">
					<button class="button" id="create">가입하기</button>
				</div>
				<div class="card-section card-section-other">
					<a href="/accounts/login">로그인하기</a>
				</div>
			</form>
		</div>
	</div>
	<footer class="footer"></footer>
</div>