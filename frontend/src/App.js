import React, { Component } from 'react';
import axios from 'axios';
import AuthorList from "./Author";
import TicketList from "./Ticket";


class App extends Component {
	state = {
		authors: [],
		tickets: []
	};


	componentDidMount() {
	    this.getAuthors();
		this.getTodos();
	}


	getAuthors() {
		axios
 			.get('http://127.0.0.1:8000/api/authors')
			.then(res => {
				this.setState({ authors: res.data });
			})
			.catch(err => {
				console.log(err);
			});
	}

	getTodos() {
		axios
			.get('http://127.0.0.1:8000/api/todos')
			.then(res => {
				this.setState({ tickets: res.data });
			})
			.catch(err => {
				console.log(err);
			});
	}

	render() {
		return (
			<div>
                <h1>Authors of todo tickets</h1>
				<AuthorList authors={this.state.authors} />

				<h1>ToDo tickets</h1>
				<TicketList tickets={this.state.tickets} />
			</div>
		);
	}
}

export default App;
