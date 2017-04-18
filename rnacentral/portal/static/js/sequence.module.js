(function() {

var xrefResourceFactory = function($resource) {
    return $resource(
        '/api/v1/rna/:upi/xrefs/',
        {upi: '@upi', taxid: '@taxid', page: '@page'},
        {
            get: {timeout: 5000, isArray: false}
        }
    );
};
xrefResourceFactory.$inject = ['$resource'];

var xrefsComponent = {
    bindings: {
        upi: '@',
        taxid: '@?'
    },
    controller: function() {
        var ctrl = this;

        $scope.xrefs = xrefResource.get(
            {upi: this.upi, taxid: this.taxid},
            function (data) {
                // hide loading spinner
            },
            function () {
                // display error
            }
        );

        xrefResource.get(
            { upi: $scope.upi, taxid: $scope.taxid },
            function(data) {
                console.log($scope.xrefs);
            }
        );

    },
    templateUrl: "/static/js/xrefs.html"
};

var taxonomyComponent = {
    bindings: {
        upi: '<',
        taxid: '<?'
    },
    controller: ['$http', '$interpolate',  function($http, $interpolate) {
        var ctrl = this;

        ctrl.$onInit = function() {
            var d3_species_tree = $('#d3-species-tree');

            if (!document.createElement('svg').getAttributeNS) {
                d3_species_tree.html('Your browser does not support SVG');
            }
            else {
                $http({
                    url: $interpolate("/rna/{{upi}}/lineage")({ upi: ctrl.upi }),
                    method: 'GET'
                }).then(
                    function(response) {
                        ctrl.response = response;
                        d3SpeciesTree(response.data, ctrl.upi, '#d3-species-tree');
                    },
                    function(response) {
                        ctrl.response = response;
                    }
                )
            }
        };
    }],
    template: '<div id="d3-species-tree">' +
              '    <div ng-if="!$ctrl.response">' +
              '        <i class="fa fa-spinner fa-spin fa-2x"></i><span class="margin-left-5px">Loading taxonomic tree...</span>' +
              '    </div>' +
              '    <div ng-if="$ctrl.response.status >= 400" class="alert alert-danger fade">' +
              '        <i class="fa fa-exclamation-triangle"></i>Sorry, there was a problem loading the data. Please try again and contact us if the problem persists.' +
              '    </div>' +
              '</div>'
};


var publicationResourceFactory = function($resource) {
    return $resource(
        '/api/v1/rna/:upi/publications?page_size=:page',
        {upi: '@upi', page: '@page'},
        {
            get: {timeout: 5000, isArray: false}
        }
    );
};
publicationResourceFactory.$inject = ['$resource'];

var abstractResourceFactory = function($resource) {
    return $resource(
        'http://www.ebi.ac.uk/europepmc/webservices/rest/search/query=ext_id\\::pubmed_id&format=json&resulttype=core',
        {pubmed_id: '@pubmed_id'},
        {
            jsonp: { method: 'JSONP', params: {callback : 'JSON_CALLBACK'} }
        }
    );
};
abstractResourceFactory.$inject = ['$resource'];

var publicationsComponent = {
    bindings: {
        upi: '<',
        taxid: '<?'
    },
    controller: ['publicationResource', 'abstractResource', '$http', '$interpolate', function(publicationResource, abstractResource, $http, $interpolate) {
        var ctrl = this;

        ctrl.$onInit = function() {
            var pageSize = 25;

            ctrl.abstracts = {};
            ctrl.publications = publicationResource.get(
                { upi: this.upi, page_size: pageSize },
                function(publications) {
                    // retrieve corresponding abstracts
                    for (var i=0; i < publications.results.length; i++) {
                        var pubmed_id = publications.results[i].pubmed_id;
                        // $http.jsonp(
                        //     $interpolate('http://www.ebi.ac.uk/europepmc/webservices/rest/search/query=ext_id:{{pubmed_id}}&format=json&resulttype=core')({pubmed_id: pubmed_id})
                        // ).then(
                        //     function(response) {
                        //         console.log(response);
                        //     },
                        //     function(response) {
                        //         console.log(response);
                        //     }
                        // );

                        // abstractResource.jsonp(
                        //     { pubmed_id: pubmed_id },
                        //     function(abstract) {
                        //         ctrl.abstracts[pubmed_id] = abstract;
                        //         console.log("ctrl.publications = ", ctrl.publications);
                        //         console.log("ctrl.abstracts = ", ctrl.abstracts);
                        //     }
                        // );

                        $.ajax({
                            url: 'http://www.ebi.ac.uk/europepmc/webservices/rest/search/query=ext_id:' + pubmed_id + '&format=json&resulttype=core',
                            dataType: "jsonp",
                            jsonp: false, // prevent jQuery from modifying the callback bit in the url
                            jsonpCallback: "callback", // tell what callback function to use
                        }).done(function(data){
                            console.log(data);
                            ctrl.abstracts[pubmed_id] = data;
                        }).fail(function(response){
                            console.log(response);
                        });
                    }
                }
            );
        };

        ctrl.loadMore = function() {
            var newPageSize = ctrl.publications.data.length + pageSize;
            ctrl.publications = publicationResource.get(
                { upi: this.upi, page_size: newPageSize },
                function(publications) {
                    // retrieve corresponding abstracts
                    for (var i=0; i < publications.results.length; i++) {
                        var pubmed_id = publications.results[i].pubmed_id;
                        ctrl.abstracts[pubmed_id] = abstractResource.get(pubmed_id);
                    }
                }
            );
        };
    }],
    template: '<div id="publications">' +
              '    <h2>Publications <small>{{ $ctrl.publications.count }}</small></h2>' +
              '    <ol>' +
              '        <div ng-repeat="publication in $ctrl.publications.results" class="col-md-8">' +
              '            <li class="margin-bottom-10px">' +
              '                <strong ng-if="publication.title">{{ publication.title }}</strong>' +
              '                <br ng-if="publication.title">' +
              '                <small>' +
              '                    <span ng-repeat="author in publication.authors track by $index"><a href="/search?q=author:&#34;{{ author }}&#34;">{{ author }}</a>{{ $last ? "" : ", " }}</span>' +
              '                    <br ng-if="publication.authors && publication.authors.length">' +
              '                    <em ng-if="publication.publication">{{ publication.publication }}</em>' +
              '                    <span ng-if="publication.pubmed_id">' +
              '                        <a href="http://www.ncbi.nlm.nih.gov/pubmed/{{ publication.pubmed_id }}" class="margin-left-5px">Pubmed</a>' +
              '                        <a ng-if="publication.doi" href="http://dx.doi.org/{{ publication.doi }}" target="_blank" class="abstract-control">Full text</a>' +
              '                        <button class="btn btn-xs btn-default abstract-btn abstract-control" ng-click="abstractVisible = !abstractVisible"><span ng-if="abstractVisible">Show abstract</span><span ng-if="!abstractVisible">Hide abstract</span></button>' +
              '                        <div ng-if="abstractVisible" class="abstract-text">{{ $ctrl.abstracts[publication.pubmed_id] }}</div>' +
              '                    </span>' +
              '                  <br>' +
              '                  <a href="/search?q=pub_id:&#34;{{ publication.pubmed_id }}&#34;" class="margin-left-5px"><i class="fa fa-search"></i> Find other sequences from this reference</a>' +
              '                </small>' +
              '            </li>' +
              '        </div>' +
              '    </ol>' +
              '    <div ng-if="$ctrl.publications.count < $ctrl.publications.total" class="col-md-8">' +
              '        <small class="text-muted">Displaying {{ $ctrl.publication.count }} of {{ $ctrl.publications.total }} publications</small>' +
              '        <br>' +
              '        <button class="btn btn-default btn-large" id="load-more-publications">Load more</button>' +
              '    </div>' +
              '    <div class="row">' +
              '        <div ng-if="!$ctrl.publications" class="col-md-12">' +
              '            <i class="fa fa-spinner fa-spin fa-2x"></i>' +
              '            <span class="margin-left-5px">Loading publications...</span>' +
              '        </div>' +
              '    ' +
              '    </div>' +
              '</div>'
};


var rnaSequenceController = function($scope, $location, $http, $interpolate, xrefResource, DTOptionsBuilder, DTColumnBuilder) {
    // Take upi and taxid from url. Note that $location.path() always starts with slash
    $scope.upi = $location.path().split('/')[2];
    $scope.taxid = $location.path().split('/')[3]; // TODO: this might not exist!

    $scope.xrefs = $http({
        url: $interpolate('/rna/{{upi}}/xrefs/{{taxid}}', false, null, true)({ upi: $scope.upi, taxid: $scope.taxid }),
        method: 'GET'
    }).then(
        function(response) {
            $("#annotations-table").html(response.data);
            $("#annotations-table").DataTable({
                "columns": [null, null, null, {"bVisible": false}, {"bVisible": false}, {"bVisible": false}], // hide columns, but keep them sortable
                "autoWidth": true, // pre-recalculate column widths
                "dom": "ftpil", // filter, table, pagination, information, length
                //"paginationType": "bootstrap", // requires dataTables.bootstrap.js
                "deferRender": true, // defer rendering until necessary
                "language": {
                    "search": "", // don't display the "Search:" bit
                    "info": "_START_-_END_ of _TOTAL_", // change the informational text
                    "paginate": {
                        "next": "",
                        "previous": "",
                    }
                },
                "order": [[ 5, "desc" ]], // prioritize entries with genomic coordinates
                "lengthMenu": [[5, 10, 20, 50, -1], [5, 10, 20, 50, "All"]],
                "initComplete": function(settings, json) {
                    console.log("init complete");
                }
            });
        },
        function(response) {
            // handle error
        }
    );

};
rnaSequenceController.$inject = ['$scope', '$location', '$http', '$interpolate', 'xrefResource', 'DTOptionsBuilder', 'DTColumnBuilder'];


/**
 * Configuration function that allows this module to load data
 * from white-listed domains.
 * @param $sceDelegateProvider
 */
var sceWhitelist = function($sceDelegateProvider) {
    $sceDelegateProvider.resourceUrlWhitelist([
        // Allow same origin resource loads.
        'self',
        // Allow loading from EBI
        'http://www.ebi.ac.uk/**'
    ]);
};
sceWhitelist.$inject = ['$sceDelegateProvider'];


angular.module("rnaSequence", ['datatables', 'ngResource'])
    .config(sceWhitelist)
    .factory("xrefResource", xrefResourceFactory)
    .factory("publicationResource", publicationResourceFactory)
    .factory("abstractResource", abstractResourceFactory)
    .controller("rnaSequenceController", rnaSequenceController)
    .component("xrefsComponent", xrefsComponent)
    .component("taxonomyComponent", taxonomyComponent)
    .component("publicationsComponent", publicationsComponent);

})();
