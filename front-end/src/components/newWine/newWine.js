import React, {PropTypes } from 'react';
import axios from "axios";

class NewWine extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      type: '',
      year: '',
      vinyard: '',
      quantity: 1
  };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  };

  handleChange(event) {
    // console.log(this.props);
    this.setState({[event.target.name]: event.target.value});
  };

  handleSubmit(event) {
    alert('Info was submitted');
    console.log("name: " + this.state.name);
    console.log("type: " + this.state.type);
    console.log("year: " + this.state.year);
    console.log("vinyard: " + this.state.vinyard);
    console.log("quantity: " + this.state.quantity);
    event.preventDefault();

    axios.post("http://localhost:5000/wine_list/api/v1.0/winelist", {
      name: this.state.name,
      type: this.state.type,
      year: this.state.year,
      winery: this.state.vinyard,
      quantity: this.state.quantity})
      // axios.get("http://localhost:5000/wine_list/api/v1.0/winelist/5b21b38431751f798b0c0665")
    .then(response => {
      console.log('backend response: ', response);
    }).catch(error => console.log(error));
  };

  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <label>
          Name:
          <input className="wineName" name="name" type="text" value={this.state.name} onChange={this.handleChange} />
        </label>
        <label>
          Type:
          <input className="wineType" name="type" type="text" value={this.state.type} onChange={this.handleChange} />
        </label>
        <label>
          Vinyard:
          <input className="wineVinyard" name="vinyard" type="text" value={this.state.vinyard} onChange={this.handleChange} />
        </label>
        <label>
          Year:
          <input className="wineYear" name="year" type="text" value={this.state.year} onChange={this.handleChange} />
        </label>
        <label>
          Quantity:
          <input className="wineQuantity" name="quantity" type="text" value={this.state.quantity} onChange={this.handleChange} />
        </label>
        <input type="submit" value="Submit" />
      </form>
    )};
};

export default NewWine;
