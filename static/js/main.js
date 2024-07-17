function sendPrompt() {
    const prompt = document.getElementById('prompt').value;
    fetch('/generate_query', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ prompt: prompt }),
    })
    .then(response => response.json())
    .then(data => {
        const output = document.getElementById('output');
        const resultTable = document.getElementById('result');
        
        if (data.error) {
            output.textContent = `Error: ${data.error}`;
            resultTable.innerHTML = '';
        } else {
            output.textContent = `SQL Query: ${data.query}`;
            displayResultTable(data.result);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayResultTable(result) {
    const resultTable = document.getElementById('result');
    resultTable.innerHTML = '';

    if (Object.keys(result).length === 0) {
        resultTable.innerHTML = '<tr><td>No results found</td></tr>';
        return;
    }

    // Get column names
    const firstRow = result[0];
    const columnNames = Array.isArray(firstRow) ? firstRow.map((_, index) => `Column ${index + 1}`) : Object.keys(firstRow);

    // Create table header
    const headerRow = document.createElement('tr');
    columnNames.forEach(columnName => {
        const th = document.createElement('th');
        th.textContent = columnName;
        headerRow.appendChild(th);
    });
    resultTable.appendChild(headerRow);

    // Create table rows
    Object.values(result).forEach(rowData => {
        const row = document.createElement('tr');
        (Array.isArray(rowData) ? rowData : Object.values(rowData)).forEach(cellData => {
            const cell = document.createElement('td');
            cell.textContent = cellData;
            row.appendChild(cell);
        });
        resultTable.appendChild(row);
    });
}