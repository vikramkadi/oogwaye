var myTableHeaders = [
	{ name: "date", type: "date" },
	{ name: "vendor", type: "string" },
	{ name: "product", type: "string" },
	{ name: "number sold", type: "integer" },
	{ name: "average value", type: "float" },
	{ name: "maximum value", type: "float" },
	{ name: "minimum value", type: "float" }
]

function initTablePane(pane) {
	var categories = pane.find("#table-categories").find(".ui-widget-content");
	var measurements = pane.find("#table-measurements").find(".ui-widget-content");
	for (var i = 0; i< myTableHeaders.length; i++) {
		var token = $("<P></P>").text(myTableHeaders[i].name);
		switch (myTableHeaders[i].type)
		{
			case "date":
			case "string":
			case "integer":
				categories.append(token);
				break;
			case "float":
				measurements.append(token);
				break;
		}
	}
}
