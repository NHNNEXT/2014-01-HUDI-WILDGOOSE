package next.wildgoose.dto.result;

import next.wildgoose.framework.Result;

public class SimpleResult extends Result {

	public SimpleResult() {
		super();
	}
	public SimpleResult(boolean success) {
		super(success);
	}
	public void setData(String key, Object value) {
		super.data.put(key, value);
	}
}
