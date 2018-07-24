import axios from "axios";
import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

import WineInfo from './components/wineInfo/wineInfo';
import WineInfoClass from './components/wineInfo/wineinfoclass';
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
          uri: wine.uri,
          onClick: this.loadWineInfo
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

  loadWineInfo(props) {
    // alert('loadWineInfo!');
    console.log('loadWineInfo called!');
    console.log('props: ', props);
      return (
        <div>
          // <WineInfo wine={props}/>
          <WineInfoClass wine={props}/>
        </div>
      );
  };

  render() {
    {/*
    console.log("app temp_wines in render:", temp_wines);
    console.log("app state in render: ", this.state.wines);
    */}

    return (
      <div className="App">


        <WineList wines={this.state.wines} onClick={this.loadWineInfo}/>



        <NewWine />
        <WineInfoClass />


      </div>
    );
  }
}

export default App;
