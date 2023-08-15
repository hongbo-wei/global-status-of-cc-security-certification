// Retrieve the chart select element
const chartSelect = document.getElementById('chartSelect');
// Retrieve the chart container element
const chartContainer = document.getElementById('chartContainer');

// Initialize the ECharts instance
const chart = echarts.init(chartContainer);

// Add an event listener to the select element
chartSelect.addEventListener('change', function() {
  const selectedChart = chartSelect.value;

  // Clear any existing chart
  chart.clear();

  // Generate and display the selected chart
  if (selectedChart === 'bar') {
    generateBarChart();
  } else if (selectedChart === 'pie') {
    generatePieChart();
  } else if (selectedChart === 'line') {
    generateLineChart();
  }
});

// Functions to generate different types of charts
function generateBarChart() {
  const options = {
    // Configuration options for the bar chart
    // Refer to the Apache ECharts documentation for the specific configuration
    xAxis: {
      type: 'category',
      data: ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        type: 'bar',
        data: [10, 20, 30, 40, 50],
      },
    ],
  };

  // Set the options and render the chart
  chart.setOption(options);
}

function generatePieChart() {
  const options = {
    // Configuration options for the pie chart
    // Refer to the Apache ECharts documentation for the specific configuration
    series: [
      {
        type: 'pie',
        data: [
          { name: 'Category 1', value: 10 },
          { name: 'Category 2', value: 20 },
          { name: 'Category 3', value: 30 },
          { name: 'Category 4', value: 40 },
          { name: 'Category 5', value: 50 },
        ],
      },
    ],
  };

  // Set the options and render the chart
  chart.setOption(options);
}

function generateLineChart() {
  const options = {
    // Configuration options for the line chart
    // Refer to the Apache ECharts documentation for the specific configuration
    xAxis: {
      type: 'category',
      data: ['Category 1', 'Category 2', 'Category 3', 'Category 4', 'Category 5'],
    },
    yAxis: {
      type: 'value',
    },
    series: [
      {
        type: 'line',
        data: [10, 20, 30, 40, 50],
      },
    ],
  };

  // Set the options and render the chart
  chart.setOption(options);
}
