 var tables;
$(function(){
     tables = $('#tAccount').DataTable({
        //DOM元素的布局设置
        //"dom": 'Bfrtip',

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
       

        //状态
        //DataTables has the option of being able to save the state of a table (its paging position, ordering state etc)
        //so that is can be restored when the user reloads a page, or comes back to the page after visiting a sub-page.
        stateSave: true,
        //筛选
        "info":true,
        //排序
        "ordering": true,
        //"order": [[0, "asc" ]],
        //分页
        "paging":   true,
        // "pagingType": "simple_numbers", //numbers,simple,simple_numbers,full,full_numbers
        //滚动条
        //"scrollX": true,
        //"scrollY":"200px", //50vh表示 50%
        "scrollCollapse": true,
        //显示多少条数据
        "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],

        //对于语言数字的处理
        "language": {
            //处理i18n
            //"url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Chinese.json",
            "decimal": ",",
            "thousands": ".",
            "search": "Search:",
            "emptyTable":"No data available in table",
            //"info": "Showing page _PAGE_ of _PAGES_",
        },

        //列的设置
        "columnDefs": [
            {
                "targets": [ 2 ], //指定某个列
                "visible": true, //是否可见
                "searchable": true, //是否能够被筛选
                //当数据加载的时候，渲染cell
                "render": function ( data, type, row ) {
                    return data +' ('+ row[3]+')';
                },
            },
            {
                "targets": [ 3 ],
                "visible": true
            }
        ],

        //设置加载后列的排序
        // "aoColumns": [
        //     null,
        //     null,
        //     { "orderSequence": [ "asc" ] },
        //     { "orderSequence": [ "desc", "asc", "asc" ] },
        //     { "orderSequence": [ "desc" ] },
        //     null
        // ],

        //列的数据读取
        //其中name,position,office都是json格式中的key
        // "columns": [
        //     { "data": "name" },
        //     { "data": "position" },
        //     { "data": "office" },
        //     { "data": "age" },
        //     { "data": "start_date" },
        //     { "data": "salary" }
        // ],

        //当数据row产生的回调函数
        "createdRow": function ( row, data, index ) {
             //console.log(row);
         },

         //当点击header, footer的时候触发
         "footerCallback":function ( row, data, start, end, display ) {
             //console.log(data);
         }
    });

    // new $.fn.dataTable.Buttons( table, {
    //     buttons: [
    //         'copy', 'excel', 'pdf'
    //     ]
    // } );

   

    // table.buttons().container()
    // .appendTo( table.table().container() ) ;;

    //进行默认设置，但是可以除了指定的选项
    // $.extend( true, $.fn.dataTable.defaults, {
    //     "searching": false,
    //     "ordering": false
    // });

    //绑定datatable的事件，可以精确到row
    // $('#tAccount tbody').on('click', 'tr', function () {
    //     var data = table.row( this ).data();
    //     alert( 'You clicked on '+data[0]+'\'s row' );
    // } );


    //当排序，筛选，分页的时候，触发的事件
    // var eventFired = function ( type ) {
    //     var n = $('#demo_info')[0];
    //     n.innerHTML += '<div>'+type+' event - '+new Date().getTime()+'</div>';
    //     n.scrollTop = n.scrollHeight;      
    // }
 
    // $('#tAccount')
    //     .on( 'order.dt',  function () { eventFired( 'Order' ); } )
    //     .on( 'search.dt', function () { eventFired( 'Search' ); } )
    //     .on( 'page.dt',   function () { eventFired( 'Page' ); } )
    //     .DataTable();

    addButtons();

});


function addButtons(){
    tables.buttons().container()
    .appendTo($(".dataTables_header"));

    // $(".dt-buttons>a").each((index,element)=>{
    //     element.className += " btn btn-default";
    // });
}

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
 


// 如果用一条语句实现多个table的设置
// $(document).ready(function() {
//     $('table.display').DataTable();
// } );


//Row grouping：比较复杂，暂时不看

//从服务器端获取数据
//https://www.datatables.net/examples/server_side/


// 添加行
// $(document).ready(function() {
//     var t = $('#example').DataTable();
//     var counter = 1;
 
//     $('#addRow').on( 'click', function () {
//         t.row.add( [
//             counter +'.1',
//             counter +'.2',
//             counter +'.3',
//             counter +'.4',
//             counter +'.5'
//         ] ).draw( false );
 
//         counter++;
//     } );
 
//     // Automatically add a first row of data
//     $('#addRow').click();
// } );


