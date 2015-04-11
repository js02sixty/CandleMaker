'use strict';

/* Controllers */

angular.module('cmApp.controllers', [])

    .controller('MainCtrl', ['$scope', 'Page', function($scope, Page) {
        $scope.Page = Page;
    }])

    .controller('HeaderCtrl', ['$scope', '$location', function($scope, $location) {
        $scope.isActive = function(viewLocation) {
            return viewLocation === $location.path();
        };
    }])

    .controller('ProductListCtrl', ['$scope', '$http', function($scope, $http) {
        $http.get('/api/product_categories')
            .success(function(data) {
                $scope.productCatagories = data.objects
            });
        $http.get('/api/product_types')
            .success(function(data) {
                $scope.productTypes = data.objects
            });
    }])

    .controller('HomeCtrl', ['$scope', 'Page', function($scope, Page) {
        Page.setTitle('Requiescents | Home');
    }])

    .controller('AdminCtrl', ['$scope', '$http', '$modal', 'Page', function($scope, $http, $modal, Page) {
        Page.setTitle('Requiescents | Admin');
        $scope.url = '/api/users';
        $scope.selectedUser = null;
        $scope.userCopy = null;

        $http.get($scope.url)
            .success(function(data) {
                $scope.users = data.objects;
            })
            .error(function(data) {
                $scope.users = data || "Request failed";
            });

        $scope.addUser = function(user) {
            $http.post($scope.url, {
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email
            })
                .success(function(data) {
                    $scope.users.push(data);
                })
        };

        $scope.deleteUser = function(user) {
            $http.delete($scope.url + "/" + user.id).
                success(function(response) {
                    $scope.users.splice($scope.users.indexOf(user), 1);
                });
        };

        $scope.updateUser = function(user) {
            $http.put($scope.url + "/" + user.id);
        };

        $scope.addUserModal = function() {
            $modal.open({
                templateUrl: 'partials/usermodal.html',
                controller: 'AddUserModalCtrl'
            })
                .result.then(function(user) {
                    $scope.addUser(user)
                });
        };

        $scope.updateUserModal = function(user) {
            $modal.open({
                templateUrl: '/partials/usermodal.html',
                controller: 'UpdateUserModalCtrl',
                resolve: {
                    user: function() {
                        return user
                    }
                }
            })
                .result.then(function(user) {
                    $scope.updateUser(user)
                });
        }
    }])

    .controller('AddUserModalCtrl', ['$scope', '$modalInstance', function($scope, $modalInstance) {
        $scope.title = "Add User";
        $scope.user = {};
        $scope.submit = function() {
            $modalInstance.close($scope.user);
        };

        $scope.cancel = function() {
            $modalInstance.dismiss('cancel');
        };
    }])

    .controller('UpdateUserModalCtrl', ['$scope', '$modalInstance', 'user', function($scope, $modalInstance, user) {
        $scope.title = "Update User";
        $scope.user = user;
        $scope.submit = function() {
            $modalInstance.close($scope.user);
        };

        $scope.cancel = function() {
            $modalInstance.dismiss('cancel');
        };
    }])

    .controller('AboutCtrl', ['$scope', '$modal', '$log', 'Page', function($scope, $modal, $log, Page) {

        Page.setTitle('Requiescents | About');
        $scope.items = ['item1', 'item2', 'item3'];

        $scope.open = function(size) {
            $modal.open({
                templateUrl: 'myModalContent.html',
                controller: 'ModalInstanceCtrl',
                size: size,
                resolve: {
                    bla: function() {
                        return $scope.items;
                    }
                }
            })
                .result.then(function(selectedItem) {
                    $scope.selected = selectedItem;
                }, function() {
                    $log.info('Modal dismissed at: ' + new Date());
                });
        };
    }])

    .controller('ProductsCtrl', ['$scope', '$http', 'Page', function($scope, $http, Page) {
        Page.setTitle('Requiescents | Products');

        $http.get('/api/products')
            .success(function(data) {
                $scope.products = data.objects
            });
    }])

    .controller('ContactCtrl', ['$scope', 'Page', function($scope, Page) {
        Page.setTitle('Requiescents | Contact');
    }]);
