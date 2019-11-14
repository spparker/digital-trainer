import React, { Component } from "react";
import PropTypes from "prop-types";

class MovementForm extends Component {
	static propTypes = {
		endpoint: PropTypes.string.isRequired
	};

	state = {
		name: "",
		description: "",
		video: "",
		unilateral: false,
		difficulty: "BEG"
	};

	handleChange = e => {
		e.preventDefault();
		const { name, description, video, unilateral, difficulty } = this.state;
		const movement = { name, description, video, unilateral, difficulty };
		const conf = {
			method: "post",
			body: JSON.stringify(movement),
			headers: new Headers({ "Content-Type":
				"application/json" })
		};
		fetch(this.props.endpoint, conf).then(response => console.log(response));
	};

	render() {
		const { name, description, video, unilateral, difficulty } = this.state;
		return (
			<div className="column">
			 <form onSubmit={this.handleSubmit}>
			 <div className="field">
			  <label className="label">Name</label>
			  <div className="control">
			   <input
				className="input"
				type="text"
				name="name"
				onChange={this.handleChange}
				value={name}
				required
			/>
			 </div>
		        </div>
			 <div className="field">
                          <label className="label">Description</label>
                          <div className="control">
                           <input
                                className="input"
                                type="text"
                                name="description"
                                onChange={this.handleChange}
                                value={description}
                                required
                        />
			  </div>
			 </div>
			 <div className="field">
                          <label className="label">Video</label>
                          <div className="control">
                           <input
                                className="input"
                                type="text"
                                name="video"
                                onChange={this.handleChange}
                                value={video}
                        />
			  </div>
			 </div>
			 <div className="field">
                          <label className="label">Unilateral</label>
                          <div className="control">
                           <input
                                className="input"
                                type="boolean"
                                name="unilateral"
                                onChange={this.handleChange}
                                value={unilateral}
                        />
                         </div>
                        </div>
			<div className="control">
			 <button type="submit" className="button is-info">
			  Send message
			 </button>
			</div>
			</form>
			</div>
		);
	}
}

export default MovementForm;
			
		
