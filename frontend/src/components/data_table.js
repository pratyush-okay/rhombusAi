import React, { useState } from 'react';
import "./data_table.css";

const DataTable = ({ data }) => {
    const types = ['Text', 'Int', 'Float', 'Bool', 'Date', 'TimeDelta', 'Category'];

    // State to store selected data types
    const [selectedDataTypes, setSelectedDataTypes] = useState({});
    const [newDataTypes, setNewDataTypes] = useState(null);

    // Function to update selected data types
    const updateSelectedDataTypes = (field, dataType) => {
        setSelectedDataTypes(prevState => ({
            ...prevState,
            [field]: dataType
        }));
    };

    // Function to create a new dictionary with original and selected changed data types
    const createNewDictionary = () => {
        const newDataTypes = {};
        Object.entries(data).forEach(([field, dataType]) => {
            newDataTypes[field] = selectedDataTypes[field] || dataType;
        });
        setNewDataTypes(newDataTypes);
        console.log(newDataTypes);
    };

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
                                    {types.map(type => (
                                        <option key={type} value={type}>{type}</option>
                                    ))}
                                </select>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>

            {/* Updated data types */}
            <button onClick={createNewDictionary}>Update Data Types</button>
            {newDataTypes && (
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
                            {Object.entries(newDataTypes).map(([field, dataType]) => (
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
