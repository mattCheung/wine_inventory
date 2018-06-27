import axios from "axios";
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import wineInfo from './components/wineInfo/wineInfo';
import WineList from './components/wineList/wineList';
import NewWine from './components/newWine/newWine';

class App extends Component {


  state = {
    wines: []
  };

  componentDidMount() {
    axios.get("http://localhost:5000/wine_list/api/v1.0/winelist")
      // axios.get("http://localhost:5000/wine_list/api/v1.0/winelist/5b21b38431751f798b0c0665")
    .then(response => {
      const newWines = response.data.wine.map(wine => {
        return {
          id: wine._id,
          year: wine.year,
          type: wine.type,
          winery: wine.winery,
          name: wine.name,
          quantity: wine.quanty ? wine.quantity : 1,
          uri: wine.uri
        };
      });
      {/*
      console.log('backend response: ', response.data.wine);
      */}
      const newState = Object.assign({}, this.state, {
        wines: newWines
      });
      this.setState(newState);
      {/*
      console.log('app state in mount: ', this.state.wines);
      */}
    }).catch(error => console.log(error));
  }

  render() {
    const temp_wines = { wines: [{name: "Gamay Rouge", type:"gamay rouge", uri: "http://localhost:5000/wine_list/api/v1.0/winelist?task_id=5b21b2d931751f798b0c0664"
    , winery: "V Sattui", year: 2016, _id: "5b21b2d931751f798b0c0664"}, {year: 2000, type: "test 2", winery: "test winery 2", name: "none 2"}]};
    {/*
    console.log("app temp_wines in render:", temp_wines);
    console.log("app state in render: ", this.state.wines);
    */}

    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>


        <WineList wines={this.state.wines}/>

        {/*
          <button onClick={() => (<NewWine />)}> Add new </button>
          <button onClick={() => alert('adding new!')}> Add new </button>

        */}

        <NewWine />


      </div>
    );
  }
}

export default App;
