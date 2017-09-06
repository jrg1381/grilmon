var EMPTY_STATUS = {"stdout": "", "stderr": "", returnCode: 0};

var app = angular.module('grilmon', [])
    .controller('GrilmonController', ['$scope', '$http', function ($scope, $http) {
        var grilmon = this;

        grilmon.shutdownScheduled = false;
        grilmon.status = EMPTY_STATUS;

        grilmon._processRemoteExec = function (data) {
            if (!data.stdout && data.returnCode === 0) {
                data.stdout = "Success";
            }
            return data;
        }

        grilmon.refresh = function () {
            grilmon.fetch();
            grilmon.status = EMPTY_STATUS;
        };

        grilmon.fetch = function () {
            $http({method: "GET", url: "/api/processes"}).then(function (response) {
                grilmon.lastUpdate = Date();
                grilmon.processes = response.data;
            })
        };

        grilmon.shutdown = function () {
            $http({method: "POST", url: "/api/shutdown"}).then(function (response) {
                grilmon.status = grilmon._processRemoteExec(response.data);
                grilmon.shutdownScheduled = !grilmon.shutdownScheduled;
            })
        };

        grilmon.closeBrowsers = function () {
            $http({method: "POST", url: "/api/close-browser"}).then(function (response) {
                grilmon.status = grilmon._processRemoteExec(response.data);
                grilmon.fetch();
            })
        };

        grilmon.fetch();
    }]);

app.config(['$interpolateProvider', function ($interpolateProvider) {
    $interpolateProvider.startSymbol('{A');
    $interpolateProvider.endSymbol('A}');
}]);
