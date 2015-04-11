'use strict';

/* Config */

angular.module('cmApp', [
    'ngRoute',
//    'ngResource',
    'ngAnimate',
//    'mm.foundation',
//    'flow',
//    'cmApp.controllers',
//    'cmApp.services'
])
    .config(['$routeProvider', '$locationProvider', function($routeProvider, $locationProvider) {
        $routeProvider
            .when('/', {
                templateUrl: 'partials/home.html',
                controller: 'HomeCtrl'
            })
            .when('/admin', {
                templateUrl: 'partials/admin.html',
                controller: 'AdminCtrl'
            })
            .when('/products', {
                templateUrl: 'partials/products.html',
                controller: 'ProductsCtrl'
            })
            .when('/about', {
                templateUrl: 'partials/about.html',
                controller: 'AboutCtrl'
            })
            .when('/contact', {
                templateUrl: 'partials/contact.html',
                controller: 'ContactCtrl'
            })
            .otherwise({
                redirectTo: '/'
            });
        $locationProvider.html5Mode(true)
    }]);
