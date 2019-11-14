import React from "react";
import ReactDOM from "react-dom";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Form from "./MovementForm";

const App = () => (
	<React.Fragment>
	 <DataProvider endpoint="api/movement/" render={data => <Table data={data} />} />
	 <Form endpoint="api/movement/" />
	</React.Fragment>
);

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper) : null;
