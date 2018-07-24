import React, {PropTypes } from 'react';
import axios from "axios";

class WineInfoClass extends React.Component {
  constructor(props) {
    super(props);
    console.log('initing WineInfoClass');
    this.render(props);
  }

  render(props) {
    console.log('wineinfoclass called!')
    if (props) {
      return (
          <div className="wineinfo">
            <span className="wineName"> Name: {props.name} </span>
            <span className="wineYear"> Year: {props.year} </span>
            <span className="wineType"> Type: {props.type} </span>
            <span className="winery"> Winery: {props.winery} </span>
            <span className="quantity"> Quantity: {props.quantity} </span>
            <span className="notes"> Notes: {props.notes} </span>
            <span className="tags"> Tags: {props.tags} </span>
            <button> Delete </button>
            <button> Update </button>
          </div>
      )}
    else {
      return (
        <div className="wineinfo">
        </div>
      )};
}};

export default WineInfoClass;
