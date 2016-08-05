$(function(){
    //render to table
    var tables =  $('#tAccount')
        .on('init.dt', function (e, settings, json) {
            //nothing to do
        })
        .DataTable({
            // ajax: {
            //     url: '/api/myData',
            //     dataSrc: 'data'
            // },
            // columns: [ 

            // ],
            buttons: [
                {
                    extend: 'csv',
                    text: 'Download CSV',
                    className: 'btn btn-default' 
                },
                {
                    //这是一个自定义的按钮
                    text: 'Reload',
                    className: 'btn btn-default',
                    action: function ( e, dt, node, config ) {
                        dt.ajax.reload();
                    }
                }
            ],   
        });
    
    //move the table.buttons to the correct position
    tables.buttons().container()
            .appendTo($(".dataTables_header"));

    //render the modal
    $('#mAccount')
        .on('show.bs.modal', function (event) {
            let button = $(event.relatedTarget) 
            let action = button.data('action')

            let modal = $(this)
            if(action == "add"){
                modal.find('.modal-title').text('Add Account');
            }
            else if(action == "edit"){
                modal.find('.modal-title').text('Edit Account');
            }
        
            console.log("打开模态框!");
        })
        .on('hidden.bs.modal', function (e) {
            console.log("关闭模态框!");
        });

    //validate the account form 
    $('#fAccount')
        .on('error.field.bv', function(e, data) {
        })
        .on('success.field.bv', function(e, data) {
        })
        .on('added.field.bv', function(e, data) {
        })
        .on('removed.field.bv', function(e, data) {
        })
        .bootstrapValidator({
            fields: {
                username: {
                    message: '',
                    validators: {
                        notEmpty: {
                            message: 'the user name is required.'
                        },
                        // remote: {
                        //     type: 'GET',
                        //     url: '/account/service/checkexist/',
                        //     message: 'the user name is existed.',
                        //     data: {
                        //         type: 'username'
                        //     }
                        // },
                    }
                },
                password: {
                    validators: {
                        notEmpty: {
                            message: 'the password is required.'
                        },
                        identical: {
                            field: 'retypePassword',
                            message: 'the password is not validate'
                        }
                    }
                },
                retypePassword: {
                    validators: {
                        notEmpty: {
                            message: 'the password is required.'
                        },
                        identical: {
                            field: 'password',
                            message: 'the password is not validate'
                        }
                    }
                },
                domain: {
                    validators: {
                        notEmpty: {
                            message: 'the domain is required.'
                        }
                    }
                }
            }
        });
});

