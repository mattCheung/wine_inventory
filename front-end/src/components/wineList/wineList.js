import React, {PropTypes } from 'react';

const TableRow = ({row}) => (
  <tr>
    {/* have a button to load wine specific info for editing? */}
    <td key={row.id}> {row.id} </td>
    <td key={row.name}> {row.name} </td>
    <td key={row.type}> {row.type} </td>
    <td key={row.year}> {row.year} </td>
    <td key={row.winery}> {row.winery} </td>
    <td key={row.quantity}> {row.quantity} </td>
    <td key={row.uri}> <button wineid={row.id} onClick={() => row.onClick(row)}> {row.uri} </button> </td>
  </tr>
)

const WineList = ({wines}) => (
  <table>
    <tbody>
      <tr key="row_names">
        <td key="id"> ID </td>
        <td key="name"> Name </td>
        <td key="type"> Type </td>
        <td key="year"> Year </td>
        <td key="winery"> Winery </td>
        <td key="quantity"> Quantity </td>
        <td key="uri"> URI </td>
      </tr>
      {wines.map(wine => (
        <TableRow row={wine} />
      ))}
    </tbody>
  </table>
)

export default WineList;
