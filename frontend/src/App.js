import './App.css';
import React, { Component } from 'react';
import axios from 'axios';

class App extends Component {
  state = {
    selectedFile: null,
    fileUploadedSuccessfully: false
  }

  onFileChange = event => {
    this.setState({ selectedFile: event.target.files[0] });
  }

  onFileUpload = async () => {
    const { selectedFile } = this.state;

    if (!selectedFile) {
      console.error('Nessun file selezionato.');
      return;
    }

    const formData = new FormData();
    formData.append('csv', selectedFile);

    try {
      const response = await axios.post('URL_DEL_TUO_API_GATEWAY', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Gestisci la risposta dal backend
      console.log(response.data);

      // Resetta lo stato per consentire un nuovo caricamento
      this.setState({
        selectedFile: null,
        fileUploadedSuccessfully: true,
      });
    } catch (error) {
      // Gestisci gli errori
      console.error('Errore durante il caricamento del file:', error);
    }
  }

  fileData = () => {
    if (this.state.selectedFile) {
      return (
        <div>
          <h2>File Details:</h2>
          <p>File Name: {this.state.selectedFile.name}</p>
        </div>
      );
    } else if (this.state.fileUploadedSuccessfully) {
      return (
        <div>
          <br />
          <h4>Il tuo file è stato caricato correttamente</h4>
        </div>
      );
    } else {
      return (
        <div>
          <br />
          <h4 className="description">Scegli un file e premi il pulsante Upload</h4>
        </div>
      );
    }
  }

  render() {
    return (
      <div className="container">
        <h2 className="title">Sort Students</h2>
        <h3 className="text">Elabora file con componente React e API Serverless</h3>
        <div>
          <input type="file" onChange={this.onFileChange} />
          <button className="button" onClick={this.onFileUpload}>Upload</button>
        </div>
        {this.fileData()}
      </div>
    )
  }
}

export default App;
