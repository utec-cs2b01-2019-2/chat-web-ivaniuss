  
$(function(){
    var url = "http://127.0.0.1:8000/users";
    $("#grid").dxDataGrid({
        dataSource: DevExpress.data.AspNet.createStore({
            key: "id",
            loadUrl: url,
            onBeforeSend: function(method, ajaxOptions) {
                ajaxOptions.xhrFields = { withCredentials: true };
            }
        }),

        editing: {
            allowUpdating: false,
            allowDeleting: false,
            allowAdding: false
        },

        remoteOperations: {
            sorting: true,
            paging: true
        },

        paging: {
            pageSize: 12
        },

        pager: {
            showPageSizeSelector: true,
            allowedPageSizes: [8, 12, 20]
        },

        columns: [{
            dataField: "id",
            dataType: "number",
            allowEditing: false
        }, {
            dataField: "username"
        }, {
            dataField: "name"
        }, {
            dataField: "fullname"
        }, {
            dataField: "password"
        }, ],
    }).dxDataGrid("instance");
});