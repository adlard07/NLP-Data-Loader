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
        
        if (data.error) {
            output.textContent = `Error: ${data.error}`;
        } else {
            output.textContent = `SQL Query: ${data.query}`;
            displayResultInNewWindow(data.result);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayResultInNewWindow(result) {
    const newWindow = window.open('', 'ResultWindow', 'width=600,height=400');
    newWindow.document.write('<html><head><title>Query Result</title>');
    newWindow.document.write('<style>table {border-collapse: collapse; width: 100%;} th, td {border: 1px solid black; padding: 8px; text-align: left;}</style>');
    newWindow.document.write('</head><body>');
    newWindow.document.write('<table id="resultTable"></table>');
    newWindow.document.write('<script>');
    newWindow.document.write('const result = ' + JSON.stringify(result) + ';');
    newWindow.document.write(`
        const resultTable = document.getElementById('resultTable');
        if (Object.keys(result).length === 0) {
            resultTable.innerHTML = '<tr><td>No results found</td></tr>';
        } else {
            const firstRow = result[0];
            const columnNames = Array.isArray(firstRow) ? firstRow.map((_, index) => \`Column \${index + 1}\`) : Object.keys(firstRow);
            
            const headerRow = document.createElement('tr');
            columnNames.forEach(columnName => {
                const th = document.createElement('th');
                th.textContent = columnName;
                headerRow.appendChild(th);
            });
            resultTable.appendChild(headerRow);

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
    `);
    newWindow.document.write('</script>');
    newWindow.document.write('</body></html>');
    newWindow.document.close();
}