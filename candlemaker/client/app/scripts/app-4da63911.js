"use strict";angular.module("cmApp",["restangular","ui.router"]).config(["$stateProvider","$urlRouterProvider","$locationProvider","RestangularProvider",function(t,a,e,r){r.setBaseUrl("/api/v1"),r.setDefaultHeaders({"content-type":"application/json"}),e.html5Mode(!0),t.state("home",{url:"/",templateUrl:"app/main/main.html",controller:"MainCtrl"}).state("home.products",{url:"products",templateUrl:"app/main/products/products.html",controller:"ProductsCtrl"}).state("home.about",{url:"about",templateUrl:"app/main/about/about.html"}).state("home.contact",{url:"contact",templateUrl:"app/main/contact/contact.html",controller:"ContactCtrl"}).state("cart",{url:"cart",templateUrl:"app/cart/cart.html"}),a.otherwise("/")}]),angular.module("cmApp").controller("ProductsCtrl",["$scope",function(t){t.ctrlName="ProductsCtrl"}]),angular.module("cmApp").controller("ContactCtrl",["$scope","Restangular",function(t,a){t.ctrlName="ContactCtrl",t.products=a.all("products").getList().$object}]),angular.module("cmApp").controller("AboutCtrl",["$scope",function(t){t.ctrlName="AboutCtrl"}]),angular.module("cmApp").controller("NavbarCtrl",["$scope",function(t){t.date=new Date}]),angular.module("cmApp").controller("MainCtrl",["$scope",function(t){t.ctrlName="MainCtrl"}]),angular.module("cmApp").run(["$templateCache",function(t){t.put("app/main/main.html",'<div class="container"><div id="top"><nav><ul><li ui-sref-active="active"><a ui-sref="home">Home</a></li><li ui-sref-active="active"><a ui-sref="home.products">Products</a></li><li ui-sref-active="active"><a ui-sref="home.about">About</a></li><li ui-sref-active="active"><a ui-sref="home.contact">Contact</a></li></ul></nav></div><div id="menu"><div ng-include="\'app/components/sidemenu/sidemenu.html\'" class="panel"></div></div><div id="content"><div ui-view="" class="panel"></div></div></div>'),t.put("app/components/navbar/navbar.html",'<nav ng-controller="NavbarCtrl"><a href="https://github.com/Swiip/generator-gulp-angular">Gulp Angular</a><ul><li class="active"><a ng-href="#">Home</a></li><li><a ng-href="#">About</a></li><li><a ng-href="#">Contact</a></li></ul><ul><li><a ng-href="#">Current date: {{ date | date:\'yyyy-MM-dd\' }}</a></li></ul></nav>'),t.put("app/components/sidemenu/sidemenu.html","<h1>menu</h1><hr>"),t.put("app/main/about/about.html",'<h1>About</h1><hr><p>welcome</p><form action="">First name:<br><input type="text" name="firstname" value="Mickey"><br>Last name:<br><input type="text" name="lastname" value="Mouse"><br><br><input type="submit" value="Submit"></form><table><thead><tr><th>#</th><th>Make</th><th>Model</th><th>Year</th></tr></thead><tbody><tr><td>1</td><td>Honda</td><td>Accord</td><td>2009</td></tr><tr><td>2</td><td>Toyota</td><td>Camry</td><td>2012</td></tr><tr><td>3</td><td>Hyundai</td><td>Elantra</td><td>2010</td></tr></tbody></table>'),t.put("app/main/contact/contact.html",'<h1>{{ctrlName}}</h1><ul><li ng-repeat="user in users">User: {{ user.username }} Email: {{ user.email }}</li></ul><ul><li ng-repeat="product in products">Products: {{ product.name }}</li></ul>'),t.put("app/main/products/products.html","<h1>Products</h1>")}]);