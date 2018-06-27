import React, {PropTypes } from 'react';

const WineInfo = (props) => {
  for (let wine of props) {

  }

  return (
    <div className="wineInfo">
      <span className="wineName"> Name: name </span>
      <span className="wineYear"> Year: year </span>
      <span className="wineType"> Type: type </span>
      <span className="winery"> Winery: winery </span>
      <span className="quantity"> Quantity: quantity </span>
      <span className="notes"> Notes: notes </span>
      <span className="tags"> Tags: tags </span>
    </div>
  );
};

export default WineInfo;
