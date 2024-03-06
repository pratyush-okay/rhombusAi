import React, { useState } from 'react';
import "./data_table.css";

const DataTable = ({ data }) => {
    const allowed_data_conversions = {
        'Text': ['Text', 'Category'],
        'Int': ['Int', 'Float', 'Text', 'Category'],
        'Float': ['Float', 'Int', 'Text', 'Category'],
        'Bool': ['Bool', 'Text', 'Category'],
        'Date': ['Date', 'Text', 'Category'],
        'TimeDelta': ['TimeDelta', 'Text', 'Category'],
        'Category': ['Category', 'Text']
    }
    // State to store selected data types
    const [selectedDataTypes, setSelectedDataTypes] = useState({});
    const [updatedDataTypes, setUpdatedDataTypes] = useState({});
    // Function to update selected data types
    const updateSelectedDataTypes = (field, dataType) => {
        setSelectedDataTypes(prevState => ({
            ...prevState,
            [field]: dataType
        }));
    };


    const updateDataTypes = () => {
        setUpdatedDataTypes(selectedDataTypes);
       
    }
    

    return (
        <div>
            {/* Processed data types */}
            <table>
                <thead>
                    <tr>
                        <th>Field</th>
                        <th>Inferred Data Type</th>
                        <th>Selected Data Type</th>
                    </tr>
                </thead>
                <tbody>
                    {Object.entries(data).map(([field, dataType]) => (
                        <tr key={field}>
                            <td>{field}</td>
                            <td>{dataType}</td>
                            <td>
                                <select
                                    value={selectedDataTypes[field] || dataType}
                                    onChange={(e) => updateSelectedDataTypes(field, e.target.value)}
                                >
                                    {allowed_data_conversions[dataType].map(type => (
                                        <option key={type} value={type}>{type}</option>
                                    ))}
                                </select>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {/* Updated data types */}
            <button type="file" name="file" id="file" onClick={updateDataTypes}>Update Data Types</button>
            {Object.keys(updatedDataTypes).length > 0  && (
                <div>
                    <h2>Updated Data Types</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>Field</th>
                                <th>Data Type</th>
                            </tr>
                        </thead>
                        <tbody>
                            {Object.entries(updatedDataTypes).map(([field, dataType]) => (
                                <tr key={field}>
                                    <td>{field}</td>
                                    <td>{dataType}</td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            )}
        </div>
    );
};

export default DataTable;
