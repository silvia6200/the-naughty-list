'use strict';

/* Directives */
angular.module('clientAppDep', ['d3'])
.directive('d3Bars', ['$window', '$timeout',
  function($window, $timeout) {
    return {
      restrict: 'A',
      scope: {
        data: '=',
        label: '@',
        onClick: '&'
      },
      link: function(scope, ele, attrs) {
        var renderTimeout,
            dimensions = {
                width: 480,
                height : 320,
                margins : {
                    width : 20,
                    height : 60
                }
            },
            svg = d3.select(ele[0]).append('svg').style({
                'width' : dimensions.width+'px',
                'height' : dimensions.height+'px'
            });
 
 /* @todo replace test data with real data*/
        scope.data = [
            {'date_added': '2014-05-01', 'reason': 'Reason A ', 'count': 4},
            {'date_added': '2014-05-01', 'reason': 'Reason B', 'count': 12},
            {'date_added': '2014-05-01', 'reason': 'Reason D', 'count': 12},
            {'date_added': '2014-05-02', 'reason': 'Reason C', 'count': 22},
            {'date_added': '2014-05-02', 'reason': 'Reason D', 'count': 17},
            {'date_added': '2014-05-03', 'reason': 'Reason E', 'count': 5},
            {'date_added': '2014-05-03', 'reason': 'Reason F', 'count': 10},
            {'date_added': '2014-05-03', 'reason': 'Reason G', 'count': 20},
        ];

        $window.onresize = function() {scope.$apply();};
        scope.$watch(function() {
            return angular.element($window)[0].innerWidth;
        }, function() {
            scope.render(scope.data);
        });

        scope.$watch('data', function(newData) {
            scope.render(newData);
        }, true);

        scope.render = function(data) {
            svg.selectAll('*').remove(); if (!data) return; if (renderTimeout) clearTimeout(renderTimeout);
            
            var days = [], max_complaints = 1
            formationLoop:
            for (var k in data) {
                var i = days.length;
                if (i) {
                    for (; i--; ) {
                        if (data[k].date_added === days[i].date_added) {
                            days[i].complaints.push({
                                'reason': data[k].reason,
                                'count': data[k].count
                            });
                            if (days[i].complaints.length > max_complaints) {
                                max_complaints = days[i].complaints.length;
                            }
                            continue formationLoop;
                        }
                    }
                }
                days.push({
                    date_added: data[k].date_added,
                    complaints: [{
                        'reason': data[k].reason,
                        'count': data[k].count
                    }]
                });
            }
 
            renderTimeout = $timeout(function() {
                var   layers = { count : max_complaints, samples : days.length },
                        stack = d3.layout.stack();
                        layers.list = stack(d3.range(layers.count).map(function(a) {
                            var formed = [], counted;
                            for (var i = 0; i < days.length; i++) {
                                var counted = typeof days[i].complaints[a] !== 'undefined' ? days[i].complaints[a].count : 0;
                                var reason = typeof days[i].complaints[a] !== 'undefined' ? days[i].complaints[a].reason : '';
                                formed.push({
                                    x: i,
                                    y: counted,
                                    reason : reason
                                });
                            }
                            return formed; 
                        }));
                        layers.max = {y : d3.max(layers.list, function(layer) { return d3.max(layer, function(d) { return d.y0 + d.y; }); })};
                var   x = d3.scale.ordinal().domain(d3.range(layers.samples)).rangeRoundBands([0, dimensions.width], .08),
                        y = d3.scale.linear().domain([0, layers.max.y]).range([dimensions.height, 0]),
                        color = d3.scale.linear().domain([0, layers.count - 1]).range(['#2980b9', '#3498db']),
                        xAxis = d3.svg.axis().scale(x).tickSize(0).tickPadding(6).orient('bottom');

                var tip = 
                        d3
                        .tip()
                        .attr('class', 'd3-tip')
                        .html(function(d) {
                            return '<strong>' + d.y +' complaints </strong> due to <span style="color:#3498db">'+d.reason+'</span>';
                        });

                svg.call(tip);
                
                svg.selectAll('.layer')
                    .data(layers.list)
                    .enter().append('g')
                    .attr('class', 'layer')
                    .style('fill', function(d, i) { return color(i); })
                    .selectAll('rect')
                    .data(function(d) { return d; })
                    .enter()
                    .append('rect')
                    .attr('x', function(d) { return x(d.x); })
                    .attr('y', dimensions.height)
                    .on('mouseover', tip.show)
                    .on('mouseout', tip.hide)
                    .attr('width', x.rangeBand())
                    .attr('height', 0)
                    .transition()
                    .delay(function(d, i) { return i * 10; })
                    .attr('y', function(d) { return y(d.y0 + d.y); })
                    .attr('height', function(d) { return y(d.y0) - y(d.y0 + d.y); });

                svg.append('g')
                    .attr('class', 'x axis')
                    .attr('transform', 'translate(0,' + dimensions.width + ')')
                    .call(xAxis);
            }, 200);
          };
      }}
}]);