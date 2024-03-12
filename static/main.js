document.addEventListener('DOMContentLoaded', function () {
    function fetchData(url, callback) {
        fetch(url)
            .then(response => response.json())
            .then(data => callback(data))
            .catch(error => console.error('Error fetching data:', error));
    }

    function createBarChart(data) {

        const referralLabels = data.labels.map(label => {
            return label === 'NOT_REFERRED' ? 'Not Referred' : 'Referred';
        });
        
        const ctx = document.getElementById('barChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: referralLabels,
                datasets: [{
                    label: 'Referral Distribution',
                    data: data.values,
                    backgroundColor: 'rgba(75, 192, 192, 0.8)',
                }]
            },
            options: {
                responsive: false,
                maintainAspectRatio: false,
            }
        });
    }

    function createLineChart(data) {
        const ctx = document.getElementById('lineChart').getContext('2d');
        new Chart(ctx, {
            type: 'line',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Average End Tidal CO2',
                    data: data.values,
                    borderColor: 'rgba(255, 99, 132, 0.8)',
                    borderWidth: 2,
                    fill: false,
                }]
            },
            options: {
                responsive: false,
                maintainAspectRatio: false,
            }
        });
    }

    function createPieChart(data) {
        const ctx = document.getElementById('pieChart').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.values,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.8)',
                        'rgba(54, 162, 235, 0.8)',
                        'rgba(255, 206, 86, 0.8)',
                    ]
                }]
            },
            options: {
                responsive: false,
                maintainAspectRatio: false,
            }
        });
    }

    function createHistogramChart(data) {
        const ctx = document.getElementById('histogramChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Oxygen Flow Rate Distribution',
                    data: data.values,
                    backgroundColor: 'rgba(75, 192, 192, 0.8)',
                }]
            },
            options: {
                responsive: false,
                maintainAspectRatio: true,
                scales: {
                    x: {
                        type: 'linear',
                        position: 'bottom'
                    }
                }
            }
        });
    }

      // Map BMI values to categories
    function mapBmiToCategory(bmi) {
        if (bmi < 18.5) return 'Underweight';
        if (bmi >= 18.5 && bmi <= 24.9) return 'Healthy Weight';
        if (bmi >= 25.0 && bmi <= 29.9) return 'Overweight';
        if (bmi >= 30.0) return 'Obesity';
    }

    // Fetch data and create charts
    fetchData('http://127.0.0.1:5000/api/patients', function (data) {
        // Extract referral data
        const referralData = data.patients.map(patient => patient.referral);

        // Count occurrences of each referral type
        const referralCount = {};
        referralData.forEach(referral => {
            referralCount[referral] = (referralCount[referral] || 0) + 1;
        });

        // Prepare data for charts
        const labels = Object.keys(referralCount);
        const values = Object.values(referralCount);

        // Create charts
        createBarChart({ labels, values });

        // Extract oxygen flow rate data for the line chart
        const oxygenFlowRateData = data.patients
    .map(patient => patient.oxygen_flow_rate)
    .filter(rate => rate !== '')
    .map(rate => Math.round(parseFloat(rate))); 

        createLineChart({ labels: oxygenFlowRateData , values: oxygenFlowRateData });

        createHistogramChart({ labels: oxygenFlowRateData , values: oxygenFlowRateData });


        // Extract BMI data for the pie chart
        const bmiData = data.patients.map(patient => patient.bmi);
        const filteredBmiData = bmiData.filter(bmi => bmi !== undefined);
        const bmiCategories = filteredBmiData.map(bmi => mapBmiToCategory(bmi));
        const bmiDistribution = {};
        bmiCategories.forEach(category => {
            bmiDistribution[category] = (bmiDistribution[category] || 0) + 1;
        });

        // Prepare data for the pie chart
        const bmiLabels = Object.keys(bmiDistribution);
        const bmiValues = Object.values(bmiDistribution);

        createPieChart({ labels: bmiLabels, values: bmiValues });
    });
});
