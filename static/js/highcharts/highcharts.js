
document.addEventListener('DOMContentLoaded', function () {
    var trlLevel = "{{ data['TRL'] }}";
    console.log(trlLevel)
    var trlIndex = parseInt(trlLevel.replace('TRL', ''));

    Highcharts.chart('spyderChart', {

        chart: {
            polar: true,
            type: 'line'
        },
    
        accessibility: {
        },
    
        title: {
            text: '',
            x: -80
        },
    
        pane: {
            size: '80%'
        },
    
        xAxis: {
            categories: [
                'Investigación', 'Desarrollo Tecnológico', 'Implementación', 'Desarrollo Comercial'
            ],
            tickmarkPlacement: 'on',
            lineWidth: 0
        },
    
        yAxis: {
            gridLineInterpolation: 'polygon',
            lineWidth: 0,
            min: 0
        },
    
        tooltip: {
            shared: true,
            pointFormat: '<span style="color:{series.color}">{series.name}: <b>' +
                '${point.y:,.0f}</b><br/>'
        },
    
        legend: {
            enabled : false
        },
    
        series: [{
            name: 'Allocated Budget',
            data: [43000, 19000, 60000, 35000],
            pointPlacement: 'on'
        }],
    
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 600
                },
                chartOptions: {
                    legend: {
                        align: 'center',
                        verticalAlign: 'bottom',
                        layout: 'horizontal'
                    },
                    pane: {
                        size: '80%'
                    }
                }
            }]
        }
    
    });

    Highcharts.chart('spyderChart2', {

        chart: {
            polar: true,
            type: 'line'
        },
    
        accessibility: {
        },
    
        title: {
            text: '',
            x: -80
        },
    
        pane: {
            size: '80%'
        },
    
        xAxis: {
            categories: [
                'Investigación', 'Ensayos Preclínicos', 'Ensayos clínicos', 'Aprobación y Comercialización'
            ],
            tickmarkPlacement: 'on',
            lineWidth: 0
        },
    
        yAxis: {
            gridLineInterpolation: 'polygon',
            lineWidth: 0,
            min: 0
        },
    
        tooltip: {
            shared: true,
            pointFormat: '<span style="color:{series.color}">{series.name}: <b>' +
                '${point.y:,.0f}</b><br/>'
        },
    
        legend: {
            enabled : false
        },
    
        series: [{
            name: 'Allocated Budget',
            data: [40000, 12000, 20000, 37000],
            pointPlacement: 'on'
        }],
    
        responsive: {
            rules: [{
                condition: {
                    maxWidth: 600
                },
                chartOptions: {
                    legend: {
                        align: 'center',
                        verticalAlign: 'bottom',
                        layout: 'horizontal'
                    },
                    pane: {
                        size: '80%'
                    }
                }
            }]
        }
    
    });

});