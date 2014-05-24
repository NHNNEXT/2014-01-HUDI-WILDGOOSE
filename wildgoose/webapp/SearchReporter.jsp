<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>

<!DOCTYPE html>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-zoom=1, user-scalable=no">
<link type="text/css" rel="stylesheet" href="/stylesheet/base.css" />
<link type="text/css" rel="stylesheet" href="/stylesheet/search_reporter.css" />
<link type="text/css" rel="stylesheet" href="/stylesheet/search.css" />
<link type="text/css" rel="stylesheet" href="/stylesheet/card.css" />
<link type="text/css" rel="stylesheet" href="/stylesheet/card-media.css" />
<script type="text/template" id="reporter-card-template">
<div class="card-section card-section-identity">
	<h3 class="name">
		<a href="/reporters/%= id %">%= name %</a>
	</h3>
	<p class="email">%= email %</p>
	<h4 class="favorite off">&#x2605;</h4>
	<div class="%= pressName % press-tag"></div>
</div>
<div class="card-section card-section-headline">
	<h4 class="headline">%= articleTitle %</h4>
</div>
</script>
<title>Wildgoose</title>

<div class="wrap">
	<header class="header">
		<%@ include file ="template/header.jsp" %>
	</header>
	<div class="container">
		<div class="logo">
			<a href="/"><img src="image/logo.png" alt="wildgoose logo" class="logo-image"/></a>
		</div>
		<div class="search search-column">
			<form class="search_form" action="./" method="get" >
			<ul class="search-column-box">
				<li class="search-query-entry">
					<input type="search" autocomplete="off" id="query-entry" name="q" placeholder="기자, URL검색" value="${ requestScope.searchQuery }" />
				</li>
				<li class="search-button">
					<input type="submit" id="search-action" value ="Search"/>
				</li>
			</ul>
			<%-- 자동완성 --%>
			<ul class="auto-completion-list">
				<!-- <li><div>서동규</div></li>
				<li><div>서동유</div></li>
				<li><div>호호호</div></li>
				<li><div>하하하</div></li>
				<li><div>히히히</div></li> -->
			</ul>
			</form>
			
			<!-- <table class="searched-box">
  				<tbody>
    				<tr>
				    </tr>
  				</tbody>
			</table> -->
		</div>
		
		<div class="search-result">
			<ul>
				<c:choose>
					<%-- message 존재시 --%>
					<c:when test="${ not empty requestScope.message }">
						<span>${ requestScope.message }</span>
					</c:when>
					<%-- searchQuery 존재시 --%>
					<c:when test="${ not empty requestScope.searchQuery }">
						<c:if test="${ empty requestScope.reporterCards }">
							<span>${ requestScope.searchQuery }에 대한 검색 결과가 없습니다.</span>
						</c:if>
						<c:forEach var="reporterCard" items="${ requestScope.reporterCards }"><li class="card card-reporter">
							<%@ include file = "template/reporterCard.jsp" %>
						</li></c:forEach>
					</c:when>
				</c:choose>
			</ul>
		</div>
		<%-- searchQuery 존재시 and 검색 결과가 더 많을 때 --%>
		<c:if test="${ not empty requestScope.searchQuery and requestScope.hasMoreCards == true }">
			<div class="search-more">
				<div class="search-button search-button-ajax">더보기</div>
				<div class="search-state search-state-hidden">
				<div class="state-search-query hidden">${ requestScope.searchQuery }</div>
				<div class="state-search-total hidden">${ requestScope.totalNum }</div>
				</div>
			</div>
		</c:if>
	</div>
	<footer class="footer"></footer>
</div>

<script type="text/javascript" src="/scripts/util.js"></script>
<script type="text/javascript" src="/scripts/searchReporter.js"></script>
<script type="text/javascript" src="/scripts/auto-complement.js"></script>
<script type="text/javascript" src="/scripts/fav.js"></script>
<script>
/* var inputEl = document.getElementById("query-entry");
inputEl.focus(); */

/* var favs = []
getFavs(); */
</script>
