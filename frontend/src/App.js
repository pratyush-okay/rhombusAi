import React, { useState } from 'react';
const App = () => {


    const [file, setFile] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
    }

    // const endpoint = 'http://localhost:8000/dataprocessing/process_data/';

    const handleUpload = (e) => {
        e.preventDefault()
        // const file = fileInput.files[0];
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
            }).then(data => { console.log(data); })
            .catch(error => {
                console.error(error);
                alert('Error uploading file');
            });
    };

    return (
        <div>
            <h1>Data Processing App</h1>

            <form onSubmit={(e) => { handleUpload(e) }}>
                <input type="file" name="fileToUpload" id="fileToUpload" onChange={handleFileChange}/>
                <button type="submit" value="Upload" onClick={handleUpload}>Upload</button>
            </form>
        </div>
    );
};

export default App;
