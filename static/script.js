document.addEventListener('DOMContentLoaded', function () {
    const tableBody = document.querySelector('#patientTable tbody');
    const exportPDFButton = document.querySelector('#exportPDF');
    const fileInput = document.querySelector('#csvFileInput');

    // Function to populate table with data from CSV
    function populateTable(data) {
        tableBody.innerHTML = '';
        if (data && data.length > 0) {
            data.forEach(row => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${row.Name}</td>
                    <td>${row.Last_Name}</td>
                    <td>${row.Age}</td>
                    <td>${row.Date_of_Birth}</td>
                    <td>${row.Gender}</td>
                    <td>${row.Condition}</td>
                    <td>${row.Need_to_be_Referred}</td>
                `;
                tableBody.appendChild(tr);
            });
        } else {
            tableBody.innerHTML = '<tr><td colspan="17">No data available</td></tr>';
        }
    }

    // Function to export table data to PDF
    function exportToPDF() {
        const doc = new jsPDF();
        doc.autoTable({ html: '#patientTable' });
        doc.save('patient_information.pdf');
    }

    // Event listener for export to PDF button
    exportPDFButton.addEventListener('click', exportToPDF);

    // Event listener for CSV file input
    fileInput.addEventListener('change', function (event) {
        const file = event.target.files[0];
        if (file) {
            Papa.parse(file, {
                header: true,
                complete: function (results) {
                    console.log(results.data); // Log parsed data
                    populateTable(results.data);
                },
                error: function(error) {
                    console.error('Error parsing CSV:', error);
                }
            });
        }
    });
});
