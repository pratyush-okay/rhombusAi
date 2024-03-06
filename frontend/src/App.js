import React, { useState } from 'react';
import DataTable from './components/data_table';
import './App.css';

const App = () => {

    const [file, setFile] = useState(null);
    const [fileName, setFileName] = useState('No file selected');
    const [data, setData] = useState(null);

    const handleFileChange = (e) => {
        const selectedFile = e.target.files[0];
        setFile(selectedFile);
        setFileName(selectedFile ? selectedFile.name : 'No file selected');
    }

    const handleUpload = (e) => {
        e.preventDefault()
        const formData = new FormData();
        formData.append('file', file, 'file.csv');
        fetch("http://localhost:8000/process_data/", {
            method: 'POST',
            body: formData,
        })
            .then(response => {
                if (response.ok) {
                    return response.json()
                } else {
                    response.text().then(text => console.log(text));
                    throw new Error('Unable to upload file');
                }
            }).then(data => { 
                setData(data);
                console.log(data); })
            .catch(error => {
                console.error(error);
                alert('Error uploading file');
            });
    };

    return (
        <div className='output'>
            <h1>Data Processing App</h1>
            {/* Form to handle file upload */}
            <form onSubmit={(e) => { handleUpload(e) }}>
                <div className='upload'>
                    <label className='uploadLabel' htmlFor="fileToUpload">Upload a file</label>
                    <input type="file" name="fileToUpload" id="fileToUpload" onChange={handleFileChange}/>
                    <span  style={{ marginLeft: '30px' }}>{fileName}</span>
                </div>
                <button type="submit" value="Upload" onClick={handleUpload}>Upload</button>

            </form>
            {/* Display processed data */}
            {data && <DataTable data={data} />}
        </div>
    );
};

export default App;
