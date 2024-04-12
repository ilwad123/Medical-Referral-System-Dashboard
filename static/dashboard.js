document.addEventListener('DOMContentLoaded', function() {
    const patientsPerPage = 9;
    let displayedCount = 0;

    const fetchData = async () => {
        try {
            const response = await fetch('./static/Algorithm.csv');
            const csvData = await response.text();
            processData(csvData);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    const processData = (csvData) => {
        const rows = csvData.split('\n');
        const headers = rows.shift().split(',');

        const patientDataContainer = document.getElementById('patientData');
        patientDataContainer.innerHTML = '';

        const patientsToDisplay = rows.slice(displayedCount, displayedCount + patientsPerPage);
        
        patientsToDisplay.forEach(row => {
            const values = row.split(',');
            const patientDiv = createPatientDiv(headers, values, ['encounterId', 'bmi', 'referral']);
            patientDataContainer.appendChild(patientDiv);
            displayedCount++;
        });

        if (displayedCount < rows.length) {
            createShowMoreButton(patientDataContainer);
        }
    };

    const createPatientDiv = (headers, values, displayHeaders) => {
        const patientDiv = document.createElement('div');
        patientDiv.className = 'patient';
        
        displayHeaders.forEach(header => {
            const index = headers.indexOf(header);
            if (index !== -1 && index < values.length) {
                let dataValue = values[index];
                // Check if the header is 'referral' and modify the value accordingly
                if (header === 'referral') {
                    dataValue = (dataValue === '1') ? 'Yes' : 'No';
                }
                const dataP = document.createElement('p');
                dataP.textContent = `${header}: ${dataValue}`;
                patientDiv.appendChild(dataP);
            }
        });

        return patientDiv;
    };

    const createShowMoreButton = (container) => {
        const showMoreButton = document.createElement('button');
        showMoreButton.textContent = 'Show More Patients';
        showMoreButton.addEventListener('click', fetchMorePatients);
        container.appendChild(showMoreButton);
    };

    const fetchMorePatients = () => {
        fetchData();
    };

    fetchData();
});
