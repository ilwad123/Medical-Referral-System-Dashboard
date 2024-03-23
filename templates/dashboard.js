document.addEventListener('DOMContentLoaded', function() {
    function fetchCSV() {
        fetch('patients.csv')
            .then(response => response.text())
            .then(data => processData(data));
    }


    function processData(csvData) {
        const rows = csvData.split('\n');
        const headers = rows.shift().split(',');
        const patientDataContainer = document.getElementById('patientData');
        let displayedCount = 0;


        rows.forEach(row => {

            const values = row.split(',');
            const patientDiv = document.createElement('div');
            patientDiv.className = 'sales';
            

            headers.forEach((header, index) => {
                const p = document.createElement('p');
                p.textContent = `${header}: ${values[index]}`;
                patientDiv.appendChild(p);
            });


            patientDataContainer.appendChild(patientDiv);
            displayedCount++;
        });


        if (rows.length > 9) {
            const scrollButton = document.getElementById('scrollButton');
            scrollButton.style.display = 'block';
            scrollButton.addEventListener('click', function() {
                patientDataContainer.scrollTop += 50; 
            });
        }
    }

    fetchCSV();
});
