import React from "react";
import ReactDOM from "react-dom";
import { Route, Redirect, Switch, withRouter } from "react-router-dom";
import ModuleBoardContainer from "./ModuleBoard/ModuleBoard";
import DataProvider from "./DataProvider";
import Table from "./Table";

const App = () => {
	return (
		<Switch>
			<Route path="/b/:boardId" component={BoardContainer} />
			<Redirect to="/" />
		</Switch>
	);
}
