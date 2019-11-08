  
$(function(){
    var url = 'postgres://cmrxbadkuqhcpf:f285929a2e21a5547d29bcd8accef35bea2dfccd269ca90ee78bf9c4dd0252d8@ec2-23-21-115-109.compute-1.amazonaws.com:5432/d7cf77eum358n2'
    $("#grid").dxDataGrid({
        dataSource: DevExpress.data.AspNet.createStore({
            key: "id",
            loadUrl: url,
            insertUrl: url,
            updateUrl: url,
            deleteUrl: url,
            onBeforeSend: function(method, ajaxOptions) {
                ajaxOptions.xhrFields = { withCredentials: true };
            }
        }),

        editing: {
            allowUpdating: true,
            allowDeleting: true,
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
            showPageSizeSelector: false,
            allowedPageSizes: [8, 12, 20]
        },

        columns: [{
            dataField: "id",
            dataType: "number",
            allowEditing: true
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