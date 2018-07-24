import React, {PropTypes } from 'react';

const WineInfo = (props) => {
  console.log('WineInfo called');
  console.log('props: ', props);
  return (
    <div className="wineInfo">
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
  );
};

export default WineInfo;
