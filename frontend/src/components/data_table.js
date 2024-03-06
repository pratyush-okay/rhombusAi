import React from 'react';
import "./data_table.css";

const DataTable = ({ data, handleTypeChange }) => {
    const types = ['object', 'datetime', 'int', 'category', 'text', 'boolean', 'float'];

    return (
        <div>
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
                                    value={dataType}
                                    onChange={(e) => handleTypeChange(field, e.target.value)}
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
        </div>
    );
};

export default DataTable;