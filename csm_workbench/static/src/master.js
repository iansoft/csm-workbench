require("./master.css")

$(document).ready(function() {
    $().setupVerticalNavigation(true);

    //drag the modal 
    $(".modal").draggable({   
        handle: ".modal-header",   
        cursor: 'move',   
        refreshPositions: false  
    });  
});
