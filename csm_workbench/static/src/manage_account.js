//define some variables
var tAccount = null;
var vfAccount = null;

$(function(){
    //hide some controls
    $("#btnCreate").hide();
    $("#btnUpdate").hide();

    //render to table
    tAccount =  $('#tAccount')
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
    tAccount.buttons().container()
            .appendTo($(".dataTables_header"));


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
                            message: 'please type the same password.'
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
                            message: 'please type the same password.'
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

    //define the validator for account form 
    vfAccount = $('#fAccount').data('bootstrapValidator'); 
    // vfAccount.disableSubmitButtons(true);

    //render the modal
    $('#mAccount')
        .on('show.bs.modal', function (event) {
            var button = $(event.relatedTarget) 
            var action = button.data('action')

            var modal = $(this)
            if(action == "create"){
                $("#btnCreate").show();
                $("#btnEdit").hide();
                modal.find('.modal-title').text('Add Account');
            }
            else if(action == "edit"){
                $("#btnCreate").hide();
                $("#btnEdit").show();
                modal.find('.modal-title').text('Edit Account');
            }
        })
        .on('hide.bs.modal', function (e) {
            //reset the form anyway
            vfAccount.resetForm();
            $(".alert").remove();
        }); 

        
        //es6...
        $("#btnCreate").click(function(){
            vfAccount.validate();
            if (vfAccount.isValid() == false){
                csmFormAlert("fAccount", "danger", false, "message!!!");
                return false;
            }
            else{
                console.log("create");
                // csmHttpService
            }
        });
});