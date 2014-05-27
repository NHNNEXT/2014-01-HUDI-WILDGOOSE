package next.wildgoose.dao;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

import javax.servlet.http.HttpServletRequest;

import next.wildgoose.dao.template.SelectJdbcTemplate;

import org.json.JSONObject;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class NumberOfArticlesDAO implements ExtractDAO{
	private static final Logger LOGGER = LoggerFactory.getLogger(NumberOfArticlesDAO.class.getName());
	
	public JSONObject byDay(final int reporterId) {
		SelectJdbcTemplate template = new SelectJdbcTemplate() {
			
			@Override
			protected Object mapRow(ResultSet rs) throws SQLException {
				JSONObject result = new JSONObject();
				JSONObject data = new JSONObject();
				while (rs.next()) {
					data.accumulate(rs.getString("date"), rs.getInt("count"));
				}
				result.put("data", data);
				return result;
			}

			@Override
			protected void setValues(PreparedStatement psmt) throws SQLException {
				psmt.setInt(1, reporterId);
			}
			
		};
		
		StringBuilder query = new StringBuilder();
		query.append("select date_format(datetime, '%m/%d') as date, count(URL) as count from article ");
		query.append("WHERE URL in (Select article_URL as url from article_author where author_id = ?) ");
		query.append("and DATEDIFF(now(), article.datetime) < 7 ");
		query.append("group by date_format(datetime, '%m/%d');");
		
		JSONObject result = new JSONObject();
		result = (JSONObject) template.select(query.toString());
		return result;
	}
	
	public JSONObject bySection (final int reporterId) {
		SelectJdbcTemplate template = new SelectJdbcTemplate() {
			
			@Override
			protected Object mapRow(ResultSet rs) throws SQLException {
				JSONObject result = new JSONObject();
				while (rs.next()) {
					JSONObject data = new JSONObject();
					data.put("label", rs.getString(1));
					data.put("value", rs.getInt(2));
					result.append("data", data);
				}
				return result;
			}

			@Override
			protected void setValues(PreparedStatement psmt) throws SQLException {
				psmt.setInt(1, reporterId);
			}
			
		};
		
		StringBuilder query = new StringBuilder();
		query.append("SELECT distinct sec.name, count(section_id) FROM article ");
		query.append("JOIN (SELECT author_id, article_URL FROM article_author as aa WHERE aa.author_id = ?) as result ");
		query.append("ON URL = result.article_URL ");
		query.append("JOIN section as sec ON section_id = sec.id ");
		query.append("GROUP BY section_id ORDER BY section_id LIMIT 5;");

		JSONObject result = new JSONObject();
		result = (JSONObject) template.select(query.toString());
		return result;
	}

	public JSONObject getJson(int reporterId, HttpServletRequest request) {
		String condition = request.getParameter("by");
		
		if ("section".equals(condition)) {
			return bySection(reporterId);
		} else if ("day".equals(condition)) {
			return byDay(reporterId);
		}
		return null;
	}
}
