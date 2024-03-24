document.addEventListener('DOMContentLoaded', function() {
    const patientsPerPage = 9;
    let displayedCount = 0;

    const fetchCSV = async () => {
        try {
            const response = await fetch('Algorithm.csv');
            const data = await response.text();
            processData(data);
        } catch (error) {
            console.error('Error fetching CSV:', error);
        }
    };

    const processData = (csvData) => {
        const rows = csvData.split('\n');
        const headers = rows.shift().split(',');
        const patientDataContainer = document.getElementById('patientData');
    
        patientDataContainer.innerHTML = '';
    
        rows.slice(displayedCount, displayedCount + patientsPerPage).forEach(row => {
            const values = row.split(',');
            const patientDiv = document.createElement('div');
            patientDiv.className = 'patient';
    
            // Find indices of required fields
            const encounterIdIndex = headers.indexOf('encounterId');
            const bmiIndex = headers.indexOf('bmi');
            const referralIndex = headers.indexOf('referral');
            const predictedReferralIndex = headers.indexOf('predicted_referral');
    
            // Create elements for each field
            const encounterIdP = document.createElement('p');
            encounterIdP.textContent = `Encounter ID: ${values[encounterIdIndex]}`;
            patientDiv.appendChild(encounterIdP);
    
            const bmiP = document.createElement('p');
            bmiP.textContent = `BMI: ${values[bmiIndex]}`;
            patientDiv.appendChild(bmiP);
    
            const referralP = document.createElement('p');
            referralP.textContent = `Referral: ${values[referralIndex]}`;
            patientDiv.appendChild(referralP);
    
            const predictedReferralP = document.createElement('p');
            predictedReferralP.textContent = `Predicted Referral: ${values[predictedReferralIndex]}`;
            patientDiv.appendChild(predictedReferralP);
    
            patientDataContainer.appendChild(patientDiv);
            displayedCount++;
        });
    
        if (displayedCount < rows.length) {
            const showMoreButton = document.createElement('button');
            showMoreButton.textContent = 'Show More Patients';
            showMoreButton.addEventListener('click', fetchMorePatients);
            patientDataContainer.appendChild(showMoreButton);
        }
    };
    
    const fetchMorePatients = () => {
        fetchCSV();
    };

    fetchCSV();
});
